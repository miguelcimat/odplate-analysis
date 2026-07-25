# Prueba rápida de PlateDesigner en Google Colab
from odplate import crear_disenador_placa

designer = crear_disenador_placa(
    filas=8,
    columnas=12,
    submatriz=3,
    mostrar=True,
)
