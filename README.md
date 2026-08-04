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
