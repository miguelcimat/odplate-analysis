from __future__ import annotations

from pathlib import Path
from typing import Callable
import matplotlib.pyplot as plt

from ..series import extraer_serie, filtrar_catalogo
from ..metrics.ranking import ranking, describir_criterio


def _dibujar(
    ax,
    matrices,
    item,
    submatriz,
    tiempos,
    normalizacion,
    mostrar_banda,
    mostrar_error,
    etiqueta=None,
):
    datos = extraer_serie(
        matrices, item.como_dict(), submatriz, tiempos, normalizacion
    )
    label = etiqueta or (
        f"{item.aceite or ''} - {item.grupo or ''} - {item.nombre}".strip(' -')
    )
    linea, = ax.plot(datos["tiempo"], datos["mean"], marker="o", label=label)

    if mostrar_error == "std":
        error = datos["std"]
    elif mostrar_error == "sem":
        error = datos["sem"]
    elif mostrar_error in (None, "ninguno"):
        error = None
    else:
        raise ValueError("mostrar_error debe ser 'std', 'sem' o None.")

    if mostrar_banda and error is not None:
        ax.fill_between(
            datos["tiempo"],
            datos["mean"] - error,
            datos["mean"] + error,
            color=linea.get_color(),
            alpha=.18,
        )
    elif error is not None:
        ax.errorbar(
            datos["tiempo"],
            datos["mean"],
            yerr=error,
            fmt="none",
            ecolor=linea.get_color(),
            capsize=3,
        )


def _seleccionar_por_ranking(
    config,
    matrices,
    items,
    criterio,
    mayor_es_mejor,
    top,
    bottom,
    rango,
    submatriz,
    aceites,
    grupos,
    incluir_ids,
    excluir_ids,
    tiempos,
    criterio_kwargs,
    tipo,
):
    if criterio is None:
        raise ValueError(
            "Los modos basados en ranking requieren un criterio. "
            "Ejemplo: criterio=calificacion_inversa."
        )

    tabla = ranking(
        config=config,
        matrices=matrices,
        criterio=criterio,
        submatriz=submatriz,
        mayor_es_mejor=mayor_es_mejor,
        aceites=aceites,
        grupos=grupos,
        incluir_ids=incluir_ids,
        excluir_ids=excluir_ids,
        tiempos=tiempos,
        tipo=tipo,
        **criterio_kwargs,
    )

    if sum(x is not None for x in (top, bottom, rango)) != 1:
        raise ValueError(
            "Indique exactamente una selección de ranking: top, bottom o rango."
        )

    if top is not None:
        if int(top) <= 0:
            raise ValueError("top debe ser mayor que cero.")
        seleccion_tabla = tabla.head(int(top))
        etiqueta = f"{int(top)} mejores series"
    elif bottom is not None:
        if int(bottom) <= 0:
            raise ValueError("bottom debe ser mayor que cero.")
        seleccion_tabla = tabla.tail(int(bottom)).sort_values("posicion")
        etiqueta = f"{int(bottom)} peores series"
    else:
        if len(rango) != 2:
            raise ValueError("rango debe ser una tupla (inicio, fin).")
        inicio, fin = map(int, rango)
        if inicio < 1 or fin < inicio:
            raise ValueError("El rango debe cumplir 1 <= inicio <= fin.")
        seleccion_tabla = tabla.iloc[inicio - 1:fin]
        etiqueta = f"Series en posiciones {inicio} a {fin}"

    orden = seleccion_tabla["id"].tolist()
    indice = {item.id: item for item in items}
    seleccion = [indice[id_] for id_ in orden if id_ in indice]
    return seleccion, etiqueta, tabla


def graficar(
    config,
    matrices,
    modo="grupos",
    aceites=None,
    grupos=None,
    incluir_ids=None,
    excluir_ids=None,
    mostrar_control=True,
    tipo="tratamiento",
    controles_ids=None,
    n_mejores=None,
    criterio: Callable | None = None,
    funcion_calificacion: Callable | None = None,
    mayor_es_mejor: bool = True,
    top=None,
    bottom=None,
    rango=None,
    criterio_kwargs=None,
    normalizacion="ninguno",
    tiempos=None,
    mostrar_banda=True,
    mostrar_error="std",
    figsize=(11, 6),
    titulo=None,
    eje_y="OD corregida",
    guardar_en=None,
    mostrar=True,
):
    """
    Grafica series con selección completamente controlada por el usuario.

    Modos
    -----
    grupos:
        Una figura por grupo.
    todo:
        Todas las series filtradas en una figura.
    seleccion:
        Solo las series indicadas mediante filtros o IDs.
    ranking:
        Selecciona ``top``, ``bottom`` o ``rango`` usando ``criterio``.
    mejores:
        Alias compatible de ``ranking`` con ``top=n_mejores``.
    peores:
        Alias de ``ranking`` con ``bottom`` o ``n_mejores``.

    No existe un criterio predeterminado: el usuario debe declarar qué
    significa "mejor" o "peor".
    """
    submatriz = config["submatriz"]
    items = filtrar_catalogo(
        config, aceites, grupos, incluir_ids, excluir_ids, None, tipo=tipo
    )
    controles = filtrar_catalogo(config, incluir_controles=True, tipo="control")
    controles = [
        x for x in controles
        if x.es_control
        and (not controles_ids or x.id in set(controles_ids))
    ]

    # Alias anterior conservado para no romper notebooks, sin imponer default.
    if criterio is not None and funcion_calificacion is not None:
        if criterio is not funcion_calificacion:
            raise ValueError(
                "Use solo 'criterio' o 'funcion_calificacion', no ambos."
            )
    criterio = criterio or funcion_calificacion
    criterio_kwargs = dict(criterio_kwargs or {})

    tabla_ranking = None
    if modo in {"mejores", "peores", "ranking"}:
        if modo == "mejores":
            top = n_mejores if top is None else top
            if top is None:
                raise ValueError(
                    "En modo='mejores' indique n_mejores o top."
                )
            bottom = rango = None
        elif modo == "peores":
            bottom = n_mejores if bottom is None else bottom
            if bottom is None:
                raise ValueError(
                    "En modo='peores' indique n_mejores o bottom."
                )
            top = rango = None

        seleccion, nombre, tabla_ranking = _seleccionar_por_ranking(
            config=config,
            matrices=matrices,
            items=items,
            criterio=criterio,
            mayor_es_mejor=mayor_es_mejor,
            top=top,
            bottom=bottom,
            rango=rango,
            submatriz=submatriz,
            aceites=aceites,
            grupos=grupos,
            incluir_ids=incluir_ids,
            excluir_ids=excluir_ids,
            tiempos=tiempos,
            criterio_kwargs=criterio_kwargs,
            tipo=tipo,
        )
        conjuntos = [(titulo or nombre, seleccion)]
    elif modo == "todo":
        conjuntos = [(titulo or "Todas las series", items)]
    elif modo == "seleccion":
        conjuntos = [(titulo or "Series seleccionadas", items)]
    elif modo == "grupos":
        claves = []
        for item in items:
            clave = (item.aceite, item.grupo)
            if clave not in claves:
                claves.append(clave)
        conjuntos = [
            (
                f"{aceite} - {grupo}",
                [x for x in items if (x.aceite, x.grupo) == (aceite, grupo)],
            )
            for aceite, grupo in claves
        ]
    else:
        raise ValueError(
            "modo debe ser 'grupos', 'todo', 'seleccion', 'ranking', "
            "'mejores' o 'peores'."
        )

    rutas = []
    figuras = []
    for nombre, seleccion in conjuntos:
        fig, ax = plt.subplots(figsize=figsize)
        if mostrar_control:
            for control in controles:
                _dibujar(
                    ax, matrices, control, submatriz, tiempos,
                    normalizacion, mostrar_banda, mostrar_error,
                    control.nombre,
                )
        for item in seleccion:
            _dibujar(
                ax, matrices, item, submatriz, tiempos,
                normalizacion, mostrar_banda, mostrar_error,
            )

        ax.set(title=nombre, xlabel="Tiempo", ylabel=eje_y)
        ax.grid(alpha=.25)
        if seleccion or (mostrar_control and controles):
            ax.legend()
        fig.tight_layout()
        figuras.append(fig)

        if guardar_en:
            carpeta = Path(guardar_en)
            carpeta.mkdir(parents=True, exist_ok=True)
            nombre_archivo = nombre.replace("/", "-").replace(" ", "_") + ".png"
            ruta = carpeta / nombre_archivo
            fig.savefig(ruta, dpi=200, bbox_inches="tight")
            rutas.append(ruta)
        if mostrar:
            plt.show()
        else:
            plt.close(fig)

    metadatos = None
    if criterio is not None:
        metadatos = describir_criterio(
            criterio, mayor_es_mejor
        ).como_dict()
        metadatos["parametros"] = criterio_kwargs

    return {
        "figuras": figuras,
        "rutas": rutas,
        "ranking": tabla_ranking,
        "criterio": metadatos,
    }
