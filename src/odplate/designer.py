"""Editor visual de configuraciones de placas para Jupyter y Google Colab."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple
import json
import string

import ipywidgets as widgets
from IPython.display import display, clear_output


@dataclass
class Bloque:
    fila: int
    columnas: List[int]

    @property
    def pozos(self) -> Set[Tuple[int, int]]:
        return {(self.fila, c) for c in self.columnas}


@dataclass
class Serie:
    id: str
    nombre: str
    cantidad: Any
    aceite: str
    grupo: str
    bloque: Bloque
    color: str


@dataclass
class Control:
    id: str
    nombre: str
    bloque: Bloque
    color: str = "#d62728"


class PlateDesigner:
    """Diseñador visual de placas con grupos disjuntos y controles múltiples."""

    PALETA = [
        "#4c78a8", "#f58518", "#54a24b", "#e45756",
        "#72b7b2", "#b279a2", "#ff9da6", "#9d755d",
        "#bab0ac", "#17becf", "#9467bd", "#8c6d31",
    ]

    def __init__(
        self,
        filas: int = 8,
        columnas: int = 12,
        submatriz: int = 3,
        titulo: str = "PlateDesigner",
        bloques_alineados: bool = True,
    ) -> None:
        self.filas = int(filas)
        self.columnas = int(columnas)
        self.submatriz = int(submatriz)
        self.titulo = titulo
        self.bloques_alineados = bool(bloques_alineados)
        self._validar_dimensiones()

        self.series: Dict[str, Serie] = {}
        self.controles: Dict[str, Control] = {}
        self.ocupacion: Dict[Tuple[int, int], str] = {}
        self.seleccion: Set[Tuple[int, int]] = set()
        self.ancla: Optional[Tuple[int, int]] = None
        self._contador_series = 0
        self._contador_controles = 0
        self._colores_grupo: Dict[Tuple[str, str], str] = {}
        self._editando: Optional[str] = None

        self._crear_widgets()
        self._crear_placa()

    # ----------------------- dimensiones y coordenadas -----------------------
    def _validar_dimensiones(self) -> None:
        if self.filas < 1 or self.columnas < 1:
            raise ValueError("Filas y columnas deben ser mayores que cero.")
        if self.submatriz < 1 or self.submatriz > self.columnas:
            raise ValueError("La submatriz debe estar entre 1 y columnas.")
        if self.bloques_alineados and self.columnas % self.submatriz != 0:
            raise ValueError(
                "Con bloques alineados, columnas debe ser divisible entre submatriz."
            )

    @staticmethod
    def nombre_fila(indice: int) -> str:
        nombre = ""
        n = indice + 1
        while n:
            n, r = divmod(n - 1, 26)
            nombre = chr(65 + r) + nombre
        return nombre

    @staticmethod
    def indice_fila(nombre: str) -> int:
        nombre = nombre.strip().upper()
        valor = 0
        for ch in nombre:
            if ch not in string.ascii_uppercase:
                raise ValueError(f"Fila inválida: {nombre}")
            valor = valor * 26 + ord(ch) - 64
        return valor - 1

    def columnas_bloque(self, columna: int) -> List[int]:
        if self.bloques_alineados:
            inicio = (columna // self.submatriz) * self.submatriz
        else:
            inicio = min(columna, self.columnas - self.submatriz)
        cols = list(range(inicio, inicio + self.submatriz))
        if cols[-1] >= self.columnas:
            raise ValueError("El bloque excede los límites de la placa.")
        return cols

    def bloque_desde_celda(self, fila: int, columna: int) -> Bloque:
        return Bloque(fila=fila, columnas=self.columnas_bloque(columna))

    # ------------------------------- widgets --------------------------------
    def _crear_widgets(self) -> None:
        estilo = {"description_width": "initial"}
        self.w_filas = widgets.BoundedIntText(value=self.filas, min=1, max=100, description="Filas:", style=estilo)
        self.w_columnas = widgets.BoundedIntText(value=self.columnas, min=1, max=200, description="Columnas:", style=estilo)
        self.w_submatriz = widgets.BoundedIntText(value=self.submatriz, min=1, max=self.columnas, description="Submatriz:", style=estilo)
        self.w_alineados = widgets.Checkbox(value=self.bloques_alineados, description="Bloques alineados desde columna 1", style=estilo)
        self.btn_dimensiones = widgets.Button(description="Aplicar dimensiones", button_style="warning", icon="refresh")

        self.w_modo = widgets.ToggleButtons(
            options=[("Bloque individual", "bloque"), ("Rectángulo (dos clics)", "rectangulo")],
            value="bloque", description="Selección:", style=estilo,
        )
        self.btn_limpiar = widgets.Button(description="Limpiar selección", icon="eraser")

        self.w_tipo = widgets.ToggleButtons(options=[("Serie", "serie"), ("Control", "control")], value="serie", description="Crear:", style=estilo)
        self.w_aceite = widgets.Text(description="Aceite:", placeholder="Aceite 1", style=estilo)
        self.w_grupo = widgets.Text(description="Grupo:", placeholder="Grupo ABC", style=estilo)
        self.w_nombre = widgets.Text(description="Nombre:", placeholder="150", style=estilo)
        self.w_cantidad = widgets.Text(description="Cantidad:", placeholder="150", style=estilo)
        self.w_control = widgets.Text(description="Nombre del control:", placeholder="Control negativo", style=estilo)
        self.btn_agregar = widgets.Button(description="Agregar selección", button_style="success", icon="plus")

        self.w_elementos = widgets.Select(options=[], rows=12, description="Elementos:", style=estilo, layout=widgets.Layout(width="100%"))
        self.btn_cargar = widgets.Button(description="Editar", icon="edit")
        self.btn_guardar_edicion = widgets.Button(description="Guardar edición", button_style="info", icon="save")
        self.btn_eliminar = widgets.Button(description="Eliminar", button_style="danger", icon="trash")

        self.btn_validar = widgets.Button(description="Validar", button_style="primary", icon="check")
        self.btn_json = widgets.Button(description="Guardar JSON", icon="download")
        self.btn_python = widgets.Button(description="Guardar Python", icon="download")

        self.placa_widget: widgets.Widget = widgets.HTML("Cargando placa...")
        self.ui: Optional[widgets.VBox] = None
        self.out_estado = widgets.Output()
        self.out_preview = widgets.Output(layout=widgets.Layout(border="1px solid #ddd", max_height="380px", overflow="auto", padding="8px"))
        self.out_archivo = widgets.Output()

        self.btn_dimensiones.on_click(self._evento_dimensiones)
        self.btn_limpiar.on_click(lambda _: self.limpiar_seleccion())
        self.w_tipo.observe(self._actualizar_formulario, names="value")
        self.btn_agregar.on_click(self._evento_agregar)
        self.btn_eliminar.on_click(self._evento_eliminar)
        self.btn_cargar.on_click(self._evento_cargar)
        self.btn_guardar_edicion.on_click(self._evento_guardar_edicion)
        self.btn_validar.on_click(lambda _: self.validar(mostrar=True))
        self.btn_json.on_click(lambda _: self.guardar_json("configuracion_placa.json"))
        self.btn_python.on_click(lambda _: self.guardar_python("configuracion_placa.py"))
        self._actualizar_formulario()

    def _construir_interfaz(self) -> widgets.VBox:
        """Construye la ventana completa usando widgets persistentes."""
        return widgets.VBox([
            widgets.HTML(f"<h2>{self.titulo}</h2><p>Seleccione siempre bloques completos. No se permiten intersecciones.</p>"),
            widgets.HTML("<h3>1. Dimensiones</h3>"),
            widgets.HBox([self.w_filas, self.w_columnas, self.w_submatriz]),
            widgets.HBox([self.w_alineados, self.btn_dimensiones]),
            widgets.HTML("<h3>2. Selección de la placa</h3>"),
            widgets.HBox([self.w_modo, self.btn_limpiar]),
            self.placa_widget,
            widgets.HBox([
                widgets.VBox([
                    widgets.HTML("<h3>3. Asignación</h3>"), self.w_tipo,
                    self.w_aceite, self.w_grupo, self.w_nombre,
                    self.w_cantidad, self.w_control, self.btn_agregar,
                ], layout=widgets.Layout(width="48%")),
                widgets.VBox([
                    widgets.HTML("<h3>4. Elementos</h3>"), self.w_elementos,
                    widgets.HBox([self.btn_cargar, self.btn_guardar_edicion, self.btn_eliminar]),
                ], layout=widgets.Layout(width="48%")),
            ], layout=widgets.Layout(justify_content="space-between", align_items="flex-start")),
            widgets.HTML("<h3>5. Validación y exportación</h3>"),
            widgets.HBox([self.btn_validar, self.btn_json, self.btn_python]),
            self.out_estado,
            widgets.HTML("<h4>Vista previa de la configuración</h4>"),
            self.out_preview,
            self.out_archivo,
        ], layout=widgets.Layout(width="100%"))

    def mostrar(self) -> "PlateDesigner":
        # La placa se inserta directamente. No se renderiza dentro de Output,
        # lo que evita que Colab pierda la salida creada durante __init__.
        self.ui = self._construir_interfaz()
        display(self.ui)
        self._actualizar_preview()
        return self

    def _crear_placa(self) -> None:
        self.botones: Dict[Tuple[int, int], widgets.Button] = {}
        ancho = "42px" if self.columnas <= 16 else "34px"
        hijos: List[widgets.Widget] = [widgets.HTML("")]
        hijos += [widgets.HTML(f"<div style='text-align:center'><b>{c+1}</b></div>") for c in range(self.columnas)]
        for f in range(self.filas):
            hijos.append(widgets.HTML(f"<div style='text-align:center'><b>{self.nombre_fila(f)}</b></div>"))
            for c in range(self.columnas):
                b = widgets.Button(description="", tooltip=f"{self.nombre_fila(f)}{c+1}", layout=widgets.Layout(width=ancho, height=ancho, padding="0"))
                b.on_click(lambda _, fila=f, columna=c: self._evento_celda(fila, columna))
                self.botones[(f, c)] = b
                hijos.append(b)
        self.placa_widget = widgets.GridBox(
            children=hijos,
            layout=widgets.Layout(
                grid_template_columns="34px " + " ".join([ancho] * self.columnas),
                grid_gap="3px", overflow_x="auto", align_items="center",
                width="100%",
            ),
        )
        # Si la ventana ya está visible, sustituye únicamente la placa sin
        # reconstruir el resto de controles ni perder sus eventos.
        if self.ui is not None:
            hijos_ui = list(self.ui.children)
            hijos_ui[6] = self.placa_widget
            self.ui.children = tuple(hijos_ui)
        self._refrescar_placa()

    # ----------------------------- selección ---------------------------------
    def _evento_celda(self, fila: int, columna: int) -> None:
        if self.w_modo.value == "bloque":
            self._alternar_bloque(self.bloque_desde_celda(fila, columna))
        else:
            self._seleccionar_rectangulo(fila, columna)
        self._refrescar_placa()

    def _alternar_bloque(self, bloque: Bloque) -> None:
        if bloque.pozos.issubset(self.seleccion):
            self.seleccion.difference_update(bloque.pozos)
            return
        conflicto = bloque.pozos.intersection(self.ocupacion)
        if conflicto:
            propietario = self.ocupacion[next(iter(conflicto))]
            self._estado(f"Intersección no permitida con '{self.etiqueta(propietario)}'.", "error")
            return
        self.seleccion.update(bloque.pozos)

    def _seleccionar_rectangulo(self, fila: int, columna: int) -> None:
        if self.ancla is None:
            self.ancla = (fila, columna)
            self._estado("Primer extremo registrado; seleccione el extremo opuesto.", "info")
            return
        f0, c0 = self.ancla
        fmin, fmax = sorted((f0, fila))
        i0 = self.columnas_bloque(c0)[0]
        i1 = self.columnas_bloque(columna)[0]
        imin, imax = sorted((i0, i1))
        paso = self.submatriz if self.bloques_alineados else 1
        bloques = []
        for f in range(fmin, fmax + 1):
            for inicio in range(imin, imax + 1, paso):
                cols = list(range(inicio, inicio + self.submatriz))
                if cols[-1] < self.columnas:
                    bloques.append(Bloque(f, cols))
        pozos = set().union(*(b.pozos for b in bloques)) if bloques else set()
        conflicto = pozos.intersection(self.ocupacion)
        if conflicto:
            propietario = self.ocupacion[next(iter(conflicto))]
            self._estado(f"El rectángulo intersecta con '{self.etiqueta(propietario)}'.", "error")
        else:
            self.seleccion.update(pozos)
        self.ancla = None

    def limpiar_seleccion(self) -> None:
        self.seleccion.clear()
        self.ancla = None
        self._refrescar_placa()

    def _bloques_seleccionados(self) -> List[Bloque]:
        bloques, vistos = [], set()
        for f, c in sorted(self.seleccion):
            if (f, c) in vistos:
                continue
            b = self.bloque_desde_celda(f, c)
            if not b.pozos.issubset(self.seleccion):
                raise ValueError(f"Existe un bloque parcial en {self.nombre_fila(f)}{c+1}.")
            bloques.append(b)
            vistos.update(b.pozos)
        return bloques

    # -------------------------- creación y edición ----------------------------
    @staticmethod
    def _cantidad(texto: str) -> Any:
        texto = texto.strip()
        if not texto:
            return ""
        try:
            x = float(texto)
            return int(x) if x.is_integer() else x
        except ValueError:
            return texto

    def _evento_agregar(self, _: Any) -> None:
        try:
            bloques = self._bloques_seleccionados()
            if not bloques:
                raise ValueError("Seleccione al menos un bloque.")
            if self.w_tipo.value == "serie":
                self._crear_series(bloques)
            else:
                self._crear_controles(bloques)
            self.limpiar_seleccion()
            self._actualizar_lista()
            self._actualizar_preview()
            self._estado("Elemento(s) agregado(s).", "ok")
        except Exception as exc:
            self._estado(str(exc), "error")

    def _crear_series(self, bloques: List[Bloque]) -> None:
        aceite = self.w_aceite.value.strip()
        grupo = self.w_grupo.value.strip()
        nombre = self.w_nombre.value.strip()
        cantidad = self._cantidad(self.w_cantidad.value)
        if not aceite or not grupo or not nombre or cantidad == "":
            raise ValueError("Aceite, grupo, nombre y cantidad son obligatorios.")
        color = self._color_grupo(aceite, grupo)
        for b in bloques:
            self._contador_series += 1
            sid = f"serie_{self._contador_series}"
            nombre_final = nombre if len(bloques) == 1 else f"{nombre} {self.nombre_fila(b.fila)}{b.columnas[0]+1}"
            self._registrar(Serie(sid, nombre_final, cantidad, aceite, grupo, b, color))

    def _crear_controles(self, bloques: List[Bloque]) -> None:
        nombre = self.w_control.value.strip()
        if not nombre:
            raise ValueError("El control debe tener nombre.")
        for b in bloques:
            self._contador_controles += 1
            cid = f"control_{self._contador_controles}"
            nombre_final = nombre if len(bloques) == 1 else f"{nombre} {self.nombre_fila(b.fila)}{b.columnas[0]+1}"
            self._registrar(Control(cid, nombre_final, b))

    def _registrar(self, elemento: Serie | Control) -> None:
        if elemento.bloque.pozos.intersection(self.ocupacion):
            raise ValueError("El elemento intersecta con otro ya registrado.")
        if isinstance(elemento, Serie):
            self.series[elemento.id] = elemento
        else:
            self.controles[elemento.id] = elemento
        for pozo in elemento.bloque.pozos:
            self.ocupacion[pozo] = elemento.id

    def _evento_eliminar(self, _: Any) -> None:
        eid = self.w_elementos.value
        if not eid:
            self._estado("Seleccione un elemento.", "error")
            return
        e = self.series.get(eid) or self.controles.get(eid)
        if e:
            for p in e.bloque.pozos:
                self.ocupacion.pop(p, None)
            self.series.pop(eid, None)
            self.controles.pop(eid, None)
        self._actualizar_lista(); self._actualizar_preview(); self._refrescar_placa()
        self._estado("Elemento eliminado.", "ok")

    def _evento_cargar(self, _: Any) -> None:
        eid = self.w_elementos.value
        if not eid:
            self._estado("Seleccione un elemento.", "error")
            return
        self._editando = eid
        if eid in self.series:
            e = self.series[eid]
            self.w_tipo.value = "serie"
            self.w_aceite.value, self.w_grupo.value = e.aceite, e.grupo
            self.w_nombre.value, self.w_cantidad.value = e.nombre, str(e.cantidad)
        else:
            self.w_tipo.value = "control"
            self.w_control.value = self.controles[eid].nombre
        self._estado("Elemento cargado para edición.", "info")

    def _evento_guardar_edicion(self, _: Any) -> None:
        if not self._editando:
            self._estado("Primero cargue un elemento.", "error")
            return
        try:
            if self._editando in self.series:
                e = self.series[self._editando]
                aceite, grupo = self.w_aceite.value.strip(), self.w_grupo.value.strip()
                nombre, cantidad = self.w_nombre.value.strip(), self._cantidad(self.w_cantidad.value)
                if not aceite or not grupo or not nombre or cantidad == "":
                    raise ValueError("Aceite, grupo, nombre y cantidad son obligatorios.")
                e.aceite, e.grupo, e.nombre, e.cantidad = aceite, grupo, nombre, cantidad
                e.color = self._color_grupo(aceite, grupo)
            else:
                nombre = self.w_control.value.strip()
                if not nombre:
                    raise ValueError("El control debe tener nombre.")
                self.controles[self._editando].nombre = nombre
            self._editando = None
            self._actualizar_lista(); self._actualizar_preview(); self._refrescar_placa()
            self._estado("Edición guardada.", "ok")
        except Exception as exc:
            self._estado(str(exc), "error")

    def _color_grupo(self, aceite: str, grupo: str) -> str:
        clave = (aceite, grupo)
        if clave not in self._colores_grupo:
            self._colores_grupo[clave] = self.PALETA[len(self._colores_grupo) % len(self.PALETA)]
        return self._colores_grupo[clave]

    # --------------------------- dimensiones UI -------------------------------
    def _evento_dimensiones(self, _: Any) -> None:
        if self.series or self.controles:
            self._estado("Elimine los elementos antes de cambiar dimensiones.", "error")
            return
        try:
            self.filas = int(self.w_filas.value)
            self.columnas = int(self.w_columnas.value)
            self.submatriz = int(self.w_submatriz.value)
            self.bloques_alineados = bool(self.w_alineados.value)
            self._validar_dimensiones()
            self.w_submatriz.max = self.columnas
            self.limpiar_seleccion(); self._crear_placa(); self._actualizar_preview()
            self._estado("Dimensiones actualizadas.", "ok")
        except Exception as exc:
            self._estado(str(exc), "error")

    # ------------------------------- validación -------------------------------
    def validar(self, mostrar: bool = False) -> Tuple[bool, List[str]]:
        errores: List[str] = []
        if not self.controles:
            errores.append("Debe existir al menos un control.")
        if not self.series:
            errores.append("Debe existir al menos una serie experimental.")
        vistos: Dict[Tuple[int, int], str] = {}
        for e in list(self.series.values()) + list(self.controles.values()):
            if len(e.bloque.columnas) != self.submatriz:
                errores.append(f"'{e.nombre}' no ocupa exactamente {self.submatriz} columnas.")
            if e.bloque.columnas != list(range(e.bloque.columnas[0], e.bloque.columnas[0] + self.submatriz)):
                errores.append(f"'{e.nombre}' no usa columnas consecutivas.")
            if self.bloques_alineados and e.bloque.columnas[0] % self.submatriz != 0:
                errores.append(f"'{e.nombre}' no está alineado con la submatriz.")
            for p in e.bloque.pozos:
                if p in vistos:
                    errores.append(f"Intersección entre '{e.nombre}' y '{self.etiqueta(vistos[p])}'.")
                vistos[p] = e.id
        for s in self.series.values():
            if not s.aceite or not s.grupo or not s.nombre or s.cantidad == "":
                errores.append(f"La serie '{s.id}' tiene campos incompletos.")
        for c in self.controles.values():
            if not c.nombre:
                errores.append(f"El control '{c.id}' no tiene nombre.")
        valido = not errores
        if mostrar:
            self._estado("Experimento válido." if valido else "Errores:\n- " + "\n- ".join(errores), "ok" if valido else "error")
        return valido, errores

    # ------------------------------- exportación ------------------------------
    def obtener_configuracion(self, validar: bool = True) -> Dict[str, Any]:
        if validar:
            valido, errores = self.validar(False)
            if not valido:
                raise ValueError("Configuración inválida:\n- " + "\n- ".join(errores))

        controles = [
            {"nombre": c.nombre, "fila": self.nombre_fila(c.bloque.fila), "columnas_originales": [x + 1 for x in c.bloque.columnas]}
            for c in sorted(self.controles.values(), key=lambda x: (x.bloque.fila, x.bloque.columnas[0], x.nombre))
        ]
        agrupados: Dict[Tuple[str, str], List[Serie]] = {}
        for s in self.series.values():
            agrupados.setdefault((s.aceite, s.grupo), []).append(s)
        grupos = []
        for (aceite, grupo), series in sorted(agrupados.items()):
            grupos.append({
                "nombre": grupo,
                "aceite": aceite,
                "series": [
                    {"nombre": s.nombre, "cantidad": s.cantidad, "fila": self.nombre_fila(s.bloque.fila), "columnas_originales": [x + 1 for x in s.bloque.columnas]}
                    for s in sorted(series, key=lambda x: (x.bloque.fila, x.bloque.columnas[0], x.nombre))
                ],
            })
        return {
            "filas": self.filas,
            "columnas": self.columnas,
            "submatriz": self.submatriz,
            "control": controles[0] if controles else None,
            "controles": controles,
            "grupos": grupos,
        }

    def guardar_json(self, ruta: str | Path) -> Path:
        ruta = Path(ruta)
        ruta.write_text(json.dumps(self.obtener_configuracion(True), ensure_ascii=False, indent=4), encoding="utf-8")
        self._mostrar_archivo(ruta)
        return ruta

    def guardar_python(self, ruta: str | Path, variable: str = "configuracion") -> Path:
        ruta = Path(ruta)
        texto = json.dumps(self.obtener_configuracion(True), ensure_ascii=False, indent=4)
        texto = texto.replace(": true", ": True").replace(": false", ": False").replace(": null", ": None")
        ruta.write_text(f"# Generado por PlateDesigner\n\n{variable} = {texto}\n", encoding="utf-8")
        self._mostrar_archivo(ruta)
        return ruta

    def cargar_configuracion(self, config: Dict[str, Any]) -> None:
        self.series.clear(); self.controles.clear(); self.ocupacion.clear()
        self._contador_series = self._contador_controles = 0
        self.filas = int(config.get("filas", self.filas))
        self.columnas = int(config.get("columnas", self.columnas))
        self.submatriz = int(config["submatriz"])
        self.w_filas.value, self.w_columnas.value = self.filas, self.columnas
        self.w_submatriz.max = max(self.columnas, self.submatriz)
        self.w_submatriz.value = self.submatriz
        controles = config.get("controles")
        if controles is None:
            controles = [config["control"]] if config.get("control") else []
        for d in controles:
            self._contador_controles += 1
            b = Bloque(self.indice_fila(d["fila"]), [int(c) - 1 for c in d["columnas_originales"]])
            self._registrar(Control(f"control_{self._contador_controles}", d["nombre"], b))
        for g in config.get("grupos", []):
            color = self._color_grupo(g["aceite"], g["nombre"])
            for d in g.get("series", []):
                self._contador_series += 1
                b = Bloque(self.indice_fila(d["fila"]), [int(c) - 1 for c in d["columnas_originales"]])
                self._registrar(Serie(f"serie_{self._contador_series}", d["nombre"], d["cantidad"], g["aceite"], g["nombre"], b, color))
        self._crear_placa(); self._actualizar_lista(); self._actualizar_preview(); self.validar(True)

    # ------------------------------ interfaz auxiliar -------------------------
    def _actualizar_formulario(self, *_: Any) -> None:
        es_serie = self.w_tipo.value == "serie"
        for w in [self.w_aceite, self.w_grupo, self.w_nombre, self.w_cantidad]:
            w.layout.display = "" if es_serie else "none"
        self.w_control.layout.display = "none" if es_serie else ""

    def _actualizar_lista(self) -> None:
        opciones = []
        for c in sorted(self.controles.values(), key=lambda x: (x.bloque.fila, x.bloque.columnas[0])):
            opciones.append((f"[CONTROL] {c.nombre} — {self._texto_bloque(c.bloque)}", c.id))
        for s in sorted(self.series.values(), key=lambda x: (x.aceite, x.grupo, x.bloque.fila, x.bloque.columnas[0])):
            opciones.append((f"[SERIE] {s.aceite} / {s.grupo} / {s.nombre} ({s.cantidad}) — {self._texto_bloque(s.bloque)}", s.id))
        self.w_elementos.options = opciones
        self._refrescar_placa()

    def _texto_bloque(self, b: Bloque) -> str:
        return f"{self.nombre_fila(b.fila)}[{','.join(str(c+1) for c in b.columnas)}]"

    def etiqueta(self, eid: str) -> str:
        if eid in self.series:
            s = self.series[eid]
            return f"{s.aceite}/{s.grupo}/{s.nombre}"
        if eid in self.controles:
            return self.controles[eid].nombre
        return eid

    def _refrescar_placa(self) -> None:
        for (f, c), b in self.botones.items():
            b.style.button_color = None; b.description = ""
            b.tooltip = f"{self.nombre_fila(f)}{c+1}"
            eid = self.ocupacion.get((f, c))
            if eid in self.series:
                e = self.series[eid]; b.style.button_color = e.color
                b.tooltip += f" | {e.aceite}/{e.grupo}/{e.nombre}"
            elif eid in self.controles:
                e = self.controles[eid]; b.style.button_color = e.color
                b.tooltip += f" | Control: {e.nombre}"
            if (f, c) in self.seleccion:
                b.style.button_color = "#ffd166"; b.description = "•"

    def _actualizar_preview(self) -> None:
        with self.out_preview:
            clear_output(wait=True)
            print(json.dumps(self.obtener_configuracion(False), ensure_ascii=False, indent=4))

    def _estado(self, mensaje: str, tipo: str) -> None:
        colores = {"ok": "#1b7f3a", "error": "#b00020", "info": "#2457a6"}
        iconos = {"ok": "✓", "error": "⚠", "info": "ℹ"}
        with self.out_estado:
            clear_output(wait=True)
            display(widgets.HTML(f"<div style='color:{colores[tipo]};white-space:pre-wrap;font-weight:600'>{iconos[tipo]} {mensaje}</div>"))

    def _mostrar_archivo(self, ruta: Path) -> None:
        with self.out_archivo:
            clear_output(wait=True)
            try:
                from google.colab import files
                files.download(str(ruta))
            except Exception:
                display(widgets.HTML(f"Archivo guardado en <code>{ruta.resolve()}</code>"))


def crear_disenador_placa(
    filas: int = 8,
    columnas: int = 12,
    submatriz: int = 3,
    mostrar: bool = True,
    **kwargs: Any,
) -> PlateDesigner:
    """Crea y opcionalmente muestra el diseñador visual."""
    designer = PlateDesigner(filas, columnas, submatriz, **kwargs)
    if mostrar:
        designer.mostrar()
    return designer
