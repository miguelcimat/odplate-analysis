from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
import pandas as pd

@dataclass
class ResultadosProcesamiento:
    crudas: dict[Any, Any] | None = None
    matrices: dict[Any, Any] | None = None

@dataclass
class ResultadosMetricas:
    tablas: dict[str, pd.DataFrame] = field(default_factory=dict)

@dataclass
class ResultadosModelos:
    ajustes: pd.DataFrame = field(default_factory=pd.DataFrame)

@dataclass
class ResultadoRanking:
    tabla: pd.DataFrame
    criterio: dict[str, Any]

@dataclass
class ResultadoGrafica:
    figuras: list[Any] = field(default_factory=list)
    rutas: list[Path] = field(default_factory=list)
