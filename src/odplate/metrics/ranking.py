from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Callable, Optional, Any
import inspect
import pandas as pd

from ..series import filtrar_catalogo, Serie
from ..plugins import ranking_registry


@dataclass(frozen=True)
class DescripcionCriterio:
    nombre: str
    descripcion: str
    modulo: str
    mayor_es_mejor: bool
    formula: Optional[str] = None

    def como_dict(self) -> dict[str, Any]:
        return asdict(self)


def describir_criterio(criterio: Callable | str, mayor_es_mejor: bool = True) -> DescripcionCriterio:
    if isinstance(criterio, str):
        criterio = ranking_registry.get(criterio)
    if not callable(criterio):
        raise TypeError("El criterio debe ser una función invocable o el nombre de un criterio registrado.")
    return DescripcionCriterio(
        nombre=getattr(criterio, "__name__", criterio.__class__.__name__),
        descripcion=inspect.getdoc(criterio) or "Sin descripción proporcionada.",
        modulo=getattr(criterio, "__module__", "desconocido"),
        mayor_es_mejor=bool(mayor_es_mejor),
        formula=getattr(criterio, "formula", None),
    )


def ranking(
    config,
    matrices,
    criterio: Callable | str,
    submatriz=None,
    n=None,
    mayor_es_mejor: bool = True,
    aceites=None,
    grupos=None,
    incluir_ids=None,
    excluir_ids=None,
    tipo="tratamiento",
    incluir_controles=None,
    **kwargs,
):
    """Ordena series mediante un criterio explícito y permite incluir controles."""
    if isinstance(criterio, str):
        criterio = ranking_registry.get(criterio)
    if not callable(criterio):
        raise TypeError("Debe proporcionar un criterio invocable o registrado.")
    if n is not None and int(n) <= 0:
        raise ValueError("n debe ser mayor que cero.")

    submatriz = submatriz or config["submatriz"]
    filas = []
    for serie in filtrar_catalogo(
        config,
        aceites=aceites,
        grupos=grupos,
        incluir_ids=incluir_ids,
        excluir_ids=excluir_ids,
        incluir_controles=incluir_controles,
        tipo=tipo,
    ):
        valor = criterio(
            matrices=matrices,
            serie=serie.como_dict(),
            submatriz=submatriz,
            **kwargs,
        )
        filas.append({
            "id": serie.id,
            "nombre": serie.nombre,
            "tipo": serie.tipo,
            "grupo": serie.grupo,
            "aceite": serie.aceite,
            "concentracion": serie.concentracion,
            "calificacion": valor,
        })

    columnas = ["posicion", "id", "nombre", "tipo", "grupo", "aceite", "concentracion", "calificacion"]
    if not filas:
        resultado = pd.DataFrame(columns=columnas)
    else:
        resultado = pd.DataFrame(filas).sort_values(
            "calificacion", ascending=not mayor_es_mejor, na_position="last"
        ).reset_index(drop=True)
        resultado.insert(0, "posicion", range(1, len(resultado) + 1))
        if n is not None:
            resultado = resultado.head(int(n)).copy()

    resultado.attrs["criterio"] = describir_criterio(criterio, mayor_es_mejor).como_dict()
    resultado.attrs["tipo"] = tipo
    return resultado
