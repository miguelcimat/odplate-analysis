# ODPlate

<p align="center">

# 📊 ODPlate

### Una biblioteca de Python para el análisis integral de experimentos de densidad óptica (OD) en microplacas

Diseño • Procesamiento • Modelado • Visualización • Reportes

</p>

---

## ¿Qué es ODPlate?

**ODPlate** es una biblioteca desarrollada en Python para facilitar el análisis completo de experimentos de densidad óptica (Optical Density, OD) realizados en microplacas.

La biblioteca integra en un único flujo de trabajo todas las etapas habituales del análisis experimental:

* Diseño interactivo de placas.
* Lectura automática de archivos de absorbancia.
* Organización de tratamientos y grupos experimentales.
* Corrección por blanco.
* Promediado automático de réplicas.
* Cálculo de métricas biológicas y estadísticas.
* Ajuste de modelos matemáticos.
* Estimación de parámetros de crecimiento e inhibición.
* Generación automática de gráficas.
* Creación de reportes científicos listos para su análisis o publicación.

El objetivo principal de ODPlate es eliminar la necesidad de realizar múltiples pasos manuales en hojas de cálculo y proporcionar un flujo de trabajo reproducible, automatizado y extensible.

---

# ¿Para quién está dirigida esta biblioteca?

ODPlate fue diseñada para investigadores, estudiantes y profesionales que trabajan con experimentos basados en microplacas de densidad óptica.

Entre las principales áreas de aplicación se encuentran:

* Microbiología.
* Biotecnología.
* Farmacología.
* Ciencias de alimentos.
* Biología molecular.
* Investigación de productos naturales.
* Evaluación de actividad antimicrobiana.
* Estudios de crecimiento microbiano.
* Ensayos de susceptibilidad a antibióticos.
* Cualquier experimento basado en mediciones de densidad óptica.

Aunque originalmente fue desarrollada para experimentos microbiológicos, su arquitectura modular permite utilizarla en cualquier estudio basado en matrices de absorbancia.

---

# Características principales

ODPlate proporciona un conjunto completo de herramientas para automatizar el análisis de experimentos de densidad óptica.

Entre sus principales características se encuentran:

* 🎨 Diseñador gráfico interactivo de placas.
* 📥 Lectura automática de archivos Excel.
* 🧪 Procesamiento de experimentos completos.
* 🧼 Corrección automática por blanco.
* 📊 Promediado de réplicas experimentales.
* 📈 Cálculo de desviaciones estándar y errores estándar.
* 🧬 Extracción automática de series experimentales.
* 📉 Ajuste de múltiples modelos matemáticos de crecimiento.
* 💊 Ajuste de curvas dosis–respuesta.
* 🔬 Estimación automática de MIC aparente.
* 🏆 Sistema flexible de ranking mediante criterios personalizables.
* 📋 Exportación completa de matrices procesadas.
* 📊 Generación de gráficas listas para publicación.
* 📄 Reportes automáticos en múltiples formatos.
* 🔌 Arquitectura extensible mediante plugins.

---

# ¿Qué puede hacer ODPlate?

Una vez configurado un experimento, ODPlate puede realizar automáticamente tareas como:

* Leer decenas o cientos de archivos Excel.
* Detectar automáticamente el blanco experimental.
* Promediar réplicas técnicas.
* Calcular desviaciones estándar y errores estándar.
* Extraer series de crecimiento para cada tratamiento.
* Comparar tratamientos contra controles.
* Ajustar modelos matemáticos.
* Calcular métricas biológicas.
* Clasificar tratamientos mediante criterios personalizados.
* Generar tablas listas para análisis estadístico.
* Exportar todas las matrices procesadas.
* Crear figuras con barras o bandas de error.
* Generar reportes completos en Excel, CSV, Word y HTML.

Todo ello utilizando unas pocas líneas de código y manteniendo un flujo completamente reproducible.

---

# Filosofía del proyecto

ODPlate fue desarrollada siguiendo cuatro principios fundamentales:

## Reproducibilidad

Cada resultado puede regenerarse a partir de los mismos datos y la misma configuración experimental.

## Automatización

Las tareas repetitivas deben ser realizadas por el software y no por el investigador.

## Flexibilidad

Cada laboratorio organiza sus experimentos de manera diferente. Por ello, la biblioteca permite adaptar el flujo de trabajo a distintos diseños experimentales sin modificar el código fuente.

## Extensibilidad

Nuevos modelos, métricas, criterios de ranking o métodos de visualización pueden incorporarse mediante el sistema de plugins sin alterar la arquitectura principal de la biblioteca.

---

# Flujo general de trabajo

El flujo típico de un análisis con ODPlate se resume en el siguiente diagrama:

```text
Diseño de la placa
        │
        ▼
Lectura de archivos Excel
        │
        ▼
Procesamiento de matrices
        │
        ▼
Extracción de series
        │
        ▼
Cálculo de métricas
        │
        ▼
Ajuste de modelos
        │
        ▼
Ranking de tratamientos
        │
        ▼
Generación de gráficas
        │
        ▼
Exportación de reportes
```

Cada una de estas etapas puede ejecutarse de forma independiente o integrarse dentro de un flujo completamente automatizado.


# Instalación

ODPlate puede instalarse directamente desde GitHub o utilizarse en modo de desarrollo. La biblioteca es compatible con Python **3.10 o superior**.

---

## Requisitos

Antes de instalar la biblioteca se recomienda disponer de:

* Python 3.10 o superior.
* pip actualizado.
* Git (únicamente para instalar desde el repositorio).

Puede comprobar la versión de Python mediante:

```bash
python --version
```

---

## Instalación desde GitHub

La forma más sencilla de instalar la versión estable es:

```bash
pip install git+https://github.com/miguelcimat/odplate-analysis.git
```

Este comando descargará automáticamente la versión más reciente disponible en la rama principal del repositorio.

---

## Instalación con todas las dependencias

Si se desea utilizar todas las funcionalidades de la biblioteca (diseñador gráfico, generación de reportes, lectura de Excel, etc.), se recomienda instalar el paquete completo:

```bash
pip install "git+https://github.com/miguelcimat/odplate-analysis.git#egg=odplate-analysis[all]"
```

Las dependencias adicionales incluyen, entre otras:

* ipywidgets
* openpyxl
* python-docx

---

## Instalación para desarrollo

Si se desea modificar la biblioteca o contribuir al proyecto:

```bash
git clone https://github.com/miguelcimat/odplate-analysis.git

cd odplate-analysis

pip install -e ".[all]"
```

La opción `-e` (editable) permite que cualquier modificación realizada sobre el código fuente se refleje inmediatamente sin necesidad de reinstalar la biblioteca.

---

## Instalación en Google Colab

ODPlate puede utilizarse directamente desde Google Colab.

```python
!pip install "git+https://github.com/miguelcimat/odplate-analysis.git#egg=odplate-analysis[all]"
```

Después de la instalación es recomendable reiniciar el entorno de ejecución para asegurar que todas las dependencias sean cargadas correctamente.

---

## Verificar la instalación

Una vez instalada la biblioteca:

```python
import odplate

print(odplate.__version__)
```

También es posible comprobar que la biblioteca se está importando desde la ubicación esperada:

```python
import odplate

print(odplate.__file__)
```

Esto resulta especialmente útil cuando existen múltiples instalaciones de la biblioteca en el mismo sistema.

---

## Importación recomendada

La forma recomendada de comenzar un proyecto es:

```python
from odplate import *
```

Aunque también es posible importar únicamente los componentes necesarios:

```python
from odplate import (
    ExperimentoOD,
    PlateDesigner,
    calificacion_inversa
)
```

Esta segunda opción suele ser preferible en proyectos grandes, ya que hace más explícitas las dependencias utilizadas.

---

## Estructura general del proyecto

Una vez instalada, la biblioteca organiza sus componentes principales en los siguientes módulos:

```text
odplate
│
├── experiment
├── designer
├── io
├── processing
├── series
├── metrics
├── models
├── plotting
├── reporting
├── ranking
├── plugins
└── results
```

Cada módulo está especializado en una etapa específica del análisis experimental, lo que facilita tanto el mantenimiento como la extensión de la biblioteca.


# Primer experimento (Quick Start)

El flujo completo de trabajo en ODPlate consta de cinco etapas principales:

```text
Diseñar la placa
      │
      ▼
Leer los archivos Excel
      │
      ▼
Procesar las matrices
      │
      ▼
Calcular métricas y modelos
      │
      ▼
Generar gráficas y reportes
```

Cada una de estas etapas puede ejecutarse de forma independiente, aunque normalmente se utilizan de manera secuencial.

## Paso 1. Crear el experimento

El objeto principal de la biblioteca es `ExperimentoOD`.

Puede construirse a partir de un archivo JSON generado por el diseñador de placas o directamente desde un diccionario de configuración.

### Desde un archivo JSON

```python
from odplate import ExperimentoOD

experimento = ExperimentoOD(
    "configuracion_placa.json"
)
```

### Desde un diccionario

```python
experimento = ExperimentoOD(configuracion)
```

Durante la construcción del objeto se valida automáticamente la configuración experimental.

Si se detecta alguna inconsistencia (por ejemplo, series duplicadas o dimensiones incompatibles), la biblioteca genera una excepción indicando el problema encontrado.

---

## Paso 2. Leer los archivos de absorbancia

Los archivos Excel pueden cargarse mediante:

```python
experimento.cargar_resultados(
    ruta="Experimentos/Ecoli",
    nombre_blanco="Blanco",
)
```

La biblioteca leerá automáticamente todos los archivos contenidos en la carpeta indicada.

---

## Paso 3. Procesar las matrices

```python
experimento.procesar()
```

Durante esta etapa se realizan automáticamente operaciones como:

* corrección por blanco;
* promediado de réplicas;
* cálculo de desviaciones estándar;
* cálculo del error estándar;
* organización interna de las matrices.

---

## Paso 4. Calcular métricas

```python
experimento.calcular_todo()
```

Esta función calcula todas las métricas necesarias para el análisis posterior.

---

## Paso 5. Generar las gráficas

```python
experimento.graficar()
```

Las figuras pueden mostrarse en pantalla o almacenarse automáticamente en una carpeta.

---

## Paso 6. Generar el reporte

```python
experimento.generar_reporte(
    carpeta="Resultados"
)
```

Se crearán automáticamente:

* archivos Excel;
* archivos CSV;
* reportes Word;
* reportes HTML;
* figuras;
* tablas de resultados;
* matrices procesadas.

Todo el análisis queda almacenado en una única carpeta lista para su consulta o distribución.

---

## Flujo completo

El siguiente ejemplo resume el flujo de trabajo más habitual:

```python
from odplate import *

experimento = ExperimentoOD(
    "configuracion_placa.json"
)

experimento.cargar_resultados(
    ruta="Datos",
    nombre_blanco="Blanco"
)

experimento.procesar()

experimento.calcular_todo()

experimento.graficar()

experimento.generar_reporte(
    carpeta="Resultados"
)
```

Con únicamente estas instrucciones es posible analizar un experimento completo y generar automáticamente todos los productos derivados del análisis.


