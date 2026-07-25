from .core import *
from .ranking import ranking, describir_criterio, DescripcionCriterio
from .statistics import *

from ..plugins import ranking_registry
try:
    ranking_registry.register(calificacion_inversa, name='calificacion_inversa')
except ValueError:
    pass
