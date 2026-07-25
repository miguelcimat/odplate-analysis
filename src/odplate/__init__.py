from .experiment import Experimento, ExperimentoOD
from .config import cargar_configuracion, guardar_configuracion, validar_configuracion
from .io import leer_matriz_absorbancia, leer_carpeta_cruda
from .processing import procesar_matrices, promediar_submatrices, normalizar_vector
from .series import Serie, Grupo, extraer_serie, catalogo_series, filtrar_catalogo
from .metrics import metricas_serie, calificacion_inversa, metricas_frente_control
from .models import ajustar_modelo, seleccionar_mejor_modelo, ajustar_ic, mic_aparente
from .metrics.ranking import ranking, describir_criterio, DescripcionCriterio
from .plotting import graficar
from .plugins import registrar_metrica, registrar_modelo, registrar_grafica, registrar_criterio
from .results import ResultadosProcesamiento, ResultadosMetricas, ResultadosModelos, ResultadoRanking
try:
    from .designer import PlateDesigner, crear_disenador_placa
except Exception:
    PlateDesigner = crear_disenador_placa = None

__version__ = '1.0.3'
__all__ = [name for name in globals() if not name.startswith('_')]
