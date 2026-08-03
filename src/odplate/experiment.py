from __future__ import annotations

from pathlib import Path
import json
import pandas as pd

from .config import cargar_configuracion, guardar_configuracion
from .io import leer_carpeta_cruda
from .processing import procesar_matrices
from .series import Serie, catalogo_series, extraer_serie, filtrar_catalogo
from .metrics import metricas_serie, metricas_frente_control
from .models import seleccionar_mejor_modelo
from .metrics.ranking import ranking, describir_criterio
from .plotting import graficar
from .reporting import (
    exportar_excel,
    exportar_csv,
    generar_html,
    generar_docx,
    generar_pdf_desde_docx,
    exportar_matrices_por_id,
    exportar_series_por_grupo,
)


class Experimento:
    """Objeto central para ejecutar y documentar un experimento de OD."""

    def __init__(self, configuracion):
        self.config = cargar_configuracion(configuracion)
        self.crudas = None
        self.matrices = None
        self.tablas: dict[str, pd.DataFrame] = {}
        self.figuras = []
        self.criterios_usados: list[dict] = []
        self._cache: dict[tuple, object] = {}

    @classmethod
    def desde_configuracion(cls, origen):
        return cls(origen)

    @property
    def series(self):
        return catalogo_series(self.config)

    def obtener_series(self, tipo="todos", aceite=None, grupo=None, incluir_ids=None, excluir_ids=None):
        return filtrar_catalogo(
            self.config,
            aceites=[aceite] if aceite else None,
            grupos=[grupo] if grupo else None,
            incluir_ids=incluir_ids,
            excluir_ids=excluir_ids,
            tipo=tipo,
        )

    def limpiar_cache(self):
        self._cache.clear()
        return self

    def cargar_resultados(
        self,
        ruta,
        nombre_blanco,
        hoja=None,
        extractor_tiempo=None,
        coincidencia_blanco="igual",
    ):
        kwargs = {} if extractor_tiempo is None else {
            "extractor_tiempo": extractor_tiempo
        }
        self._cache.clear()
        self.crudas = leer_carpeta_cruda(
            ruta,
            nombre_blanco,
            self.config.get("filas", 8),
            self.config.get("columnas", 12),
            hoja,
            coincidencia_blanco=coincidencia_blanco,
            **kwargs,
        )
        return self

    def procesar(self, restar_blanco=True, ddof=1):
        if self.crudas is None:
            raise RuntimeError("Primero cargue los resultados.")
        self._cache.clear()
        self.matrices = procesar_matrices(
            self.crudas,
            self.config["submatriz"],
            restar_blanco,
            ddof=ddof,
        )
        return self

    def calcular_todo(
        self,
        normalizacion="ninguno",
        ajustar_modelos=True,
        control_indice=0,
        criterio_ranking=None,
        mayor_es_mejor=True,
        criterio_kwargs=None,
    ):
        """
        Calcula estadísticas descriptivas y modelos para todas las series.

        El ranking solo se calcula cuando el usuario entrega explícitamente
        ``criterio_ranking``. Así la biblioteca nunca decide por sí misma qué
        significa "mejor".
        """
        if self.matrices is None:
            raise RuntimeError("Primero procese las matrices.")

        catalogo = catalogo_series(self.config)
        controles = [x for x in catalogo if x.es_control]
        if not controles:
            raise RuntimeError("No hay control.")
        if not 0 <= control_indice < len(controles):
            raise IndexError("control_indice está fuera del rango disponible.")

        control = controles[control_indice]
        metricas_control = metricas_serie(
            self.matrices,
            control.como_dict(),
            self.config["submatriz"],
            normalizacion=normalizacion,
        )

        filas = []
        curvas = []
        modelos = []
        for item in catalogo:
            metricas = metricas_serie(
                self.matrices,
                item.como_dict(),
                self.config["submatriz"],
                normalizacion=normalizacion,
            )
            fila = {
                "id": item.id, "nombre": item.nombre, "tipo": item.tipo,
                "grupo": item.grupo, "aceite": item.aceite,
                "concentracion": item.concentracion, "es_control": item.es_control,
            } | metricas
            if not item.es_control:
                fila |= metricas_frente_control(metricas, metricas_control)
            filas.append(fila)

            datos = extraer_serie(
                self.matrices,
                item.como_dict(),
                self.config["submatriz"],
                normalizacion=normalizacion,
            )
            for i, tiempo in enumerate(datos["tiempo"]):
                curvas.append(
                    {
                        "id": item.id, "nombre": item.nombre, "tipo": item.tipo,
                        "grupo": item.grupo, "aceite": item.aceite,
                        "concentracion": item.concentracion, "es_control": item.es_control,
                    }
                    | {
                        "tiempo": tiempo,
                        "mean": datos["mean"][i],
                        "std": datos["std"][i],
                        "sem": datos["sem"][i],
                        "n": datos["n"][i],
                    }
                )

            if ajustar_modelos:
                ajuste = seleccionar_mejor_modelo(
                    datos["tiempo"], datos["mean"]
                )
                for modelo in ajuste["ajustes"]:
                    modelos.append(
                        {
                            "id": item.id, "aceite": item.aceite,
                            "grupo": item.grupo, "nombre": item.nombre,
                            "tipo": item.tipo
                        } | modelo
                    )

        self.tablas["Resumen_series"] = pd.DataFrame(filas)
        self.tablas["Curvas"] = pd.DataFrame(curvas)
        self.tablas["Ajustes_modelos"] = pd.DataFrame(modelos)

        if criterio_ranking is not None:
            self.calcular_ranking(
                criterio=criterio_ranking,
                mayor_es_mejor=mayor_es_mejor,
                criterio_kwargs=criterio_kwargs,
                guardar_como="Ranking",
            )
        else:
            self.tablas.pop("Ranking", None)

        return self.tablas

    def calcular_ranking(
        self,
        criterio,
        n=None,
        mayor_es_mejor=True,
        aceites=None,
        grupos=None,
        incluir_ids=None,
        excluir_ids=None,
        tiempos=None,
        criterio_kwargs=None,
        guardar_como="Ranking",
        tipo="tratamiento",
        incluir_controles=None,
    ):
        """Calcula un ranking con un criterio proporcionado por el usuario."""
        if self.matrices is None:
            raise RuntimeError("Primero procese las matrices.")

        kwargs = dict(criterio_kwargs or {})
        tabla = ranking(
            config=self.config,
            matrices=self.matrices,
            criterio=criterio,
            submatriz=self.config["submatriz"],
            n=n,
            mayor_es_mejor=mayor_es_mejor,
            aceites=aceites,
            grupos=grupos,
            incluir_ids=incluir_ids,
            excluir_ids=excluir_ids,
            tiempos=tiempos,
            tipo=tipo,
            incluir_controles=incluir_controles,
            **kwargs,
        )
        if guardar_como:
            self.tablas[guardar_como] = tabla
        self._registrar_criterio(
            criterio,
            mayor_es_mejor,
            uso=f"ranking:{guardar_como or 'no_guardado'}",
            parametros=kwargs,
        )
        return tabla

    def graficar(self, **kwargs):
        if self.matrices is None:
            raise RuntimeError("Primero procese las matrices.")
        resultado = graficar(self.config, self.matrices, **kwargs)
        self.figuras.extend(resultado["rutas"])
        if resultado.get("criterio"):
            metadatos = dict(resultado["criterio"])
            metadatos["uso"] = f"grafica:{kwargs.get('modo', 'grupos')}"
            self._agregar_criterio_si_nuevo(metadatos)
        if resultado.get("ranking") is not None:
            self.tablas["Ranking_ultima_grafica"] = resultado["ranking"]
        return resultado

    def _registrar_criterio(
        self,
        criterio,
        mayor_es_mejor,
        uso,
        parametros=None,
    ):
        metadatos = describir_criterio(
            criterio, mayor_es_mejor
        ).como_dict()
        metadatos["uso"] = uso
        metadatos["parametros"] = parametros or {}
        self._agregar_criterio_si_nuevo(metadatos)

    def _agregar_criterio_si_nuevo(self, metadatos):
        clave = json.dumps(metadatos, ensure_ascii=False, sort_keys=True, default=str)
        existentes = {
            json.dumps(x, ensure_ascii=False, sort_keys=True, default=str)
            for x in self.criterios_usados
        }
        if clave not in existentes:
            self.criterios_usados.append(metadatos)
        self._actualizar_tabla_criterios()

    def _actualizar_tabla_criterios(self):
        if not self.criterios_usados:
            self.tablas.pop("Criterios_ranking", None)
            return
        filas = []
        for criterio in self.criterios_usados:
            fila = dict(criterio)
            fila["parametros"] = json.dumps(
                fila.get("parametros", {}), ensure_ascii=False, default=str
            )
            filas.append(fila)
        self.tablas["Criterios_ranking"] = pd.DataFrame(filas)

    
    def exportar_datos_matrices(
        self,
        carpeta="datos_matrices",
        orden_ids=None,
        nombres_filas=None,
        nombres_columnas=None,
        decimales=4,
        incluir_blanco=True,
        tipo_series="todos",
        incluir_ids=None,
        excluir_ids=None,
    ):
        """
        Genera los dos archivos detallados de matrices.

        Archivos generados
        ------------------
        matrices_por_id.xlsx
            Matrices de cada ID y del blanco.

        series_por_grupo.xlsx
            Series organizadas por grupo y por tiempo.
        """

        if self.matrices is None:
            raise RuntimeError(
                "Primero procese las matrices."
            )

        carpeta = Path(
            carpeta
        )
        carpeta.mkdir(
            parents=True,
            exist_ok=True,
        )

        ruta_matrices = exportar_matrices_por_id(
            matrices=self.matrices,
            ruta_excel=carpeta / "matrices_por_id.xlsx",
            orden_ids=orden_ids,
            nombres_filas=nombres_filas,
            nombres_columnas=nombres_columnas,
            decimales=decimales,
            incluir_blanco=incluir_blanco,
        )

        ruta_series = exportar_series_por_grupo(
            config=self.config,
            matrices=self.matrices,
            ruta_excel=carpeta / "series_por_grupo.xlsx",
            tiempos=orden_ids,
            tipo=tipo_series,
            incluir_ids=incluir_ids,
            excluir_ids=excluir_ids,
            decimales=decimales,
        )

        return {
            "matrices_por_id": ruta_matrices,
            "series_por_grupo": ruta_series,
        }
    
    
    
    def generar_reporte(
        self,
        carpeta="reporte_od",
        formatos=(
            "xlsx",
            "html",
            "docx",
            "pdf",
            "csv",
        ),
        titulo="Reporte de análisis OD",
        incluir_matrices_detalladas=True,
        orden_ids=None,
        decimales_matrices=4,
    ):
        if not self.tablas:
            self.calcular_todo()
        self._actualizar_tabla_criterios()

        carpeta = Path(carpeta)
        carpeta.mkdir(parents=True, exist_ok=True)
        guardar_configuracion(self.config, carpeta / "configuracion.json")
        salidas = {"configuracion": carpeta / "configuracion.json"}

        if incluir_matrices_detalladas:
            salidas["matrices_detalladas"] = (
                self.exportar_datos_matrices(
                    carpeta=carpeta / "matrices",
                    orden_ids=orden_ids,
                    decimales=decimales_matrices,
                )
            )

        if "xlsx" in formatos:
            salidas["xlsx"] = exportar_excel(
                self.tablas, carpeta / "resultados.xlsx"
            )
        if "csv" in formatos:
            salidas["csv"] = exportar_csv(self.tablas, carpeta / "csv")
        if "html" in formatos:
            salidas["html"] = generar_html(
                titulo,
                self.config,
                self.tablas,
                self.figuras,
                carpeta / "reporte.html",
            )
        if "docx" in formatos or "pdf" in formatos:
            salidas["docx"] = generar_docx(
                titulo,
                self.config,
                self.tablas,
                self.figuras,
                carpeta / "reporte.docx",
            )
        if "pdf" in formatos:
            try:
                salidas["pdf"] = generar_pdf_desde_docx(
                    salidas["docx"], carpeta / "reporte.pdf"
                )
            except Exception as error:
                salidas["pdf_error"] = str(error)

        manifest = {
            "salidas": {k: str(v) for k, v in salidas.items()},
            "criterios_usados": self.criterios_usados,
        }
        (carpeta / "manifest.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2, default=str),
            encoding="utf-8",
        )
        return salidas


class ExperimentoOD(Experimento):
    """Especialización compatible para experimentos de densidad óptica."""

