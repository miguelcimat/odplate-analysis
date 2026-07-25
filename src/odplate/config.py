from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import Any, Dict, List

from .exceptions import ConfigurationError


def _slug(*parts: Any) -> str:
    text = "::".join(str(p).strip() for p in parts if p not in (None, ""))
    return text or "serie"


def normalizar_configuracion(config: Dict[str, Any]) -> Dict[str, Any]:
    """Convierte configuraciones antiguas al catálogo único de ``series``."""
    cfg = copy.deepcopy(config)
    if cfg.get("series"):
        series = []
        for i, s in enumerate(cfg["series"]):
            x = dict(s)
            x.setdefault("id", _slug(x.get("tipo", "serie"), x.get("nombre", i), i))
            x.setdefault("tipo", "tratamiento")
            if "concentracion" not in x and "cantidad" in x:
                x["concentracion"] = x.get("cantidad")
            series.append(x)
        cfg["series"] = series
        cfg.setdefault("grupos_catalogo", _grupos_desde_series(series))
        return cfg

    series = []
    controles_vistos = set()
    cs = cfg.get("controles")
    if cs is None and cfg.get("control"):
        cs = [cfg["control"]]
    for i, c in enumerate(cs or []):
        x = dict(c)
        x.setdefault("id", _slug("control", x.get("nombre", i), i))
        x.setdefault("nombre", f"Control {i + 1}")
        x.setdefault("tipo", x.get("subtipo", "control"))
        x.setdefault("grupo", "Controles")
        x.setdefault("aceite", None)
        key = (x.get("fila"), tuple(x.get("columnas_originales", [])))
        if key not in controles_vistos:
            series.append(x)
            controles_vistos.add(key)

    grupos_catalogo = []
    for gi, grupo in enumerate(cfg.get("grupos", [])):
        ids = []
        for si, serie in enumerate(grupo.get("series", [])):
            x = dict(serie)
            x.setdefault("id", _slug(grupo.get("aceite"), grupo.get("nombre"), x.get("nombre", si), si))
            x.setdefault("nombre", f"Serie {si + 1}")
            x.setdefault("tipo", "tratamiento")
            x.setdefault("grupo", grupo.get("nombre"))
            x.setdefault("aceite", grupo.get("aceite"))
            if "concentracion" not in x and "cantidad" in x:
                x["concentracion"] = x.get("cantidad")
            ids.append(x["id"])
            series.append(x)
        grupos_catalogo.append({
            "nombre": grupo.get("nombre", f"Grupo {gi + 1}"),
            "aceite": grupo.get("aceite"),
            "ids": ids,
        })

    cfg["series"] = series
    cfg["grupos_catalogo"] = grupos_catalogo
    return cfg


def _grupos_desde_series(series: list[dict[str, Any]]) -> list[dict[str, Any]]:
    agrupados: dict[tuple[Any, Any], list[str]] = {}
    for s in series:
        if s.get("grupo"):
            agrupados.setdefault((s.get("grupo"), s.get("aceite")), []).append(str(s["id"]))
    return [
        {"nombre": nombre, "aceite": aceite, "ids": ids}
        for (nombre, aceite), ids in agrupados.items()
    ]


def cargar_configuracion(origen: str | Path | Dict[str, Any]) -> Dict[str, Any]:
    if isinstance(origen, dict):
        config = origen
    else:
        ruta = Path(origen)
        if ruta.suffix.lower() == ".json":
            config = json.loads(ruta.read_text(encoding="utf-8"))
        elif ruta.suffix.lower() == ".py":
            espacio: Dict[str, Any] = {}
            exec(ruta.read_text(encoding="utf-8"), espacio)
            config = espacio.get("configuracion")
            if not isinstance(config, dict):
                raise ConfigurationError("El archivo Python debe definir 'configuracion'.")
        else:
            raise ConfigurationError("La configuración debe ser dict, JSON o Python.")
    config = normalizar_configuracion(config)
    validar_configuracion(config)
    return config


def guardar_configuracion(config: Dict[str, Any], ruta: str | Path) -> Path:
    config = normalizar_configuracion(config)
    validar_configuracion(config)
    ruta = Path(ruta)
    ruta.parent.mkdir(parents=True, exist_ok=True)
    if ruta.suffix.lower() == ".json":
        ruta.write_text(json.dumps(config, ensure_ascii=False, indent=4), encoding="utf-8")
    elif ruta.suffix.lower() == ".py":
        ruta.write_text("configuracion = " + repr(config) + "\n", encoding="utf-8")
    else:
        raise ConfigurationError("Use extensión .json o .py")
    return ruta


def controles(config: Dict[str, Any]) -> List[Dict[str, Any]]:
    return [s for s in config.get("series", []) if str(s.get("tipo", "")).startswith("control")]


def iterar_series(config: Dict[str, Any]):
    for s in config.get("series", []):
        if str(s.get("tipo", "tratamiento")) == "tratamiento":
            grupo = {"nombre": s.get("grupo"), "aceite": s.get("aceite")}
            yield grupo, s


def clave_serie(grupo: Dict[str, Any], serie: Dict[str, Any]) -> str:
    return str(serie.get("id") or _slug(grupo.get("aceite"), grupo.get("nombre"), serie.get("nombre")))


def validar_configuracion(config: Dict[str, Any]) -> None:
    if not isinstance(config, dict):
        raise ConfigurationError("La configuración debe ser un diccionario.")
    sub = int(config.get("submatriz", 0))
    if sub < 1:
        raise ConfigurationError("submatriz debe ser mayor que cero.")
    filas = int(config.get("filas", 8))
    columnas = int(config.get("columnas", 12))
    series = config.get("series", [])
    if not series:
        raise ConfigurationError("Debe existir al menos una serie.")
    if not any(str(s.get("tipo", "")).startswith("control") for s in series):
        raise ConfigurationError("Debe existir al menos un control.")

    ids, ocupados = set(), {}
    tipos_validos = {"tratamiento", "control", "control_positivo", "control_negativo", "referencia", "blanco"}
    for s in series:
        sid = str(s.get("id", "")).strip()
        if not sid:
            raise ConfigurationError("Todas las series deben tener id.")
        if sid in ids:
            raise ConfigurationError(f"ID duplicado: {sid}.")
        ids.add(sid)
        tipo = str(s.get("tipo", "tratamiento")).strip().lower()
        if not tipo:
            raise ConfigurationError(f"{sid}: falta tipo.")
        # Se permiten tipos personalizados, pero deben ser identificadores simples.
        if not tipo.replace("_", "").replace("-", "").isalnum():
            raise ConfigurationError(f"{sid}: tipo inválido '{tipo}'.")
        fila = str(s.get("fila", "")).strip().upper()
        cols = sorted(int(x) for x in s.get("columnas_originales", []))
        if not fila:
            raise ConfigurationError(f"{sid}: falta fila.")
        fila_idx = 0
        for ch in fila:
            fila_idx = fila_idx * 26 + ord(ch) - 64
        if fila_idx < 1 or fila_idx > filas:
            raise ConfigurationError(f"{sid}: fila {fila} fuera de rango.")
        if len(cols) != sub:
            raise ConfigurationError(f"{sid}: debe usar exactamente {sub} columnas.")
        if cols != list(range(cols[0], cols[0] + sub)):
            raise ConfigurationError(f"{sid}: columnas no consecutivas.")
        if (cols[0] - 1) % sub != 0:
            raise ConfigurationError(f"{sid}: bloque no alineado con submatriz.")
        if min(cols) < 1 or max(cols) > columnas:
            raise ConfigurationError(f"{sid}: columnas fuera de rango.")
        for col in cols:
            pozo = (fila, col)
            if pozo in ocupados:
                raise ConfigurationError(f"Intersección entre {sid} y {ocupados[pozo]} en {fila}{col}.")
            ocupados[pozo] = sid
