from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import Any, Iterable
import numpy as np

from .processing import normalizar_vector


@dataclass(frozen=True)
class Serie:
    """Unidad experimental única: tratamiento, control o referencia."""

    id: str
    nombre: str
    tipo: str = "tratamiento"
    fila: str = ""
    columnas_originales: tuple[int, ...] = field(default_factory=tuple)
    grupo: str | None = None
    aceite: str | None = None
    concentracion: Any = None
    metadatos: dict[str, Any] = field(default_factory=dict, compare=False)

    @classmethod
    def desde_dict(cls, data: dict[str, Any], *, defaults: dict[str, Any] | None = None) -> "Serie":
        d = dict(defaults or {}) | dict(data)
        columnas = tuple(int(x) for x in d.get("columnas_originales", d.get("columnas", ())))
        conocidos = {
            "id", "nombre", "tipo", "fila", "columnas_originales", "columnas",
            "grupo", "aceite", "concentracion", "cantidad", "metadatos",
        }
        meta = dict(d.get("metadatos") or {})
        meta.update({k: v for k, v in d.items() if k not in conocidos})
        concentracion = d.get("concentracion", d.get("cantidad"))
        return cls(
            id=str(d["id"]),
            nombre=str(d.get("nombre", d["id"])),
            tipo=str(d.get("tipo", "tratamiento")).strip().lower(),
            fila=str(d.get("fila", "")).strip().upper(),
            columnas_originales=columnas,
            grupo=d.get("grupo"),
            aceite=d.get("aceite"),
            concentracion=concentracion,
            metadatos=meta,
        )

    def como_dict(self) -> dict[str, Any]:
        d = asdict(self)
        d["columnas_originales"] = list(self.columnas_originales)
        return d

    @property
    def es_control(self) -> bool:
        return self.tipo.startswith("control")


@dataclass(frozen=True)
class Grupo:
    nombre: str
    ids: tuple[str, ...] = field(default_factory=tuple)
    aceite: str | None = None
    metadatos: dict[str, Any] = field(default_factory=dict, compare=False)


def indice_fila(fila):
    if isinstance(fila, int):
        return fila
    s = str(fila).strip().upper()
    n = 0
    for ch in s:
        n = n * 26 + ord(ch) - 64
    return n - 1


def indice_columna(columnas_originales, submatriz: int):
    cols = sorted(map(int, columnas_originales))
    if (
        len(cols) != submatriz
        or cols != list(range(cols[0], cols[0] + submatriz))
        or (cols[0] - 1) % submatriz
    ):
        raise ValueError(f"Bloque inválido: {cols}")
    return (cols[0] - 1) // submatriz


def tiempos_disponibles(matrices):
    return sorted(k for k in matrices if isinstance(k, (int, float, np.integer, np.floating)))


def extraer_serie(matrices, serie, submatriz: int, tiempos=None, normalizacion="ninguno"):
    if isinstance(serie, Serie):
        serie_dict = serie.como_dict()
    else:
        serie_dict = serie
    tiempos = np.asarray(tiempos if tiempos is not None else tiempos_disponibles(matrices), float)
    f = indice_fila(serie_dict["fila"])
    c = indice_columna(serie_dict["columnas_originales"], submatriz)
    medias, std, sem, ns = [], [], [], []
    for t in tiempos:
        key = int(t) if int(t) == t and int(t) in matrices else t
        d = matrices[key]
        medias.append(d["mean"][f, c])
        std.append(d["std"][f, c])
        sem.append(d.get("sem", np.zeros_like(d["std"]))[f, c])
        ns.append(d.get("n", np.ones_like(d["std"]))[f, c])
    y = normalizar_vector(medias, normalizacion)
    return {
        "tiempo": tiempos,
        "mean": y,
        "std": np.asarray(std, float),
        "sem": np.asarray(sem, float),
        "n": np.asarray(ns, float),
        "serie": serie,
    }


def catalogo_series(config) -> list[Serie]:
    """Devuelve un catálogo único de series, incluidos los controles."""
    return [Serie.desde_dict(x) for x in config.get("series", [])]


def filtrar_catalogo(
    config,
    aceites=None,
    grupos=None,
    incluir_ids=None,
    excluir_ids=None,
    incluir_controles=None,
    tipo="tratamiento",
):
    """Filtra el catálogo unificado.

    ``tipo`` acepta ``tratamiento``, ``control``, ``todos`` o cualquier tipo
    personalizado almacenado en la configuración. ``incluir_controles`` se
    conserva como alias compatible y, cuando se proporciona, prevalece sobre
    el valor predeterminado de ``tipo``.
    """
    if incluir_controles is True and tipo == "tratamiento":
        tipo = "todos"
    elif incluir_controles is False and tipo == "todos":
        tipo = "tratamiento"

    aceites = set(aceites) if aceites else None
    grupos = set(grupos) if grupos else None
    inc = set(incluir_ids) if incluir_ids else None
    exc = set(excluir_ids or [])
    tipos = None if tipo in (None, "todos") else ({tipo} if isinstance(tipo, str) else set(tipo))

    out: list[Serie] = []
    for serie in catalogo_series(config):
        if tipos and serie.tipo not in tipos:
            continue
        if aceites and serie.aceite not in aceites:
            continue
        if grupos and serie.grupo not in grupos:
            continue
        if inc is not None and serie.id not in inc:
            continue
        if serie.id in exc:
            continue
        out.append(serie)
    return out
