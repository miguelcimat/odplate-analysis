# ODPlate Analysis 0.3.0

Biblioteca extensible para procesamiento, análisis, ranking, visualización y reporte de experimentos de densidad óptica en microplacas.

## Instalación en Google Colab

```python
!unzip -q odplate_analysis.zip -d /content/odplate_analysis
!pip install -e "/content/odplate_analysis[all]"

from odplate import ExperimentoOD, calificacion_inversa
```

No es necesario modificar `sys.path`.

## Ranking explícito

```python
exp.graficar(
    modo="mejores",
    n_mejores=5,
    criterio=calificacion_inversa,
    mostrar_control=True,
)
```

También puede usarse el nombre registrado:

```python
exp.calcular_ranking(criterio="calificacion_inversa", n=5)
```

## Plugins

```python
from odplate import registrar_criterio

@registrar_criterio(name="mi_criterio")
def mi_criterio(matrices, serie, submatriz, tiempos=None):
    return 0.0
```

Después puede utilizarse con `criterio="mi_criterio"`.

## Estructura

El código fuente usa el formato estándar `src/odplate/`, con subpaquetes para entrada/salida, procesamiento, métricas, modelos, gráficas, reportes, plugins y utilidades. Los imports históricos como `from odplate.processing import procesar_matrices` siguen funcionando.

## Catálogo único de series (1.0)

Los controles, tratamientos y referencias se almacenan en `configuracion["series"]`.
Las configuraciones 0.x con `control`, `controles` y `grupos` se convierten automáticamente.

```python
ranking = experimento.calcular_ranking(
    criterio="calificacion_inversa",
    tipo="todos",              # tratamiento, control, todos o tipo personalizado
)
```

```python
experimento.graficar(
    modo="ranking",
    criterio="calificacion_inversa",
    top=5,
    tipo="todos",
    mostrar_control=False,      # evita dibujar el control dos veces si ya está en el ranking
)
```

El núcleo general está disponible como `Experimento`; `ExperimentoOD` se conserva como interfaz compatible.
