class ODPlateError(Exception):
    """Excepción base de la biblioteca."""

class ConfigurationError(ODPlateError):
    """Configuración de placa inválida."""

class ProcessingError(ODPlateError):
    """Error durante el procesamiento de matrices."""

class RankingError(ODPlateError):
    """Error al construir un ranking."""
