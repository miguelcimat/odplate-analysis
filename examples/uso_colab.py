from odplate import (
    ExperimentoOD,
    crear_disenador_placa,
    calificacion_inversa,
)

# 1) Crear o cargar configuración
# designer = crear_disenador_placa(filas=8, columnas=12, submatriz=3)
# configuracion = designer.obtener_configuracion()
configuracion = "configuracion_placa.json"

# 2) Cargar, corregir blanco y promediar réplicas
exp = ExperimentoOD(configuracion)
exp.cargar_resultados(
    "/content/drive/MyDrive/PlacasMedicion/E.coli_placa1",
    "Ecoli_blanco",
).procesar()

# 3) Estadísticas y modelos, sin imponer ranking
exp.calcular_todo(normalizacion="delta", ajustar_modelos=True)

# 4) Gráficas libres
exp.graficar(
    modo="grupos",
    mostrar_control=True,
    guardar_en="salida/figuras",
    mostrar=False,
)

# “Mejor” se define mediante una función explícita
exp.graficar(
    modo="mejores",
    n_mejores=5,
    criterio=calificacion_inversa,
    mostrar_control=False,
    guardar_en="salida/figuras",
    mostrar=False,
)

# También puede pedirse cualquier tramo del ranking
exp.graficar(
    modo="ranking",
    criterio=calificacion_inversa,
    rango=(6, 10),
    mostrar_control=True,
    guardar_en="salida/figuras",
    mostrar=False,
)

# Guardar un ranking completo en las tablas del reporte
exp.calcular_ranking(
    criterio=calificacion_inversa,
    guardar_como="Ranking_calificacion_inversa",
)

# 5) Reportes
salidas = exp.generar_reporte(
    "salida",
    formatos=("xlsx", "csv", "html", "docx", "pdf"),
)
print(salidas)
