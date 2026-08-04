# ODPlate

<p align="center">

# 📊 ODPlate

### Biblioteca de Python para el análisis integral de experimentos de densidad óptica (OD) en microplacas

**Diseño de placas · Procesamiento · Modelado · Visualización · Reportes**

</p>

---

# ¿Qué es ODPlate?

**ODPlate** es una biblioteca de Python desarrollada para automatizar el análisis completo de experimentos de densidad óptica (Optical Density, OD) realizados en microplacas.

Su objetivo es proporcionar un flujo de trabajo reproducible, flexible y extensible que permita al investigador concentrarse en el análisis científico de los resultados y no en tareas repetitivas de procesamiento de datos.

A diferencia de los flujos tradicionales basados en hojas de cálculo, ODPlate integra en una única plataforma todas las etapas habituales del análisis experimental:

* Diseño interactivo de placas.
* Configuración del experimento.
* Lectura automática de archivos de absorbancia.
* Corrección por blanco.
* Promediado automático de réplicas.
* Cálculo de métricas estadísticas y biológicas.
* Ajuste de modelos matemáticos.
* Generación de curvas de crecimiento.
* Estimación de parámetros experimentales.
* Comparación de tratamientos.
* Ranking de compuestos mediante criterios personalizables.
* Generación automática de figuras.
* Exportación de reportes completos.

El resultado es un entorno unificado que facilita la reproducibilidad de los experimentos y reduce significativamente el tiempo dedicado al procesamiento manual de los datos.

---

# Motivación

En numerosos laboratorios, el análisis de experimentos de densidad óptica continúa realizándose mediante una combinación de hojas de cálculo, scripts desarrollados para proyectos específicos y software con funcionalidades limitadas.

Este enfoque suele presentar diversos inconvenientes:

* Procesamiento manual de grandes cantidades de datos.
* Alto riesgo de errores durante la manipulación de las hojas de cálculo.
* Escasa reproducibilidad de los análisis.
* Dificultad para reutilizar procedimientos entre distintos experimentos.
* Falta de integración entre procesamiento, modelado y generación de reportes.
* Escasa flexibilidad para adaptar el flujo de trabajo a diferentes diseños experimentales.

ODPlate fue desarrollada para resolver estos problemas mediante una arquitectura modular que integra todas las etapas del análisis dentro de una única biblioteca.

---

# Objetivos

Los principales objetivos de ODPlate son:

* Automatizar el procesamiento de experimentos de densidad óptica.
* Facilitar la reproducibilidad de los análisis.
* Reducir el tiempo dedicado a tareas repetitivas.
* Simplificar el manejo de experimentos complejos.
* Proporcionar herramientas listas para publicaciones científicas.
* Permitir la incorporación sencilla de nuevos modelos, métricas y criterios de análisis.

---

# ¿Para quién está dirigida esta biblioteca?

ODPlate está orientada principalmente a investigadores, estudiantes y profesionales que trabajan con experimentos basados en mediciones de densidad óptica.

Entre sus posibles aplicaciones se encuentran:

* Microbiología.
* Biotecnología.
* Farmacología.
* Ciencias de alimentos.
* Productos naturales.
* Evaluación de actividad antimicrobiana.
* Estudios de crecimiento microbiano.
* Ensayos de susceptibilidad a antibióticos.
* Evaluación de compuestos bioactivos.
* Cualquier experimento cuya información se obtenga mediante microplacas de absorbancia.

Aunque fue concebida para experimentos microbiológicos, la arquitectura de la biblioteca permite adaptarla fácilmente a otros dominios experimentales.

---

# Filosofía del proyecto

ODPlate fue diseñada siguiendo cinco principios fundamentales.

## 1. Reproducibilidad

Cada resultado obtenido debe poder reproducirse utilizando exactamente la misma configuración experimental y los mismos datos de entrada.

La biblioteca evita configuraciones implícitas y registra toda la información necesaria para reconstruir un análisis completo.

---

## 2. Automatización

Las tareas repetitivas no deberían depender del investigador.

Operaciones como:

* lectura de archivos;
* organización de tratamientos;
* corrección por blanco;
* cálculo de promedios;
* generación de reportes;

son realizadas automáticamente por la biblioteca.

---

## 3. Flexibilidad

Cada laboratorio organiza sus experimentos de forma diferente.

Por esta razón, ODPlate no impone un diseño fijo de placas ni una estructura rígida para los tratamientos.

El usuario puede definir libremente:

* número de filas;
* número de columnas;
* tamaño de las submatrices;
* grupos experimentales;
* controles;
* tratamientos;
* concentraciones;
* criterios de ranking;
* modelos matemáticos.

---

## 4. Extensibilidad

La biblioteca está organizada en módulos independientes que permiten incorporar nuevas funcionalidades sin modificar el resto del sistema.

Entre las extensiones posibles se encuentran:

* nuevas métricas;
* nuevos modelos matemáticos;
* nuevos criterios de ranking;
* nuevas visualizaciones;
* nuevos formatos de reporte.

---

## 5. Claridad

ODPlate intenta representar explícitamente la estructura de un experimento.

En lugar de trabajar únicamente con matrices numéricas, la biblioteca utiliza conceptos cercanos al dominio experimental, como:

* experimento;
* placa;
* serie;
* grupo;
* tratamiento;
* control;
* submatriz.

Esto facilita tanto la lectura del código como el mantenimiento de proyectos a largo plazo.

---

# Capacidades principales

ODPlate integra un amplio conjunto de herramientas para el análisis de experimentos de densidad óptica.

Entre sus principales funcionalidades destacan:

* 🎨 Diseñador gráfico interactivo de placas.
* 📁 Lectura automática de carpetas con archivos Excel.
* ⚙️ Configuración completa del experimento mediante archivos JSON.
* 🧪 Procesamiento automático de matrices de absorbancia.
* 🧼 Corrección automática por blanco.
* 📊 Promediado de réplicas técnicas.
* 📉 Cálculo de desviaciones estándar y errores estándar.
* 📈 Extracción automática de series experimentales.
* 🧬 Ajuste de modelos de crecimiento.
* 💊 Ajuste de curvas dosis–respuesta.
* 🔬 Estimación de parámetros biológicos.
* 🏆 Sistema flexible de ranking basado en criterios personalizables.
* 📋 Exportación detallada de matrices procesadas.
* 📊 Generación de figuras listas para publicación.
* 📄 Creación automática de reportes en múltiples formatos.
* 🔌 Arquitectura extensible mediante plugins.

---

# Flujo general de trabajo

El análisis completo de un experimento en ODPlate sigue el siguiente flujo conceptual:

```text
Diseño de la placa
        │
        ▼
Configuración del experimento
        │
        ▼
Lectura de archivos de absorbancia
        │
        ▼
Procesamiento de matrices
        │
        ▼
Construcción de series experimentales
        │
        ▼
Cálculo de métricas
        │
        ▼
Ajuste de modelos matemáticos
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

Cada una de estas etapas puede ejecutarse de forma independiente o integrarse dentro de un flujo completamente automatizado mediante la clase `ExperimentoOD`.

---

# Arquitectura general

La biblioteca se organiza en módulos especializados, cada uno responsable de una etapa concreta del análisis.

```text
odplate
│
├── experiment        Gestión completa del experimento
├── designer          Diseñador interactivo de placas
├── config            Configuración y validación
├── io                Lectura de archivos
├── processing        Procesamiento de matrices
├── series            Construcción de series experimentales
├── metrics           Métricas biológicas y estadísticas
├── models            Modelos matemáticos
├── ranking           Clasificación de tratamientos
├── plotting          Generación de figuras
├── reporting         Exportación de resultados
├── plugins           Extensión de la biblioteca
├── results           Objetos de resultados
└── exceptions        Excepciones específicas
```

Esta arquitectura modular permite utilizar únicamente los componentes necesarios o construir flujos de trabajo completamente personalizados.
