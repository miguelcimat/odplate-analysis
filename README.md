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

# Instalación

ODPlate está desarrollada para Python y puede utilizarse tanto en computadoras personales como en servidores, estaciones de trabajo o entornos en la nube como Google Colab.

Actualmente la biblioteca es compatible con **Python 3.10 o superior**.

---

# Requisitos

Antes de instalar ODPlate se recomienda verificar que Python y `pip` estén correctamente instalados.

Puede comprobar la versión de Python mediante:

```bash
python --version
```

o

```bash
python3 --version
```

La salida debe indicar una versión igual o superior a **3.10**.

También es recomendable actualizar `pip` antes de la instalación:

```bash
pip install --upgrade pip
```

---

# Instalación desde GitHub

La forma recomendada de instalar la biblioteca consiste en utilizar directamente el repositorio oficial.

```bash
pip install "git+https://github.com/miguelcimat/odplate-analysis.git#egg=odplate-analysis[all]"
```

Esta opción instala tanto la biblioteca como todas las dependencias necesarias para utilizar la totalidad de sus funcionalidades.

---

# Instalación para desarrollo

Si desea modificar el código fuente o contribuir al desarrollo del proyecto, puede clonar el repositorio e instalar la biblioteca en modo editable.

```bash
git clone https://github.com/miguelcimat/odplate-analysis.git

cd odplate-analysis

pip install -e ".[all]"
```

La instalación editable (`-e`) permite que cualquier modificación realizada en el código fuente se refleje inmediatamente sin necesidad de reinstalar la biblioteca.

Esta modalidad resulta especialmente útil durante el desarrollo de nuevos modelos, métricas, plugins o funcionalidades.

---

# Instalación en Google Colab

ODPlate puede utilizarse directamente desde Google Colab.

```python
!pip install "git+https://github.com/miguelcimat/odplate-analysis.git#egg=odplate-analysis[all]"
```

Una vez finalizada la instalación, se recomienda **reiniciar el entorno de ejecución** antes de importar la biblioteca.

Esto garantiza que todas las dependencias se carguen correctamente.

---

# Verificar la instalación

Después de instalar ODPlate, puede comprobar que la biblioteca se encuentra disponible ejecutando:

```python
import odplate

print(odplate.__version__)
```

También es posible conocer desde dónde está siendo importada la biblioteca:

```python
import odplate

print(odplate.__file__)
```

Esta información resulta especialmente útil cuando existen varias instalaciones de la biblioteca en el mismo sistema.

---

# Importación de la biblioteca

La forma más sencilla de comenzar consiste en importar todos los componentes públicos:

```python
from odplate import *
```

Sin embargo, en proyectos grandes suele ser recomendable importar únicamente los componentes necesarios.

Por ejemplo:

```python
from odplate import (
    ExperimentoOD,
    PlateDesigner,
    calificacion_inversa
)
```

Esta estrategia hace que el código sea más legible y facilita identificar las dependencias utilizadas por cada proyecto.

---

# Dependencias principales

ODPlate utiliza varias bibliotecas ampliamente reconocidas dentro del ecosistema científico de Python.

Entre las más importantes se encuentran:

| Biblioteca  | Propósito                                  |
| ----------- | ------------------------------------------ |
| NumPy       | Operaciones matriciales y cálculo numérico |
| Pandas      | Manipulación de tablas de datos            |
| SciPy       | Métodos estadísticos y optimización        |
| Matplotlib  | Generación de figuras                      |
| OpenPyXL    | Lectura y escritura de archivos Excel      |
| Python-docx | Generación automática de reportes Word     |
| ipywidgets  | Diseñador interactivo de placas            |

Estas dependencias son instaladas automáticamente cuando se utiliza la opción `[all]`.

---

# Organización del proyecto

Después de instalar la biblioteca, la estructura principal del paquete es la siguiente:

```text
odplate/
│
├── experiment.py
├── designer.py
├── config.py
├── exceptions.py
├── ranking.py
├── results.py
├── series.py
├── statistics.py
│
├── io/
├── processing/
├── metrics/
├── models/
├── plotting/
├── reporting/
└── plugins/
```

Cada módulo se especializa en una etapa concreta del análisis experimental.

La comunicación entre estos módulos se realiza principalmente mediante la clase `ExperimentoOD`, que constituye el punto de entrada principal de la biblioteca.

---

# Primera prueba

Una vez instalada la biblioteca, puede comprobar que todo funciona correctamente ejecutando el siguiente código:

```python
from odplate import ExperimentoOD

print("ODPlate se instaló correctamente.")
```

Si la instalación fue exitosa, el código finalizará sin errores.

---

# Flujo de trabajo general

Aunque cada módulo puede utilizarse de forma independiente, el flujo de trabajo recomendado es el siguiente:

```text
Diseñar la placa
        │
        ▼
Guardar la configuración
        │
        ▼
Crear el experimento
        │
        ▼
Leer los archivos Excel
        │
        ▼
Procesar las matrices
        │
        ▼
Calcular métricas
        │
        ▼
Ajustar modelos
        │
        ▼
Generar gráficas
        │
        ▼
Exportar reportes
```

En las siguientes secciones se describirá detalladamente cada una de estas etapas.

---

# Convenciones utilizadas en esta documentación

A lo largo del manual se utilizarán las siguientes convenciones.

### Código Python

Todos los ejemplos de código estarán escritos en Python.

```python
experimento.procesar()
```

### Parámetros opcionales

Los parámetros que aparecen con un valor por defecto son opcionales.

Por ejemplo:

```python
experimento.procesar(
    restar_blanco=True,
    ddof=1
)
```

indica que ambos parámetros pueden omitirse.

### Rutas de archivos

Las rutas mostradas en los ejemplos son únicamente ilustrativas.

Cada usuario deberá sustituirlas por la ubicación correspondiente de sus propios datos experimentales.

### Configuración experimental

Siempre que se haga referencia a una **configuración**, se estará hablando del archivo JSON generado por el diseñador de placas, el cual describe completamente la organización del experimento y constituye la base para todo el procesamiento posterior.

# Conceptos fundamentales de ODPlate

Antes de comenzar a utilizar la biblioteca es importante comprender cómo representa ODPlate un experimento de densidad óptica.

A diferencia de otras herramientas que trabajan únicamente con matrices numéricas, ODPlate modela explícitamente los diferentes elementos que forman parte de un experimento. Esto permite que el código sea más claro, más reproducible y más cercano al lenguaje utilizado habitualmente en el laboratorio.

En esta sección se presentan los conceptos fundamentales sobre los que se construye toda la biblioteca.

---

# Experimento

El **experimento** constituye la unidad principal de trabajo dentro de ODPlate.

Un experimento contiene toda la información necesaria para reproducir un análisis completo, incluyendo:

* configuración de la placa;
* tratamientos;
* controles;
* grupos experimentales;
* archivos de absorbancia;
* matrices procesadas;
* métricas calculadas;
* modelos ajustados;
* gráficas;
* reportes generados.

En la práctica, casi todas las operaciones de la biblioteca se realizan a través de un objeto `ExperimentoOD`.

```python
from odplate import ExperimentoOD

experimento = ExperimentoOD(
    "configuracion.json"
)
```

Una vez creado, el experimento actúa como el administrador de todas las etapas del análisis.

---

# Placa

Una **placa** representa la organización física del experimento.

Cada placa está formada por un conjunto de pozos distribuidos en filas y columnas.

Por ejemplo, una placa de 96 pozos posee:

* 8 filas
* 12 columnas

ODPlate permite trabajar con placas de diferentes dimensiones, siempre que puedan dividirse en bloques compatibles con el tamaño de submatriz definido por el usuario.

La organización de la placa se define mediante el diseñador gráfico o mediante un archivo de configuración.

---

# Submatriz

Uno de los conceptos más importantes de ODPlate es la **submatriz**.

Una submatriz corresponde al conjunto de réplicas técnicas asociadas a una misma condición experimental.

Por ejemplo, si una placa de 8×12 utiliza tres columnas para cada tratamiento:

```text
A1 A2 A3
```

las tres mediciones pertenecen a una misma submatriz.

Durante el procesamiento, ODPlate calcula automáticamente:

* promedio;
* desviación estándar;
* error estándar;
* número de réplicas.

Si la placa original es de:

```text
8 × 12
```

y el tamaño de submatriz es:

```text
3
```

la matriz procesada tendrá dimensiones:

```text
8 × 4
```

porque cada grupo de tres columnas será reemplazado por un único valor promedio.

Este mecanismo elimina la necesidad de realizar manualmente el cálculo de promedios y medidas de dispersión.

---

# Tratamiento

Un **tratamiento** representa cualquier condición experimental cuya respuesta se desea evaluar.

Algunos ejemplos son:

* un aceite esencial;
* un antibiótico;
* un extracto vegetal;
* un compuesto químico;
* una concentración específica.

Cada tratamiento queda asociado a una posición concreta dentro de la placa.

---

# Control

Un **control** corresponde a una condición de referencia utilizada para comparar el comportamiento de los tratamientos.

ODPlate distingue explícitamente los controles del resto de los tratamientos.

Esto permite, entre otras cosas:

* mostrarlos automáticamente en las gráficas;
* utilizarlos como referencia para calcular métricas;
* excluirlos de los rankings cuando sea necesario;
* compararlos con cualquier tratamiento.

Una misma configuración puede contener varios controles.

---

# Serie experimental

Una **serie** representa la evolución temporal de una condición experimental.

Cada serie está formada por los valores correspondientes a un mismo tratamiento medidos en diferentes tiempos.

Por ejemplo:

```text
Tiempo 0
Tiempo 1
Tiempo 2
...
Tiempo 24
```

ODPlate construye automáticamente estas series utilizando la información de la configuración experimental y las matrices procesadas.

Posteriormente, las series constituyen la entrada para:

* gráficas;
* métricas;
* modelos matemáticos;
* rankings.

---

# Grupo

Los **grupos** permiten organizar tratamientos relacionados.

Por ejemplo:

```text
Aceites cítricos

- Limón
- Naranja
- Mandarina
```

o bien

```text
Antibióticos

- Penicilina
- Ampicilina
- Gentamicina
```

Los grupos facilitan:

* filtrar resultados;
* generar gráficas específicas;
* crear reportes parciales;
* comparar únicamente subconjuntos del experimento.

---

# Configuración

Toda la organización del experimento se almacena en un único archivo de configuración.

Este archivo contiene información como:

* dimensiones de la placa;
* tamaño de las submatrices;
* posición de cada tratamiento;
* grupos experimentales;
* controles;
* nombres de las series;
* concentraciones;
* características adicionales del experimento.

Normalmente este archivo es generado automáticamente mediante el diseñador gráfico de placas.

Una vez creado, puede reutilizarse para cualquier cantidad de experimentos que compartan el mismo diseño experimental.

---

# Matrices procesadas

Después de leer los archivos de absorbancia, ODPlate genera internamente un conjunto de matrices procesadas.

Para cada tiempo experimental se almacenan automáticamente:

* matriz de medias;
* matriz de desviaciones estándar;
* matriz de errores estándar;
* número de réplicas.

Estas matrices constituyen la base de todas las etapas posteriores del análisis.

Además, la biblioteca permite exportarlas automáticamente a archivos Excel para facilitar su inspección y reutilización.

---

# Flujo interno de procesamiento

Conceptualmente, ODPlate transforma los datos experimentales siguiendo el siguiente flujo:

```text
Archivos Excel
        │
        ▼
Lectura de matrices
        │
        ▼
Corrección por blanco
        │
        ▼
Promediado de submatrices
        │
        ▼
Matrices procesadas
        │
        ▼
Construcción de series
        │
        ▼
Métricas
        │
        ▼
Modelos
        │
        ▼
Ranking
        │
        ▼
Gráficas y reportes
```

Este flujo representa la filosofía general de la biblioteca y constituye la base de todas las funciones documentadas en las siguientes secciones.

---

# ¿Qué ocurre automáticamente?

Una de las principales ventajas de ODPlate es que muchas tareas repetitivas son ejecutadas automáticamente.

Por ejemplo, durante el procesamiento la biblioteca puede:

* localizar el blanco correspondiente;
* corregir las mediciones;
* promediar las réplicas técnicas;
* calcular la desviación estándar;
* calcular el error estándar;
* construir las series temporales;
* almacenar todas las matrices procesadas;
* preparar los datos para las etapas posteriores.

De esta forma, el usuario puede concentrarse en la interpretación de los resultados sin preocuparse por operaciones repetitivas o propensas a errores.

---

# Resumen

En términos generales, ODPlate puede entenderse como un sistema compuesto por tres niveles:

1. **Diseño experimental**, donde se describe cómo está organizada la placa.
2. **Procesamiento**, donde las mediciones de absorbancia se transforman en datos estadísticos y series experimentales.
3. **Análisis**, donde se calculan métricas, se ajustan modelos, se generan figuras y se producen los reportes finales.

Comprender esta estructura facilitará el uso de todas las clases y funciones descritas en el resto de esta documentación.

# Diseñador de Placas (Plate Designer)

El **Plate Designer** es una herramienta gráfica interactiva que permite construir la configuración completa de un experimento sin necesidad de escribir código.

A través de una interfaz visual es posible definir:

* dimensiones de la placa;
* tamaño de las submatrices;
* tratamientos;
* controles;
* grupos experimentales;
* nombres de las series;
* concentraciones;
* organización espacial del experimento.

Una vez finalizado el diseño, la configuración puede guardarse como un archivo JSON que posteriormente será utilizado por la clase `ExperimentoOD` para analizar cualquier experimento que comparta la misma organización.

---

# ¿Por qué utilizar el diseñador?

Aunque una configuración puede construirse manualmente mediante un diccionario de Python, el diseñador ofrece numerosas ventajas:

* Reduce errores de configuración.
* Permite visualizar toda la placa antes del análisis.
* Valida automáticamente la consistencia del diseño.
* Facilita la reutilización de experimentos.
* Elimina la necesidad de editar archivos JSON manualmente.

En la mayoría de los casos se recomienda utilizar el diseñador incluso cuando posteriormente el procesamiento se realice mediante código.

---

# Crear un diseñador

El diseñador puede crearse mediante la función:

```python
from odplate import crear_disenador_placa

designer = crear_disenador_placa(
    filas=8,
    columnas=12,
    submatriz=3
)

designer.mostrar()
```

También puede construirse directamente utilizando la clase:

```python
from odplate import PlateDesigner

designer = PlateDesigner(
    filas=8,
    columnas=12,
    submatriz=3
)

designer.mostrar()
```

En ambos casos el resultado es exactamente el mismo.

---

# Parámetros

## filas

Tipo:

```python
int
```

Número de filas de la placa.

Ejemplo:

```python
filas=8
```

Corresponde a una placa convencional de 96 pozos.

También pueden utilizarse otros tamaños compatibles con el diseño experimental.

---

## columnas

Tipo:

```python
int
```

Número de columnas de la placa.

Ejemplo:

```python
columnas=12
```

---

## submatriz

Tipo:

```python
int
```

Número de columnas que constituyen una réplica técnica.

Por ejemplo:

```python
submatriz=3
```

significa que cada tratamiento utiliza tres columnas consecutivas.

Una placa de:

```text
8 × 12
```

producirá matrices procesadas de:

```text
8 × 4
```

---

# Mostrar la interfaz

Una vez creado el diseñador, la interfaz gráfica se despliega mediante:

```python
designer.mostrar()
```

En Google Colab y Jupyter Notebook aparecerá automáticamente la ventana interactiva.

---

# Organización de la interfaz

La interfaz se divide en cinco secciones principales.

## 1. Dimensiones

Permite modificar:

* número de filas;
* número de columnas;
* tamaño de la submatriz.

Estos parámetros pueden cambiarse antes de comenzar el diseño.

---

## 2. Selección de la placa

En esta sección aparece la representación gráfica de la placa.

Cada botón corresponde a un pozo.

El usuario puede seleccionar bloques completos que posteriormente serán asignados a tratamientos o controles.

La biblioteca no permite seleccionar regiones incompatibles con el tamaño de submatriz definido.

---

## 3. Asignación

Una vez seleccionada una región de la placa es posible asignarle información experimental.

Los principales campos son:

### Tipo

Permite indicar si la selección corresponde a:

* tratamiento;
* control.

---

### Aceite

Nombre general del compuesto o tratamiento.

Por ejemplo:

```text
Orégano
```

---

### Grupo

Categoría experimental a la que pertenece la serie.

Ejemplo:

```text
Aceites esenciales
```

---

### Nombre

Nombre específico que aparecerá posteriormente en los reportes y gráficas.

Por ejemplo:

```text
150 μg/mL
```

---

### Cantidad

Número de tiempos experimentales asociados a esa serie.

---

### Control asociado

Permite indicar qué control debe utilizarse como referencia para esa serie.

---

## 4. Elementos

En esta sección se muestran todas las series creadas.

Desde aquí es posible:

* editar;
* eliminar;
* revisar;
* cargar nuevamente una configuración existente.

---

## 5. Validación y exportación

Finalmente el diseñador permite:

* validar la configuración;
* exportarla como JSON;
* generar automáticamente el código Python equivalente.

---

# Flujo de trabajo recomendado

El procedimiento habitual para diseñar una placa es:

1. Definir las dimensiones.
2. Seleccionar un bloque.
3. Asignarle un tratamiento o control.
4. Repetir el proceso hasta completar la placa.
5. Validar la configuración.
6. Guardar el archivo JSON.

Posteriormente este archivo podrá utilizarse tantas veces como sea necesario.

---

# Guardar la configuración

Una vez terminado el diseño, la configuración puede exportarse mediante el botón **Guardar JSON**.

También puede realizarse desde código:

```python
configuracion = designer.obtener_configuracion()
```

El resultado es un diccionario completamente compatible con la clase `ExperimentoOD`.

---

# Cargar una configuración existente

Una configuración previamente guardada puede recuperarse mediante:

```python
designer.cargar_configuracion(
    "configuracion.json"
)
```

Esto permite modificar diseños ya existentes sin necesidad de reconstruirlos desde cero.

---

# Validación automática

Antes de exportar la configuración, el diseñador realiza diversas comprobaciones de consistencia.

Entre ellas:

* bloques superpuestos;
* regiones incompletas;
* controles inexistentes;
* dimensiones incompatibles;
* series duplicadas;
* configuraciones inválidas.

Si se detecta algún problema, el diseñador informa al usuario antes de permitir la exportación.

---

# Exportación a Python

Además del archivo JSON, el diseñador puede generar automáticamente el código Python equivalente al diseño realizado.

Esta funcionalidad resulta especialmente útil cuando se desea integrar la configuración directamente dentro de un proyecto o reproducir experimentos sin depender de archivos externos.

---

# Buenas prácticas

Se recomienda:

* utilizar nombres descriptivos para las series;
* organizar tratamientos similares dentro del mismo grupo;
* reutilizar una misma configuración cuando el diseño experimental no cambie;
* validar siempre la configuración antes de comenzar el procesamiento;
* conservar el archivo JSON junto con los datos experimentales.

---

# Ejemplo completo

```python
from odplate import crear_disenador_placa

designer = crear_disenador_placa(
    filas=8,
    columnas=12,
    submatriz=3
)

designer.mostrar()

# Una vez finalizado el diseño:

configuracion = designer.obtener_configuracion()
```

La configuración obtenida constituye la base de todo el flujo de trabajo posterior y será utilizada para crear el objeto `ExperimentoOD`.


# La clase `ExperimentoOD`

La clase **`ExperimentoOD`** constituye el componente principal de ODPlate y representa un experimento completo de densidad óptica.

Todas las operaciones realizadas por la biblioteca se organizan alrededor de esta clase.

Una instancia de `ExperimentoOD` almacena no solamente la configuración del experimento, sino también todos los datos derivados del procesamiento, incluyendo:

* configuración experimental;
* información de tratamientos y controles;
* archivos de absorbancia cargados;
* matrices procesadas;
* series experimentales;
* métricas calculadas;
* modelos ajustados;
* rankings;
* gráficas;
* reportes generados.

En términos prácticos, un objeto `ExperimentoOD` representa el estado completo de un experimento durante todo su ciclo de vida.

---

# Filosofía de diseño

ODPlate sigue una filosofía orientada a objetos.

En lugar de trabajar con funciones independientes que reciben continuamente matrices y configuraciones, la biblioteca mantiene toda la información del experimento dentro de un único objeto.

Esto proporciona varias ventajas:

* evita duplicación de código;
* reduce errores de configuración;
* facilita la reproducibilidad;
* simplifica la generación de reportes;
* mantiene todos los resultados organizados en un único lugar.

---

# Flujo de trabajo

El flujo habitual de trabajo con un objeto `ExperimentoOD` es el siguiente:

```text
Crear experimento
        │
        ▼
Leer archivos Excel
        │
        ▼
Procesar matrices
        │
        ▼
Construir series
        │
        ▼
Calcular métricas
        │
        ▼
Ajustar modelos
        │
        ▼
Calcular rankings
        │
        ▼
Generar gráficas
        │
        ▼
Exportar reportes
```

Aunque este es el flujo recomendado, cada etapa puede ejecutarse de manera independiente según las necesidades del usuario.

---

# Crear un experimento

La forma más habitual consiste en utilizar un archivo JSON generado por el diseñador de placas.

```python
from odplate import ExperimentoOD

experimento = ExperimentoOD(
    "configuracion.json"
)
```

También es posible crear un experimento a partir de un diccionario de Python.

```python
configuracion = {
    ...
}

experimento = ExperimentoOD(configuracion)
```

Esta modalidad resulta especialmente útil cuando la configuración se genera automáticamente mediante otro programa.

---

# Parámetros del constructor

## configuracion

**Tipo**

```python
str | pathlib.Path | dict
```

Define la configuración experimental.

Puede tomar tres formas diferentes.

### 1. Archivo JSON

```python
experimento = ExperimentoOD(
    "configuracion.json"
)
```

Es la opción recomendada.

---

### 2. Ruta absoluta

```python
experimento = ExperimentoOD(
    "/home/usuario/proyecto/configuracion.json"
)
```

---

### 3. Diccionario

```python
experimento = ExperimentoOD(
    configuracion
)
```

ODPlate validará automáticamente la estructura antes de crear el experimento.

---

# Validación automática

Durante la construcción del objeto se realizan diversas comprobaciones para garantizar la consistencia de la configuración.

Entre ellas:

* existencia de la configuración;
* formato correcto del archivo;
* dimensiones compatibles;
* controles válidos;
* series correctamente definidas;
* grupos consistentes;
* ausencia de identificadores duplicados.

Si alguna validación falla, se genera una excepción indicando claramente el problema encontrado.

---

# Información almacenada

Una vez creado el experimento, el objeto comienza prácticamente vacío.

A medida que se ejecutan los distintos métodos, se van incorporando nuevos resultados.

Por ejemplo:

```text
Experimento
│
├── Configuración
├── Series
├── Controles
├── Archivos Excel
├── Matrices
├── Métricas
├── Modelos
├── Ranking
├── Figuras
└── Reportes
```

Esto permite acceder posteriormente a cualquiera de estos componentes sin necesidad de volver a calcularlos.

---

# Ciclo de vida del objeto

Durante un análisis típico, el contenido del objeto evoluciona progresivamente.

## Después del constructor

```text
✓ Configuración
```

---

## Después de cargar los archivos

```text
✓ Configuración
✓ Archivos Excel
```

---

## Después del procesamiento

```text
✓ Configuración
✓ Archivos Excel
✓ Matrices procesadas
✓ Series
```

---

## Después del cálculo de métricas

```text
✓ Configuración
✓ Archivos Excel
✓ Matrices
✓ Series
✓ Métricas
```

---

## Después del ajuste de modelos

```text
✓ Configuración
✓ Archivos Excel
✓ Matrices
✓ Series
✓ Métricas
✓ Modelos
```

---

## Después de generar reportes

```text
✓ Configuración
✓ Archivos Excel
✓ Matrices
✓ Series
✓ Métricas
✓ Modelos
✓ Ranking
✓ Figuras
✓ Reportes
```

Este diseño evita recalcular información que ya ha sido obtenida previamente.

---

# Métodos principales

La mayor parte de las tareas del análisis se realizan mediante los siguientes métodos públicos.

| Método                | Descripción                                   |
| --------------------- | --------------------------------------------- |
| `cargar_resultados()` | Lee los archivos de absorbancia.              |
| `procesar()`          | Procesa las matrices experimentales.          |
| `calcular_metricas()` | Calcula las métricas experimentales.          |
| `ajustar_modelos()`   | Ajusta los modelos matemáticos disponibles.   |
| `calcular_ranking()`  | Clasifica tratamientos según un criterio.     |
| `graficar()`          | Genera figuras listas para publicación.       |
| `generar_reporte()`   | Exporta todos los resultados del experimento. |

Cada uno de estos métodos será documentado detalladamente en las siguientes secciones.

---

# Acceso a la configuración

La configuración original permanece disponible durante todo el análisis.

```python
experimento.config
```

Esto permite consultar cualquier información del diseño experimental sin necesidad de volver a cargar el archivo JSON.

---

# Acceso a los resultados

Una vez ejecutadas las distintas etapas del análisis, los resultados permanecen almacenados dentro del experimento.

Por ejemplo, dependiendo de las operaciones realizadas, el usuario podrá acceder a:

* matrices procesadas;
* series experimentales;
* métricas;
* modelos ajustados;
* rankings;
* configuraciones exportadas.

De esta manera, el experimento actúa como un contenedor centralizado de toda la información generada.

---

# Recomendaciones

Para aprovechar al máximo la arquitectura de ODPlate se recomienda:

* crear un único objeto `ExperimentoOD` por cada experimento;
* reutilizar el mismo objeto durante todo el análisis;
* evitar reconstruir el experimento entre etapas;
* conservar el archivo JSON original junto con los datos experimentales;
* generar los reportes únicamente una vez finalizado el procesamiento.

Este flujo garantiza que todos los resultados permanezcan sincronizados y facilita la reproducción completa del análisis en el futuro.

# Método `cargar_resultados()`

Una vez creado el objeto `ExperimentoOD`, el siguiente paso consiste en cargar los archivos de absorbancia obtenidos durante el experimento.

Esta tarea se realiza mediante el método:

```python
experimento.cargar_resultados(...)
```

Este método localiza automáticamente los archivos experimentales, identifica el blanco (cuando existe), organiza las mediciones según el tiempo experimental y prepara toda la información necesaria para el procesamiento posterior.

---

# Sintaxis

```python
experimento.cargar_resultados(
    ruta,
    nombre_blanco=None,
    coincidencia_blanco="exacta"
)
```

---

# Parámetros

## `ruta`

**Tipo**

```python
str | pathlib.Path
```

Ruta de la carpeta que contiene los archivos Excel del experimento.

Todos los archivos compatibles encontrados dentro de esta carpeta serán leídos automáticamente.

### Ejemplo

```python
experimento.cargar_resultados(
    ruta="Datos"
)
```

También es posible utilizar rutas absolutas.

```python
experimento.cargar_resultados(
    ruta="/home/usuario/Experimentos/Ecoli"
)
```

o utilizando `Path`:

```python
from pathlib import Path

experimento.cargar_resultados(
    ruta=Path("Datos")
)
```

---

## `nombre_blanco`

**Tipo**

```python
str | None
```

Permite indicar cuál de los archivos corresponde al blanco experimental.

Si se especifica este parámetro, la biblioteca separará automáticamente dicho archivo del resto de los tiempos experimentales.

### Ejemplo

```python
experimento.cargar_resultados(
    ruta="Datos",
    nombre_blanco="Blanco"
)
```

---

Cuando el nombre del blanco contiene información adicional, también puede utilizarse:

```python
experimento.cargar_resultados(
    ruta="Datos",
    nombre_blanco="control"
)
```

junto con el parámetro `coincidencia_blanco`.

---

Si no existe blanco experimental, simplemente puede omitirse.

```python
experimento.cargar_resultados(
    ruta="Datos"
)
```

---

## `coincidencia_blanco`

**Tipo**

```python
str
```

Controla la forma en que ODPlate identifica el archivo correspondiente al blanco.

Valores permitidos:

### `"exacta"`

El nombre debe coincidir exactamente.

Ejemplo:

```text
Blanco.xlsx
```

Código:

```python
experimento.cargar_resultados(
    ruta="Datos",
    nombre_blanco="Blanco",
    coincidencia_blanco="exacta"
)
```

---

### `"contiene"`

El archivo será considerado blanco cuando su nombre contenga el texto indicado.

Ejemplo:

```text
Ecoli_Blanco.xlsx
```

```python
experimento.cargar_resultados(
    ruta="Datos",
    nombre_blanco="Blanco",
    coincidencia_blanco="contiene"
)
```

---

### `"empieza"`

El nombre debe comenzar con el texto indicado.

```text
Blanco_Control.xlsx
```

```python
experimento.cargar_resultados(
    ruta="Datos",
    nombre_blanco="Blanco",
    coincidencia_blanco="empieza"
)
```

---

### `"termina"`

El nombre debe terminar con el texto indicado.

```text
Muestra_Blanco.xlsx
```

```python
experimento.cargar_resultados(
    ruta="Datos",
    nombre_blanco="Blanco",
    coincidencia_blanco="termina"
)
```

---

# ¿Qué realiza internamente este método?

Al ejecutarse, `cargar_resultados()` realiza automáticamente las siguientes operaciones:

1. Busca todos los archivos compatibles dentro de la carpeta indicada.
2. Identifica el archivo correspondiente al blanco (si existe).
3. Lee las matrices de absorbancia.
4. Extrae el identificador temporal de cada archivo.
5. Ordena cronológicamente todas las mediciones.
6. Verifica que no existan tiempos duplicados.
7. Almacena toda la información dentro del experimento.

El usuario no necesita realizar ninguna de estas tareas manualmente.

---

# Resultado

Después de ejecutar este método, el objeto `ExperimentoOD` contiene todas las matrices originales del experimento listas para ser procesadas.

A partir de este momento ya es posible ejecutar:

```python
experimento.procesar()
```

---

# Ejemplo mínimo

```python
from odplate import ExperimentoOD

experimento = ExperimentoOD(
    "configuracion.json"
)

experimento.cargar_resultados(
    ruta="Datos"
)
```

---

# Ejemplo utilizando un blanco

```python
experimento.cargar_resultados(
    ruta="Datos",
    nombre_blanco="Blanco"
)
```

---

# Ejemplo utilizando coincidencia parcial

```python
experimento.cargar_resultados(
    ruta="Datos",
    nombre_blanco="Blanco",
    coincidencia_blanco="contiene"
)
```

---

# Buenas prácticas

Se recomienda:

* almacenar todos los archivos correspondientes a un mismo experimento dentro de una única carpeta;
* utilizar nombres consistentes para los tiempos experimentales;
* conservar el archivo del blanco junto con el resto de las mediciones;
* utilizar nombres descriptivos que faciliten su identificación.

---

# Errores comunes

## La carpeta no existe

Si la ruta especificada no existe, se generará una excepción indicando que la carpeta no pudo localizarse.

---

## No se encontró el blanco

Cuando se especifica `nombre_blanco` y ningún archivo cumple el criterio de búsqueda, ODPlate informará del problema.

---

## Archivos duplicados

Si dos archivos representan el mismo tiempo experimental, la biblioteca detendrá la ejecución para evitar inconsistencias durante el procesamiento.

---

## Formato incompatible

Si alguno de los archivos no corresponde al formato esperado de una matriz de absorbancia, se generará una excepción indicando el archivo que produjo el problema.

---

# Flujo recomendado

Normalmente este método se utiliza inmediatamente después de crear el experimento.

```python
experimento = ExperimentoOD(
    "configuracion.json"
)

experimento.cargar_resultados(
    ruta="Datos",
    nombre_blanco="Blanco"
)

experimento.procesar()
```

Este es el flujo recomendado para prácticamente todos los experimentos realizados con ODPlate.
# Método `procesar()`

Una vez cargados los archivos de absorbancia mediante `cargar_resultados()`, el siguiente paso consiste en transformar las matrices originales en un conjunto de datos estadísticamente procesados.

Esta tarea se realiza mediante el método:

```python
experimento.procesar(...)
```

Durante esta etapa ODPlate convierte las matrices crudas de absorbancia en matrices experimentales listas para su análisis.

Es probablemente el método más importante de toda la biblioteca, ya que todas las etapas posteriores (métricas, modelos, gráficas y reportes) utilizan los resultados obtenidos aquí.

---

# Sintaxis

```python
experimento.procesar(
    restar_blanco=True,
    ddof=1
)
```

---

# Parámetros

## `restar_blanco`

**Tipo**

```python
bool
```

**Valor por defecto**

```python
True
```

Indica si debe corregirse la absorbancia utilizando la matriz correspondiente al blanco experimental.

Cuando el parámetro es `True`, cada medición será corregida automáticamente restando el valor correspondiente del blanco.

### Ejemplo

```python
experimento.procesar(
    restar_blanco=True
)
```

Esta es la opción recomendada para la mayoría de los experimentos.

---

También es posible omitir la corrección:

```python
experimento.procesar(
    restar_blanco=False
)
```

En este caso las matrices conservarán los valores originales.

---

## ¿Cuándo utilizar cada opción?

### `True`

Se recomienda cuando:

* existe una medición de blanco;
* se desea eliminar el ruido basal del instrumento;
* las mediciones deben compararse respecto al medio de cultivo.

---

### `False`

Puede utilizarse cuando:

* el equipo ya realizó la corrección;
* los archivos ya contienen valores corregidos;
* se desea inspeccionar las absorbancias originales.

---

## `ddof`

**Tipo**

```python
int
```

**Valor por defecto**

```python
1
```

Controla el cálculo de la desviación estándar.

Corresponde al parámetro **Delta Degrees of Freedom** utilizado por NumPy.

### Ejemplo

```python
experimento.procesar(
    ddof=1
)
```

Produce la desviación estándar muestral.

---

También puede utilizarse:

```python
experimento.procesar(
    ddof=0
)
```

para calcular la desviación estándar poblacional.

---

En la mayoría de los experimentos biológicos se recomienda mantener el valor por defecto (`ddof=1`).

---

# ¿Qué realiza internamente este método?

Durante el procesamiento ODPlate ejecuta automáticamente las siguientes etapas.

## 1. Organización de las matrices

Las matrices experimentales son ordenadas según el tiempo correspondiente.

---

## 2. Corrección por blanco

Si existe una matriz de blanco y `restar_blanco=True`, ésta se resta automáticamente a cada tiempo experimental.

---

## 3. División en submatrices

Cada fila se divide utilizando el tamaño de submatriz definido durante el diseño experimental.

Por ejemplo:

```text
A1 A2 A3 | A4 A5 A6 | A7 A8 A9 | A10 A11 A12
```

con:

```text
submatriz = 3
```

produce:

```text
[A1 A2 A3]
[A4 A5 A6]
[A7 A8 A9]
[A10 A11 A12]
```

---

## 4. Cálculo de estadísticas

Para cada submatriz se calculan automáticamente:

* media;
* desviación estándar;
* error estándar;
* número de observaciones.

---

## 5. Construcción de las matrices procesadas

Cada tiempo experimental queda representado por cuatro matrices distintas.

* Medias.
* Desviaciones estándar.
* Errores estándar.
* Número de réplicas.

Estas matrices serán utilizadas posteriormente por toda la biblioteca.

---

# ¿Qué cambia dentro del objeto `ExperimentoOD`?

Antes de ejecutar `procesar()` el experimento únicamente contiene las matrices originales.

```text
Experimento
│
├── Configuración
├── Archivos Excel
└── Matrices originales
```

Después del procesamiento el experimento incorpora automáticamente las matrices estadísticas.

```text
Experimento
│
├── Configuración
├── Archivos Excel
├── Matrices originales
├── Matrices promedio
├── Matrices desviación estándar
├── Matrices error estándar
└── Número de réplicas
```

A partir de este momento ya es posible calcular métricas, ajustar modelos y generar gráficas.

---

# Valor de retorno

Este método modifica el estado interno del experimento.

No es necesario capturar ningún valor de retorno.

Simplemente:

```python
experimento.procesar()
```

---

# Ejemplo mínimo

```python
experimento.procesar()
```

---

# Utilizando corrección por blanco

```python
experimento.procesar(
    restar_blanco=True
)
```

---

# Conservando las absorbancias originales

```python
experimento.procesar(
    restar_blanco=False
)
```

---

# Utilizando desviación estándar poblacional

```python
experimento.procesar(
    restar_blanco=True,
    ddof=0
)
```

---

# Buenas prácticas

Se recomienda:

* utilizar siempre el mismo valor de `ddof` durante un proyecto;
* conservar la matriz de blanco junto con el resto del experimento;
* no modificar manualmente las matrices procesadas;
* volver a ejecutar `procesar()` únicamente cuando cambien los datos originales.

---

# Errores comunes

## No se cargaron los archivos

Si `procesar()` se ejecuta antes de `cargar_resultados()`, la biblioteca generará una excepción indicando que no existen matrices para procesar.

---

## Tamaño de submatriz incompatible

Si las dimensiones de la placa no son compatibles con el tamaño de submatriz definido en la configuración, el procesamiento se detendrá mostrando el problema detectado.

---

## Blanco inexistente

Si se solicita la corrección por blanco pero el experimento no contiene una matriz de blanco, ODPlate informará del problema mediante una excepción.

---

# Flujo recomendado

El orden habitual de ejecución es:

```python
experimento.cargar_resultados(
    ruta="Datos",
    nombre_blanco="Blanco"
)

experimento.procesar()

experimento.calcular_todo()
```

Una vez finalizado el procesamiento, el experimento se encuentra preparado para todas las etapas posteriores del análisis.
# Inspeccionando el experimento

Aunque la mayoría de las operaciones de ODPlate pueden realizarse mediante los métodos de alto nivel de la clase `ExperimentoOD`, en muchas ocasiones resulta útil acceder directamente a la información almacenada dentro del experimento.

Todos los resultados generados durante el análisis permanecen disponibles dentro del objeto y pueden consultarse en cualquier momento.

Esta característica facilita la realización de análisis personalizados sin necesidad de volver a procesar los datos.

---

# La estructura del experimento

Conceptualmente, un objeto `ExperimentoOD` puede visualizarse de la siguiente manera:

```text
ExperimentoOD
│
├── Configuración
├── Series experimentales
├── Controles
├── Archivos originales
├── Matrices procesadas
├── Métricas
├── Modelos ajustados
├── Rankings
├── Figuras
└── Reportes
```

Cada uno de estos componentes se incorpora automáticamente conforme avanza el flujo de trabajo.

---

# Consultar la configuración

La configuración utilizada para construir el experimento permanece disponible durante toda la ejecución.

```python
experimento.config
```

Este atributo contiene exactamente la información almacenada en el archivo JSON generado por el diseñador de placas.

Puede utilizarse para inspeccionar cualquier aspecto del diseño experimental.

Por ejemplo:

```python
print(experimento.config["filas"])

print(experimento.config["columnas"])

print(experimento.config["submatriz"])
```

---

# Series experimentales

Una vez creada la configuración, todas las series experimentales quedan disponibles dentro del experimento.

```python
experimento.series
```

Este atributo contiene una colección de objetos `Serie`.

Cada serie describe una condición experimental específica.

Entre otras propiedades, cada serie almacena información como:

* identificador;
* nombre;
* grupo;
* tratamiento;
* control asociado;
* posición dentro de la placa;
* tiempos experimentales.

Por ejemplo:

```python
for serie in experimento.series:

    print(serie.id)

    print(serie.nombre)

    print(serie.grupo)
```

---

# Controles

Los controles definidos durante el diseño experimental pueden consultarse mediante:

```python
experimento.controles
```

Cada elemento corresponde a un objeto de tipo `Serie`, pero identificado como control.

Esto permite tratarlos exactamente igual que cualquier otro tratamiento.

---

# Matrices procesadas

Después de ejecutar:

```python
experimento.procesar()
```

el experimento incorpora automáticamente las matrices procesadas.

Estas matrices constituyen la base para todas las etapas posteriores del análisis.

Dependiendo del procesamiento realizado, estarán disponibles:

* medias;
* desviaciones estándar;
* errores estándar;
* número de réplicas.

Estas matrices son utilizadas internamente por la biblioteca, aunque también pueden inspeccionarse o exportarse.

---

# Resultados de las métricas

Después de ejecutar:

```python
experimento.calcular_metricas()
```

o

```python
experimento.calcular_todo()
```

los resultados quedan almacenados dentro del experimento.

Cada métrica calculada puede reutilizarse posteriormente para:

* generar gráficas;
* construir rankings;
* exportar reportes;
* realizar análisis adicionales.

No es necesario recalcular las métricas cada vez que se requieran.

---

# Modelos ajustados

Una vez ejecutado:

```python
experimento.ajustar_modelos()
```

los modelos matemáticos permanecen almacenados dentro del experimento.

Cada modelo conserva toda la información correspondiente al ajuste realizado.

Por ejemplo:

* parámetros estimados;
* coeficientes;
* medidas de ajuste;
* predicciones;
* información auxiliar.

Estos resultados pueden utilizarse posteriormente sin necesidad de repetir el proceso de optimización.

---

# Rankings

Después de calcular un ranking:

```python
ranking = experimento.calcular_ranking(...)
```

el resultado puede almacenarse y reutilizarse posteriormente.

Los rankings permiten ordenar tratamientos utilizando cualquiera de los criterios implementados por la biblioteca o criterios definidos por el propio usuario.

---

# Figuras

Las figuras generadas mediante:

```python
experimento.graficar(...)
```

pueden guardarse automáticamente en disco.

Además, dependiendo del flujo de trabajo utilizado, el experimento conserva la información necesaria para reconstruir dichas figuras sin volver a procesar los datos.

---

# Reportes

Los reportes generados mediante:

```python
experimento.generar_reporte(...)
```

no modifican los resultados del experimento.

Simplemente exportan la información ya disponible a distintos formatos, como:

* Excel;
* CSV;
* Word;
* HTML;
* PDF.

Esto significa que un mismo experimento puede exportarse múltiples veces utilizando diferentes configuraciones sin necesidad de recalcular métricas o modelos.

---

# Estado del experimento

El contenido del objeto evoluciona conforme se ejecutan los distintos métodos.

## Después del constructor

```text
✓ Configuración
```

---

## Después de cargar los archivos

```text
✓ Configuración
✓ Archivos originales
```

---

## Después del procesamiento

```text
✓ Configuración
✓ Archivos originales
✓ Matrices procesadas
```

---

## Después del cálculo de métricas

```text
✓ Configuración
✓ Archivos originales
✓ Matrices procesadas
✓ Métricas
```

---

## Después del ajuste de modelos

```text
✓ Configuración
✓ Archivos originales
✓ Matrices procesadas
✓ Métricas
✓ Modelos
```

---

## Después de generar los reportes

```text
✓ Configuración
✓ Archivos originales
✓ Matrices procesadas
✓ Métricas
✓ Modelos
✓ Rankings
✓ Reportes
```

---

# ¿Debo acceder directamente a estos atributos?

En la mayoría de los casos, **no**.

La forma recomendada de utilizar ODPlate consiste en trabajar mediante los métodos públicos de `ExperimentoOD`.

Sin embargo, cuando se desea desarrollar análisis personalizados, crear nuevas visualizaciones o implementar algoritmos propios, acceder directamente a estos atributos puede resultar extremadamente útil.

La arquitectura de ODPlate ha sido diseñada precisamente para facilitar este tipo de extensiones sin necesidad de modificar el núcleo de la biblioteca.

# Método `calcular_todo()`

El método `calcular_todo()` constituye la forma recomendada de realizar el análisis cuantitativo de un experimento.

Su objetivo es ejecutar automáticamente todas las etapas posteriores al procesamiento de las matrices, evitando que el usuario tenga que invocar cada módulo de manera independiente.

En la mayoría de los casos este será el único método necesario para calcular todas las métricas y ajustar los modelos disponibles.

---

# ¿Qué hace este método?

Cuando se ejecuta:

```python
experimento.calcular_todo()
```

ODPlate realiza automáticamente todas las operaciones necesarias para transformar las matrices procesadas en resultados científicos listos para su análisis.

Dependiendo de la configuración del experimento y de los parámetros utilizados, el método puede realizar automáticamente:

* extracción de las series experimentales;
* normalización de las curvas;
* cálculo de todas las métricas disponibles;
* ajuste de todos los modelos matemáticos registrados;
* estimación de parámetros biológicos;
* organización de los resultados.

El usuario no necesita preocuparse por el orden de ejecución de cada una de estas etapas.

---

# Sintaxis

```python
experimento.calcular_todo(
    normalizacion="ninguno",
    ajustar_modelos=True
)
```

---

# Parámetros

## `normalizacion`

**Tipo**

```python
str
```

Indica la estrategia de normalización que se utilizará antes de calcular las métricas y ajustar los modelos.

El valor seleccionado se aplicará a todas las series experimentales.

### Valores permitidos

#### `"ninguno"`

No se realiza ninguna transformación sobre los datos.

Las curvas conservan exactamente los valores obtenidos durante el procesamiento.

```python
experimento.calcular_todo(
    normalizacion="ninguno"
)
```

Esta es la opción recomendada cuando se desea trabajar directamente con absorbancias corregidas.

---

#### `"delta"`

Las series se expresan como variaciones respecto al tiempo inicial.

```python
experimento.calcular_todo(
    normalizacion="delta"
)
```

Esta opción suele ser útil para comparar tratamientos con diferentes absorbancias iniciales.

---

#### `"porcentaje"`

Transforma las curvas a porcentaje respecto al valor inicial o al criterio definido por la biblioteca.

```python
experimento.calcular_todo(
    normalizacion="porcentaje"
)
```

Resulta especialmente útil cuando se desea comparar experimentos realizados en condiciones diferentes.

---

#### `"control"`

Normaliza cada tratamiento respecto al control asociado definido durante el diseño experimental.

```python
experimento.calcular_todo(
    normalizacion="control"
)
```

Esta modalidad facilita la comparación directa entre tratamientos y controles.

---

> **Nota:** Los métodos de normalización disponibles pueden ampliarse en futuras versiones mediante el sistema de plugins de ODPlate.

---

## `ajustar_modelos`

**Tipo**

```python
bool
```

**Valor por defecto**

```python
True
```

Indica si además del cálculo de métricas deben ajustarse automáticamente todos los modelos matemáticos registrados.

### Ajustar modelos

```python
experimento.calcular_todo(
    ajustar_modelos=True
)
```

Esta es la opción recomendada.

---

### Calcular únicamente métricas

```python
experimento.calcular_todo(
    ajustar_modelos=False
)
```

En este caso la biblioteca omite completamente la etapa de optimización, reduciendo considerablemente el tiempo de ejecución.

---

# ¿Qué ocurre internamente?

Cuando este método es ejecutado, ODPlate realiza automáticamente el siguiente flujo de trabajo:

```text
Matrices procesadas
        │
        ▼
Extracción de series
        │
        ▼
Normalización
        │
        ▼
Cálculo de métricas
        │
        ▼
Ajuste de modelos
        │
        ▼
Resultados finales
```

Cada etapa utiliza la salida de la anterior.

---

# ¿Qué cambia dentro del experimento?

Antes de ejecutar este método el experimento únicamente contiene:

```text
✓ Configuración
✓ Archivos originales
✓ Matrices procesadas
```

Después de ejecutar:

```python
experimento.calcular_todo()
```

el objeto incorpora automáticamente:

```text
✓ Series experimentales
✓ Métricas
✓ Modelos
✓ Parámetros estimados
✓ Resultados listos para gráficas
✓ Resultados listos para reportes
```

Todo este contenido permanece almacenado en memoria y puede reutilizarse posteriormente.

---

# Valor de retorno

Este método actualiza el estado interno del experimento.

No es necesario capturar ningún valor.

Simplemente:

```python
experimento.calcular_todo()
```

---

# Ejemplo mínimo

```python
experimento.calcular_todo()
```

---

# Normalizando respecto al control

```python
experimento.calcular_todo(
    normalizacion="control"
)
```

---

# Calculando únicamente métricas

```python
experimento.calcular_todo(
    ajustar_modelos=False
)
```

---

# Ejemplo completo

```python
experimento.calcular_todo(
    normalizacion="delta",
    ajustar_modelos=True
)
```

---

# Buenas prácticas

Se recomienda:

* ejecutar `procesar()` antes de este método;
* mantener el mismo criterio de normalización para todos los experimentos de un proyecto;
* utilizar `ajustar_modelos=False` únicamente cuando los modelos no sean necesarios;
* evitar modificar manualmente las series una vez calculadas las métricas.

---

# Errores comunes

## Ejecutar el método antes de procesar

Si el experimento no contiene matrices procesadas, la biblioteca generará una excepción indicando que no existen datos suficientes para realizar los cálculos.

---

## Utilizar un método de normalización inexistente

Cuando se especifica un nombre no registrado, ODPlate informa del problema indicando las estrategias de normalización disponibles.

---

## Repetir innecesariamente el ajuste de modelos

El ajuste de modelos puede ser una de las etapas más costosas computacionalmente.

Si únicamente cambian las opciones de visualización o exportación, no es necesario volver a ejecutar `calcular_todo()`.

---

# Flujo recomendado

En la mayoría de los experimentos el flujo completo se reduce a:

```python
experimento = ExperimentoOD(
    "configuracion.json"
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

Este constituye el flujo de trabajo recomendado para la mayoría de los usuarios de ODPlate.
# Fundamentos del procesamiento de datos

Uno de los principales objetivos de ODPlate es automatizar el procesamiento de experimentos de densidad óptica sin ocultar la metodología utilizada.

Aunque la biblioteca realiza automáticamente todas las operaciones necesarias para transformar los archivos de absorbancia en resultados listos para su análisis, resulta importante comprender qué ocurre internamente durante este proceso.

En esta sección se describe el flujo de procesamiento seguido por ODPlate.

---

# Flujo completo de procesamiento

Conceptualmente, la biblioteca transforma los datos siguiendo el siguiente esquema:

```text
Archivos Excel
        │
        ▼
Lectura de matrices
        │
        ▼
Identificación del blanco
        │
        ▼
Corrección de absorbancia
        │
        ▼
Construcción de submatrices
        │
        ▼
Cálculo de estadísticas
        │
        ▼
Matrices procesadas
        │
        ▼
Construcción de series
        │
        ▼
Normalización
        │
        ▼
Cálculo de métricas
        │
        ▼
Ajuste de modelos
        │
        ▼
Ranking
        │
        ▼
Gráficas y reportes
```

Cada etapa utiliza los resultados obtenidos por la anterior y queda almacenada dentro del objeto `ExperimentoOD`.

---

# Lectura de archivos

El primer paso consiste en leer todos los archivos experimentales contenidos en la carpeta indicada por el usuario.

Cada archivo representa un tiempo experimental.

Durante esta etapa ODPlate:

* localiza automáticamente todos los archivos compatibles;
* identifica el blanco (si existe);
* extrae el identificador temporal;
* ordena cronológicamente todas las mediciones.

Las matrices originales permanecen almacenadas sin modificaciones para garantizar la reproducibilidad del análisis.

---

# Corrección por blanco

Cuando el experimento dispone de una medición de blanco y el usuario activa la opción correspondiente, cada matriz experimental se corrige automáticamente.

La corrección consiste en restar, elemento por elemento, la matriz del blanco a cada una de las matrices experimentales.

Matemáticamente:

```text
Matriz corregida = Matriz experimental − Matriz blanco
```

Este procedimiento elimina el efecto basal del medio de cultivo o del sistema de medición y constituye una práctica habitual en experimentos de densidad óptica.

---

# Construcción de submatrices

Una vez corregidas las absorbancias, cada matriz se divide utilizando el tamaño de submatriz definido durante el diseño experimental.

Por ejemplo, si la placa original tiene dimensiones:

```text
8 × 12
```

y el tamaño de submatriz es:

```text
3
```

cada grupo de tres columnas consecutivas se considera una única unidad experimental.

```text
A1  A2  A3 │ A4  A5  A6 │ A7  A8  A9 │ A10 A11 A12
```

se transforma en

```text
[A1 A2 A3]
[A4 A5 A6]
[A7 A8 A9]
[A10 A11 A12]
```

Cada bloque corresponde normalmente a las réplicas técnicas de una misma condición experimental.

---

# Cálculo de estadísticas

Para cada submatriz ODPlate calcula automáticamente:

* media;
* desviación estándar;
* error estándar de la media;
* número de observaciones.

Estos valores sustituyen a las réplicas originales durante el resto del análisis.

De esta manera, el usuario trabaja siempre con datos resumidos y estadísticamente consistentes.

---

# Construcción de las matrices procesadas

Después del procesamiento, para cada tiempo experimental existen varias matrices derivadas.

Entre ellas:

* matriz de medias;
* matriz de desviaciones estándar;
* matriz de errores estándar;
* matriz con el número de réplicas.

Estas matrices permanecen disponibles durante todo el análisis y pueden exportarse posteriormente mediante las herramientas de reporte de ODPlate.

---

# Construcción de series experimentales

Una vez calculadas las matrices procesadas, la biblioteca reorganiza automáticamente la información para construir las series temporales.

Cada serie representa la evolución de un tratamiento específico a lo largo del experimento.

Por ejemplo:

```text
Tiempo 0
Tiempo 1
Tiempo 2
...
Tiempo 24
```

Cada punto de la serie corresponde a la media calculada para ese tratamiento en el tiempo correspondiente.

Además de la media, cada punto conserva su desviación estándar y su error estándar, lo que permite representar correctamente la incertidumbre experimental en las figuras.

---

# Normalización

Antes del cálculo de métricas y del ajuste de modelos, las series pueden normalizarse.

La estrategia de normalización depende de los parámetros seleccionados por el usuario.

Dependiendo del método elegido, las curvas pueden conservar sus valores originales o transformarse respecto a una referencia determinada, como el tiempo inicial o el control experimental.

La normalización se aplica de manera uniforme a todas las series del experimento.

---

# Cálculo de métricas

A partir de las series experimentales, ODPlate calcula automáticamente las métricas registradas en la biblioteca.

Cada métrica constituye una descripción cuantitativa del comportamiento del tratamiento.

El sistema de métricas es completamente extensible y permite incorporar nuevas medidas mediante el mecanismo de plugins.

Esto facilita adaptar la biblioteca a diferentes dominios experimentales sin modificar el núcleo del proyecto.

---

# Ajuste de modelos

Cuando el usuario activa esta opción, ODPlate ajusta automáticamente todos los modelos matemáticos registrados.

Cada modelo estima los parámetros que mejor describen la evolución temporal observada para cada serie experimental.

Los resultados incluyen tanto los parámetros estimados como diversas medidas de calidad del ajuste.

Posteriormente, estos modelos pueden utilizarse para comparar tratamientos, generar predicciones o estimar parámetros biológicos.

---

# Ranking de tratamientos

Una vez calculadas las métricas y ajustados los modelos, los tratamientos pueden ordenarse utilizando cualquiera de los criterios disponibles.

El sistema de ranking de ODPlate no está limitado a un conjunto fijo de reglas.

Por el contrario, permite definir criterios completamente personalizados que utilizan cualquier combinación de métricas calculadas por la biblioteca.

Esto proporciona una gran flexibilidad para adaptar el análisis a distintos tipos de experimentos.

---

# Generación de figuras

Las gráficas producidas por ODPlate utilizan directamente las series experimentales y sus medidas de variabilidad.

Dependiendo de la configuración seleccionada, las figuras pueden incluir:

* desviaciones estándar;
* errores estándar;
* bandas de confianza;
* controles experimentales;
* tratamientos específicos;
* grupos completos;
* subconjuntos definidos por el usuario.

Además, las leyendas, títulos y demás elementos gráficos pueden personalizarse para adaptarse a las necesidades de cada proyecto o publicación científica.

---

# Exportación de resultados

Finalmente, toda la información generada durante el análisis puede exportarse automáticamente.

Entre los principales productos generados se encuentran:

* tablas de resultados;
* matrices procesadas;
* series experimentales;
* figuras;
* rankings;
* reportes completos.

Todos estos elementos se obtienen directamente a partir del estado interno del objeto `ExperimentoOD`, garantizando que los resultados exportados sean consistentes con el análisis realizado.

---

# Reproducibilidad

Una característica fundamental de ODPlate es que ninguna de las etapas descritas modifica los datos originales.

Los archivos de absorbancia permanecen intactos durante todo el proceso.

Todas las transformaciones se realizan sobre estructuras de datos independientes generadas por la biblioteca.

Esto garantiza que un mismo experimento pueda procesarse repetidamente utilizando diferentes parámetros sin alterar nunca la información original obtenida en el laboratorio.
# Método `graficar()`

Una de las principales fortalezas de ODPlate es la generación automática de figuras listas para su análisis, presentación o publicación.

El método `graficar()` permite visualizar las series experimentales utilizando diferentes criterios de selección, múltiples estrategias de representación del error experimental y un amplio conjunto de opciones de personalización.

Dependiendo de los parámetros utilizados, puede generar desde una única curva hasta un conjunto completo de figuras para todos los tratamientos del experimento.

---

# Sintaxis

```python
experimento.graficar(
    modo="grupos",
    aceites=None,
    grupos=None,
    incluir_ids=None,
    excluir_ids=None,
    mostrar_control=True,
    tipo="tratamiento",
    controles_ids=None,
    n_mejores=None,
    criterio=None,
    funcion_calificacion=None,
    mayor_es_mejor=True,
    top=None,
    bottom=None,
    rango=None,
    criterio_kwargs=None,
    normalizacion="ninguno",
    tiempos=None,
    mostrar_banda=True,
    mostrar_error="std",
    figsize=(11,6),
    titulo=None,
    eje_y="OD corregida",
    leyendas=None,
    formato_leyenda=None,
    mostrar_leyenda=True,
    leyenda_kwargs=None,
    guardar_en=None,
    mostrar=True
)
```

---

# Descripción general

Este método genera automáticamente una o varias figuras utilizando la información almacenada dentro del objeto `ExperimentoOD`.

Las figuras se construyen directamente a partir de las series experimentales calculadas previamente mediante `procesar()` y `calcular_todo()`.

No es necesario preparar manualmente los datos antes de llamar a este método.

---

# Modos de visualización

El parámetro más importante es `modo`.

Este determina qué series aparecerán en las figuras.

## `"grupos"`

Genera una figura independiente para cada grupo experimental.

```python
experimento.graficar(
    modo="grupos"
)
```

Es la opción recomendada para la mayoría de los experimentos.

---

## `"todo"`

Dibuja todas las series del experimento en una única figura.

```python
experimento.graficar(
    modo="todo"
)
```

Resulta útil cuando el número de tratamientos es reducido.

---

## `"mejores"`

Selecciona automáticamente los tratamientos mejor evaluados utilizando un criterio de ranking.

```python
experimento.graficar(
    modo="mejores",
    criterio=calificacion_inversa,
    n_mejores=10
)
```

---

## `"seleccion"`

Permite indicar exactamente qué tratamientos deben representarse.

```python
experimento.graficar(
    modo="seleccion",
    incluir_ids=[
        3,
        8,
        15
    ]
)
```

---

# Selección de tratamientos

ODPlate permite seleccionar tratamientos mediante diversos mecanismos.

## Por grupos

```python
experimento.graficar(
    grupos=[
        "Aceites esenciales"
    ]
)
```

---

## Por aceite

```python
experimento.graficar(
    aceites=[
        "Orégano"
    ]
)
```

---

## Por identificadores

```python
experimento.graficar(
    incluir_ids=[
        1,
        2,
        7
    ]
)
```

---

## Excluyendo tratamientos

```python
experimento.graficar(
    excluir_ids=[
        10,
        11
    ]
)
```

---

# Controles

Los controles pueden mostrarse automáticamente.

```python
experimento.graficar(
    mostrar_control=True
)
```

También pueden ocultarse.

```python
experimento.graficar(
    mostrar_control=False
)
```

Cuando existen varios controles, es posible indicar cuáles utilizar.

```python
experimento.graficar(
    controles_ids=[
        1,
        3
    ]
)
```

---

# Normalización

Las figuras pueden construirse utilizando cualquiera de las estrategias de normalización implementadas por la biblioteca.

```python
experimento.graficar(
    normalizacion="delta"
)
```

o

```python
experimento.graficar(
    normalizacion="control"
)
```

La normalización utilizada en las figuras es independiente de la utilizada durante el cálculo de métricas.

---

# Representación del error experimental

ODPlate permite representar la incertidumbre mediante distintos mecanismos.

## Desviación estándar

```python
experimento.graficar(
    mostrar_error="std"
)
```

---

## Error estándar

```python
experimento.graficar(
    mostrar_error="sem"
)
```

---

## Sin barras de error

```python
experimento.graficar(
    mostrar_error=None
)
```

---

# Bandas de confianza

Las bandas coloreadas pueden activarse mediante:

```python
experimento.graficar(
    mostrar_banda=True
)
```

o desactivarse:

```python
experimento.graficar(
    mostrar_banda=False
)
```

Cuando las bandas están activadas, ODPlate utiliza automáticamente la medida de variabilidad seleccionada (`std` o `sem`).

---

# Tamaño de la figura

```python
experimento.graficar(
    figsize=(14,8)
)
```

---

# Título

```python
experimento.graficar(
    titulo="Actividad antimicrobiana"
)
```

---

# Etiqueta del eje Y

```python
experimento.graficar(
    eje_y="Absorbancia (OD600)"
)
```

---

# Personalización de las leyendas

Las leyendas pueden definirse mediante un diccionario.

```python
experimento.graficar(

    leyendas={

        3: "Orégano 150 μg/mL",

        4: "Orégano 100 μg/mL",

        5: "Orégano 50 μg/mL"

    }

)
```

También pueden generarse automáticamente mediante un formato.

```python
experimento.graficar(

    formato_leyenda="{aceite} ({nombre})"

)
```

Campos disponibles:

* `{id}`
* `{nombre}`
* `{grupo}`
* `{aceite}`
* `{tipo}`
* `{concentracion}`
* `{fila}`
* `{columnas}`

---

# Configuración de la leyenda

La posición y el estilo pueden personalizarse utilizando cualquier parámetro aceptado por Matplotlib.

```python
experimento.graficar(

    leyenda_kwargs={

        "loc":"center left",

        "bbox_to_anchor":(1.02,0.5),

        "fontsize":10,

        "title":"Tratamientos"

    }

)
```

También es posible ocultar completamente la leyenda.

```python
experimento.graficar(

    mostrar_leyenda=False

)
```

---

# Guardar figuras

Las figuras pueden almacenarse automáticamente.

```python
experimento.graficar(

    guardar_en="Resultados/Figuras"

)
```

Si la carpeta no existe, ODPlate la crea automáticamente.

---

# Mostrar figuras

```python
experimento.graficar(

    mostrar=True

)
```

o bien

```python
experimento.graficar(

    mostrar=False

)
```

Esto resulta útil cuando únicamente se desea generar archivos sin mostrarlos en pantalla.

---

# Flujo recomendado

```python
experimento.procesar()

experimento.calcular_todo()

experimento.graficar(

    modo="grupos",

    mostrar_control=True,

    mostrar_error="std",

    mostrar_banda=True,

    guardar_en="Resultados/Figuras"

)
```

Esta configuración constituye la forma recomendada de generar las figuras para la mayoría de los experimentos.

# Método `generar_reporte()`

Una vez finalizado el análisis del experimento, ODPlate permite exportar automáticamente todos los resultados mediante el método `generar_reporte()`.

Este método reúne en un único punto toda la información generada durante el procesamiento y produce un conjunto organizado de archivos listos para su análisis, distribución o inclusión en publicaciones científicas.

Dependiendo de los formatos seleccionados, ODPlate puede generar:

* Reportes en Excel.
* Archivos CSV.
* Reportes en Microsoft Word.
* Reportes HTML.
* Figuras.
* Matrices procesadas.
* Series experimentales.
* Tablas resumen.
* Rankings.
* Modelos ajustados.

La estructura de salida está diseñada para que todos los resultados del experimento queden organizados automáticamente dentro de una misma carpeta.

---

# Sintaxis

```python
salidas = experimento.generar_reporte(
    carpeta,
    formatos=("xlsx", "csv", "docx", "html"),
    titulo="Reporte del experimento",
    sobrescribir=True
)
```

---

# Parámetros

## `carpeta`

**Tipo**

```python
str | Path
```

Ruta donde se almacenarán todos los archivos generados.

Ejemplo:

```python
experimento.generar_reporte(
    carpeta="Resultados"
)
```

Si la carpeta no existe, ODPlate la crea automáticamente.

También puede utilizarse una ruta absoluta.

```python
experimento.generar_reporte(
    carpeta="/home/miguel/Resultados"
)
```

---

## `formatos`

**Tipo**

```python
tuple | list
```

Indica los formatos que deben generarse.

Puede contener uno o varios de los siguientes valores:

| Formato  | Descripción      |
| -------- | ---------------- |
| `"xlsx"` | Reporte de Excel |
| `"csv"`  | Archivos CSV     |
| `"docx"` | Reporte Word     |
| `"html"` | Reporte HTML     |

Ejemplo:

```python
experimento.generar_reporte(

    carpeta="Resultados",

    formatos=("xlsx",)

)
```

Genera únicamente el archivo Excel.

---

También pueden solicitarse varios formatos simultáneamente.

```python
experimento.generar_reporte(

    carpeta="Resultados",

    formatos=(

        "xlsx",

        "csv",

        "docx"

    )

)
```

Esta es la configuración recomendada.

---

## `titulo`

**Tipo**

```python
str
```

Título que aparecerá en los reportes.

Ejemplo:

```python
experimento.generar_reporte(

    carpeta="Resultados",

    titulo="Actividad antimicrobiana"

)
```

Si no se especifica, ODPlate utilizará un título por defecto.

---

## `sobrescribir`

**Tipo**

```python
bool
```

Indica si los archivos existentes deben reemplazarse.

```python
experimento.generar_reporte(

    carpeta="Resultados",

    sobrescribir=True

)
```

---

# ¿Qué hace internamente este método?

Cuando se ejecuta `generar_reporte()`, la biblioteca recopila toda la información almacenada dentro del objeto `ExperimentoOD`.

No realiza nuevos cálculos.

Simplemente organiza y exporta los resultados previamente obtenidos durante las etapas anteriores.

Conceptualmente, el flujo es el siguiente:

```text
Experimento
      │
      ▼
Configuración
      │
      ▼
Series
      │
      ▼
Matrices
      │
      ▼
Métricas
      │
      ▼
Modelos
      │
      ▼
Ranking
      │
      ▼
Exportación
```

Esto garantiza que todos los archivos generados sean completamente consistentes entre sí.

---

# Archivos generados

Dependiendo de la configuración seleccionada, la carpeta de salida puede contener una estructura similar a la siguiente:

```text
Resultados/

│

├── Reporte.xlsx

├── Reporte.docx

├── Reporte.html

├── ranking.csv

├── metricas.csv

├── modelos.csv

├── Figuras/

│      ├── Grupo_A.png

│      ├── Grupo_B.png

│      └── ...

│

├── Matrices/

│      ├── matrices_promedio.xlsx

│      ├── matrices_series.xlsx

│      └── ...

│

└── Series/

       ├── serie_001.csv

       ├── serie_002.csv

       └── ...
```

La estructura exacta dependerá de las opciones utilizadas y de las funcionalidades disponibles en la versión instalada de ODPlate.

---

# ¿Qué información contienen los reportes?

Los reportes pueden incluir, entre otros elementos:

* Información general del experimento.
* Configuración utilizada.
* Tratamientos y controles.
* Grupos experimentales.
* Matrices procesadas.
* Series experimentales.
* Métricas calculadas.
* Modelos ajustados.
* Rankings.
* Figuras generadas.
* Resumen estadístico.

Toda esta información se obtiene directamente del estado interno del experimento.

---

# Valor de retorno

El método devuelve una colección con las rutas de los archivos generados.

```python
salidas = experimento.generar_reporte(
    carpeta="Resultados"
)
```

Esto permite utilizar posteriormente dichas rutas para integrarlas en otros sistemas o realizar procesamiento adicional.

Por ejemplo:

```python
for archivo in salidas:

    print(archivo)
```

---

# Ejemplo mínimo

```python
experimento.generar_reporte(
    carpeta="Resultados"
)
```

---

# Generar únicamente Excel

```python
experimento.generar_reporte(

    carpeta="Resultados",

    formatos=("xlsx",)

)
```

---

# Generar únicamente Word

```python
experimento.generar_reporte(

    carpeta="Resultados",

    formatos=("docx",)

)
```

---

# Generar todos los formatos

```python
experimento.generar_reporte(

    carpeta="Resultados",

    formatos=(

        "xlsx",

        "csv",

        "docx",

        "html"

    )

)
```

Esta es la configuración recomendada para conservar una copia completa del análisis.

---

# Flujo recomendado

```python
experimento.cargar_resultados(
    ruta="Datos",
    nombre_blanco="Blanco"
)

experimento.procesar()

experimento.calcular_todo()

experimento.graficar(
    guardar_en="Resultados/Figuras"
)

experimento.generar_reporte(

    carpeta="Resultados",

    formatos=(

        "xlsx",

        "csv",

        "docx",

        "html"

    ),

    titulo="Actividad antimicrobiana"

)
```

Con estas instrucciones se obtiene un conjunto completo de archivos que documentan todo el experimento.

---

# Buenas prácticas

Se recomienda:

* generar el reporte únicamente cuando el análisis haya finalizado;
* conservar la carpeta de salida junto con los datos originales;
* utilizar títulos descriptivos para facilitar la identificación de los experimentos;
* evitar modificar manualmente los archivos generados.

---

# Errores comunes

## Ejecutar el método antes de procesar el experimento

Si aún no existen matrices procesadas, métricas o modelos, el reporte contendrá únicamente la información disponible.

Se recomienda completar primero todo el flujo de análisis.

---

## Utilizar un formato no soportado

Si se especifica un formato inexistente, ODPlate generará una excepción indicando los formatos disponibles.

---

## Sobrescribir accidentalmente resultados anteriores

Cuando se trabaja con múltiples experimentos, se recomienda utilizar carpetas independientes para evitar reemplazar archivos previamente generados.
# Interpretación de los resultados

ODPlate automatiza gran parte del procesamiento experimental; sin embargo, la interpretación de los resultados sigue siendo responsabilidad del investigador.

Esta sección describe el significado de los principales productos generados por la biblioteca y proporciona recomendaciones para su correcta interpretación.

---

# Matrices procesadas

Después de ejecutar:

```python
experimento.procesar()
```

ODPlate genera un conjunto de matrices procesadas para cada tiempo experimental.

Estas matrices representan la información resumida de las réplicas técnicas y constituyen la base de todos los análisis posteriores.

Generalmente, para cada tiempo experimental se generan:

* Matriz de medias.
* Matriz de desviaciones estándar.
* Matriz de errores estándar.
* Matriz del número de réplicas.

---

# Matriz de medias

La matriz de medias contiene el promedio de cada submatriz definida durante el diseño experimental.

Por ejemplo, si una placa de 96 pozos fue dividida utilizando submatrices de tres columnas, cada valor de la matriz corresponde al promedio de esas tres mediciones.

Conceptualmente:

```text
A1  A2  A3
```

se transforma en

```text
Promedio(A1,A2,A3)
```

Estas matrices representan la mejor estimación del comportamiento observado para cada tratamiento.

En la mayoría de los análisis posteriores únicamente se utilizan estas medias.

---

# Matriz de desviación estándar

Cada promedio experimental se acompaña de su desviación estándar.

La desviación estándar cuantifica la variabilidad existente entre las réplicas técnicas.

Valores pequeños indican una buena reproducibilidad experimental.

Valores elevados pueden indicar:

* alta variabilidad biológica;
* errores de pipeteo;
* problemas instrumentales;
* contaminación;
* diferencias entre réplicas.

Una desviación estándar elevada no implica necesariamente que el experimento sea incorrecto, pero sí merece una revisión cuidadosa.

---

# Error estándar

El error estándar estima la incertidumbre asociada a la media.

Mientras que la desviación estándar describe la dispersión de las observaciones, el error estándar describe la precisión con la que se ha estimado el promedio.

En general:

* desviación estándar → variabilidad experimental;
* error estándar → precisión de la media.

ODPlate puede utilizar cualquiera de estas dos medidas para construir barras de error o bandas de confianza en las figuras.

---

# Series experimentales

Las series representan la evolución temporal de cada tratamiento.

Cada punto de la serie corresponde a una matriz procesada en un tiempo determinado.

Por ejemplo:

```text
Tiempo      OD

0           0.05

1           0.18

2           0.46

3           0.91

4           1.12
```

Estas series constituyen la materia prima para:

* ajuste de modelos;
* cálculo de métricas;
* construcción de figuras;
* comparación entre tratamientos.

---

# Curvas de crecimiento

En experimentos microbiológicos, las series suelen representarse mediante curvas de crecimiento.

Generalmente pueden distinguirse cuatro fases:

```text
Adaptación
      │
      ▼
Crecimiento exponencial
      │
      ▼
Fase estacionaria
      │
      ▼
Declive
```

La forma de la curva proporciona información importante sobre el efecto producido por cada tratamiento.

---

# Comparación con el control

Cuando existe un control experimental, éste constituye el punto de referencia para interpretar el comportamiento del resto de los tratamientos.

Algunas observaciones típicas son:

* curvas similares al control indican ausencia de efecto;
* curvas por debajo del control indican inhibición;
* curvas por encima del control pueden indicar estimulación del crecimiento.

La magnitud de estas diferencias dependerá del tipo de experimento realizado.

---

# Métricas experimentales

ODPlate calcula automáticamente diversas métricas para resumir cuantitativamente el comportamiento de cada tratamiento.

Cada métrica responde a una pregunta diferente.

Por ejemplo:

* ¿Cuál alcanzó la mayor absorbancia?
* ¿Cuál creció más lentamente?
* ¿Cuál presentó mayor inhibición?
* ¿Cuál tuvo el área bajo la curva más pequeña?
* ¿Cuál alcanzó antes la fase estacionaria?

Por esta razón, no existe una única métrica universalmente mejor.

La elección depende del objetivo biológico del estudio.

---

# Modelos matemáticos

Cuando se ajustan modelos de crecimiento, la biblioteca estima automáticamente los parámetros que mejor describen las curvas experimentales.

Estos parámetros permiten:

* comparar tratamientos;
* estimar tasas de crecimiento;
* calcular tiempos característicos;
* realizar predicciones.

En general, un buen modelo debe reproducir adecuadamente la forma observada de la curva sin introducir oscilaciones artificiales.

---

# Ranking de tratamientos

El sistema de ranking de ODPlate ordena automáticamente los tratamientos utilizando un criterio definido por el usuario.

El mejor tratamiento no siempre será el que produzca la mayor absorbancia.

Por ejemplo:

En un experimento de actividad antimicrobiana normalmente interesa minimizar el crecimiento bacteriano.

En cambio, en un experimento de optimización de cultivos podría buscarse exactamente lo contrario.

Por esta razón, ODPlate permite definir funciones de evaluación completamente personalizadas.

---

# Interpretación de las gráficas

Las figuras generadas por la biblioteca muestran simultáneamente:

* evolución temporal;
* variabilidad experimental;
* comparación entre tratamientos;
* comparación con controles.

Al interpretar una figura conviene prestar atención a:

* tendencia general de la curva;
* diferencias respecto al control;
* tamaño de las barras de error;
* solapamiento entre tratamientos;
* comportamiento durante la fase exponencial;
* comportamiento en la fase estacionaria.

Nunca debe interpretarse únicamente el valor final de una curva.

En muchos experimentos la dinámica temporal contiene información mucho más relevante que la absorbancia final.

---

# Exportación de matrices

ODPlate permite exportar todas las matrices procesadas.

Estas tablas resultan especialmente útiles para:

* verificar el procesamiento realizado;
* realizar análisis estadísticos externos;
* compartir resultados con colaboradores;
* incorporar datos suplementarios en publicaciones científicas.

Cada valor exportado corresponde exactamente al utilizado durante el resto del análisis.

Esto garantiza la consistencia entre las tablas, las métricas y las figuras.

---

# Recomendaciones generales

Para obtener resultados confiables se recomienda:

* revisar siempre las matrices procesadas antes de comenzar el análisis;
* inspeccionar las desviaciones estándar para detectar posibles anomalías;
* comparar todas las curvas con sus respectivos controles;
* interpretar conjuntamente tablas, métricas y figuras;
* conservar los archivos originales del experimento junto con los reportes generados por ODPlate.

---

# Reproducibilidad

Una de las principales ventajas de ODPlate es que todos los resultados pueden reproducirse utilizando:

* el mismo archivo de configuración;
* los mismos archivos de absorbancia;
* los mismos parámetros de procesamiento.

Esto garantiza que cualquier investigador pueda repetir exactamente el análisis realizado originalmente.

La reproducibilidad constituye uno de los principios fundamentales sobre los que fue desarrollada la biblioteca.
# Arquitectura interna de ODPlate

ODPlate ha sido desarrollada siguiendo una arquitectura modular cuyo objetivo es facilitar la reutilización del código, la incorporación de nuevas funcionalidades y el mantenimiento a largo plazo.

Cada módulo de la biblioteca tiene una responsabilidad claramente definida y puede utilizarse de forma independiente o como parte del flujo completo de análisis.

---

# Visión general

La siguiente figura conceptual resume la organización de la biblioteca.

```text id="njlwm7"
                   Usuario
                       │
                       ▼
               ExperimentoOD
                       │
 ┌─────────────────────┼─────────────────────┐
 │                     │                     │
 ▼                     ▼                     ▼
Configuración      Procesamiento        Visualización
 │                     │                     │
 ▼                     ▼                     ▼
PlateDesigner     Processing         Plotting
 │                     │                     │
 ▼                     ▼                     ▼
Configuración      Series          Figuras
 │                     │
 └────────────┬────────┘
              ▼
          Métricas
              │
              ▼
           Modelos
              │
              ▼
           Ranking
              │
              ▼
          Reporting
```

Como puede observarse, la clase `ExperimentoOD` actúa como el punto de integración de todos los módulos.

---

# Organización del paquete

La estructura principal del proyecto es la siguiente:

```text id="7w50w5"
odplate/

│

├── config.py

├── designer.py

├── experiment.py

├── exceptions.py

├── plate_designer.py

├── ranking.py

├── results.py

├── series.py

├── statistics.py

│

├── io/

├── metrics/

├── models/

├── plotting/

├── plugins/

├── processing/

└── reporting/
```

Cada módulo tiene una responsabilidad específica, lo que facilita la incorporación de nuevas funcionalidades sin modificar el resto del sistema.

---

# Módulo `experiment`

Este módulo contiene la clase `ExperimentoOD`.

Es el punto de entrada principal de la biblioteca y coordina todas las etapas del análisis.

Entre sus responsabilidades se encuentran:

* administrar la configuración;
* almacenar los datos experimentales;
* coordinar el procesamiento;
* organizar las series;
* calcular métricas;
* ajustar modelos;
* generar gráficas;
* exportar reportes.

En la mayoría de los proyectos, el usuario interactúa exclusivamente con esta clase.

---

# Módulo `designer`

Implementa el diseñador gráfico de placas.

Permite construir visualmente la configuración experimental y exportarla como un archivo JSON compatible con `ExperimentoOD`.

Este módulo constituye el punto de partida recomendado para nuevos experimentos.

---

# Módulo `config`

Contiene las funciones encargadas de:

* cargar configuraciones;
* validar configuraciones;
* guardar configuraciones.

El resto de la biblioteca asume que toda configuración utilizada ha sido previamente validada por este módulo.

---

# Módulo `io`

Este módulo implementa la lectura de los archivos de absorbancia.

Entre sus responsabilidades se encuentran:

* lectura de archivos Excel;
* organización cronológica de los experimentos;
* identificación del blanco;
* construcción de las matrices originales.

Su objetivo es aislar completamente las operaciones de entrada y salida del resto de la biblioteca.

---

# Módulo `processing`

Contiene las funciones responsables del procesamiento estadístico inicial.

Entre ellas:

* corrección por blanco;
* división en submatrices;
* cálculo de medias;
* cálculo de desviaciones estándar;
* cálculo del error estándar;
* organización de las matrices procesadas.

Este módulo constituye la base sobre la que trabajan todos los análisis posteriores.

---

# Módulo `series`

Transforma las matrices procesadas en series experimentales.

Cada serie representa la evolución temporal de un tratamiento específico.

Estas series son utilizadas posteriormente por:

* métricas;
* modelos;
* gráficas;
* reportes.

---

# Módulo `metrics`

Implementa todas las métricas cuantitativas disponibles en la biblioteca.

Cada métrica resume un aspecto particular del comportamiento experimental.

La arquitectura del módulo permite incorporar nuevas métricas sin modificar el resto del sistema.

---

# Módulo `models`

Este módulo contiene los modelos matemáticos utilizados para describir las curvas experimentales.

Dependiendo del tipo de experimento, pueden ajustarse diferentes modelos de crecimiento o de respuesta a dosis.

Cada modelo se implementa como un componente independiente.

Esto facilita la incorporación de nuevos algoritmos de ajuste en futuras versiones.

---

# Módulo `ranking`

Permite clasificar automáticamente los tratamientos utilizando cualquier criterio definido por el usuario.

El sistema no está limitado a un conjunto fijo de métricas.

Por el contrario, cualquier función que produzca una puntuación puede utilizarse como criterio de ranking.

---

# Módulo `plotting`

Genera automáticamente las figuras del experimento.

Este módulo utiliza directamente las series experimentales calculadas previamente.

Entre otras funcionalidades permite:

* representar tratamientos;
* comparar grupos;
* incluir controles;
* mostrar bandas de error;
* personalizar títulos y leyendas;
* guardar figuras automáticamente.

---

# Módulo `reporting`

Centraliza toda la generación de reportes.

Actualmente permite exportar resultados en distintos formatos, incluyendo:

* Excel;
* CSV;
* Word;
* HTML.

Además, organiza automáticamente las carpetas de salida y genera tablas listas para su análisis o publicación.

---

# Módulo `plugins`

ODPlate ha sido diseñada para ser extensible.

Este módulo permite registrar nuevos componentes sin modificar el código fuente de la biblioteca.

Actualmente es posible incorporar:

* nuevas métricas;
* nuevos modelos;
* nuevas funciones de visualización;
* nuevos criterios de ranking.

Esta arquitectura facilita adaptar la biblioteca a distintos dominios experimentales.

---

# Módulo `results`

Contiene las clases utilizadas para almacenar los resultados producidos durante el análisis.

Estas clases proporcionan una estructura homogénea para intercambiar información entre los distintos módulos.

---

# Módulo `exceptions`

Define las excepciones específicas de la biblioteca.

Utilizar excepciones propias permite que los errores sean mucho más descriptivos y facilita su manejo dentro de aplicaciones desarrolladas por terceros.

---

# Dependencias entre módulos

La arquitectura de ODPlate evita dependencias circulares.

Conceptualmente, el flujo entre módulos puede representarse de la siguiente manera:

```text id="gr84hc"
Config
   │
   ▼
Designer
   │
   ▼
Experiment
   │
   ▼
IO
   │
   ▼
Processing
   │
   ▼
Series
   │
   ├────────► Metrics
   │               │
   │               ▼
   │           Ranking
   │
   ├────────► Models
   │
   ├────────► Plotting
   │
   └────────► Reporting
```

Cada módulo conoce únicamente la información estrictamente necesaria para realizar su tarea, lo que facilita el mantenimiento del proyecto y reduce el acoplamiento entre componentes.

---

# Ventajas de esta arquitectura

La organización modular de ODPlate proporciona numerosas ventajas:

* Código más fácil de mantener.
* Mayor reutilización de componentes.
* Incorporación sencilla de nuevas funcionalidades.
* Posibilidad de utilizar únicamente los módulos necesarios.
* Facilidad para realizar pruebas unitarias.
* Mayor claridad en la organización del proyecto.
* Mejor escalabilidad para futuras versiones.

Esta arquitectura constituye uno de los pilares fundamentales sobre los que se ha construido ODPlate y permite que la biblioteca evolucione sin comprometer la compatibilidad con proyectos existentes.

# Sistema de Plugins

Uno de los principios fundamentales sobre los que fue desarrollada ODPlate es la **extensibilidad**.

La biblioteca ha sido diseñada para permitir que investigadores y desarrolladores incorporen nuevas funcionalidades sin modificar el código fuente del proyecto.

Para ello, ODPlate implementa un sistema de **plugins**, mediante el cual es posible registrar nuevos componentes que serán reconocidos automáticamente por la biblioteca.

Actualmente pueden añadirse:

* Nuevas métricas.
* Nuevos modelos matemáticos.
* Nuevos criterios de ranking.
* Nuevos tipos de gráficas.

Esta arquitectura convierte a ODPlate en una plataforma extensible, permitiendo adaptar la biblioteca a distintos dominios experimentales y nuevas líneas de investigación.

---

# Filosofía

El núcleo de ODPlate intenta mantenerse lo más pequeño y estable posible.

Las funcionalidades específicas deben implementarse como componentes independientes registrados dinámicamente.

Esta estrategia presenta varias ventajas:

* No es necesario modificar el código de la biblioteca.
* Las actualizaciones son más sencillas.
* Los nuevos algoritmos pueden compartirse fácilmente.
* Distintos laboratorios pueden desarrollar sus propias extensiones.
* Se mantiene la compatibilidad con versiones futuras.

---

# Registro de componentes

Todos los plugins siguen el mismo patrón.

Primero se implementa una función o clase y posteriormente se registra dentro de la biblioteca.

Conceptualmente:

```text
Crear algoritmo
        │
        ▼
Registrar plugin
        │
        ▼
Utilizar normalmente desde ExperimentoOD
```

Una vez registrado, el nuevo componente se comporta exactamente igual que los componentes nativos de ODPlate.

---

# Registrar una nueva métrica

Las métricas permiten resumir cuantitativamente el comportamiento de una serie experimental.

Una nueva métrica puede implementarse como una función de Python.

Por ejemplo:

```python
def indice_personalizado(serie):

    return ...
```

Posteriormente se registra mediante:

```python
from odplate import registrar_metrica

registrar_metrica(
    nombre="IndicePersonalizado",
    funcion=indice_personalizado
)
```

A partir de ese momento la métrica podrá utilizarse igual que cualquier otra métrica incorporada en la biblioteca.

---

# Buenas prácticas para nuevas métricas

Se recomienda que una métrica:

* reciba una única serie experimental;
* produzca siempre un valor numérico;
* no modifique la serie recibida;
* sea determinista;
* documente claramente las unidades del resultado.

---

# Registrar un nuevo modelo matemático

ODPlate permite incorporar nuevos modelos de ajuste sin modificar el módulo `models`.

Conceptualmente, un modelo debe recibir una serie experimental y devolver el resultado del ajuste correspondiente.

Por ejemplo:

```python
def modelo_personalizado(serie):

    ...

    return resultado
```

El modelo se registra mediante:

```python
from odplate import registrar_modelo

registrar_modelo(
    nombre="MiModelo",
    funcion=modelo_personalizado
)
```

Desde ese momento el modelo podrá seleccionarse igual que los modelos incorporados por defecto.

---

# Recomendaciones para nuevos modelos

Un modelo debería proporcionar, siempre que sea posible:

* parámetros estimados;
* curva ajustada;
* medidas de calidad del ajuste;
* información auxiliar relevante.

Esto permitirá que pueda utilizarse posteriormente en reportes y figuras.

---

# Registrar un nuevo criterio de ranking

El sistema de ranking de ODPlate no depende de un conjunto fijo de reglas.

Cualquier función que asigne una puntuación a una serie experimental puede convertirse en un criterio de ranking.

Ejemplo:

```python
def mejor_crecimiento(resultado):

    return ...
```

Registro:

```python
from odplate import registrar_criterio

registrar_criterio(
    nombre="Mayor crecimiento",
    funcion=mejor_crecimiento
)
```

Posteriormente podrá utilizarse mediante:

```python
experimento.calcular_ranking(
    criterio="Mayor crecimiento"
)
```

---

# Registrar una nueva gráfica

También es posible ampliar el sistema de visualización.

Una función de graficación debe recibir la información necesaria para construir una figura y producir una visualización compatible con Matplotlib.

Registro:

```python
from odplate import registrar_grafica

registrar_grafica(
    nombre="MiGrafica",
    funcion=mi_grafica
)
```

A partir de ese momento la nueva visualización estará disponible para el resto de la biblioteca.

---

# Organización recomendada

Cuando se desarrollan varios plugins, se recomienda organizarlos en un módulo independiente.

Por ejemplo:

```text
mis_plugins/

│

├── metricas.py

├── modelos.py

├── ranking.py

└── graficas.py
```

y registrar todos los componentes al iniciar el proyecto.

```python
import mis_plugins.metricas
import mis_plugins.modelos
import mis_plugins.ranking
import mis_plugins.graficas
```

De esta forma, todo el laboratorio puede reutilizar las mismas extensiones entre distintos experimentos.

---

# Compatibilidad

Los plugins registrados se comportan exactamente igual que los componentes incorporados en ODPlate.

Esto significa que pueden utilizarse en:

* procesamiento;
* métricas;
* modelos;
* rankings;
* reportes;
* figuras.

No existe ninguna diferencia entre un componente nativo y uno registrado dinámicamente.

---

# Recomendaciones de desarrollo

Al desarrollar un plugin se recomienda:

* documentar claramente su funcionamiento;
* validar los datos de entrada;
* lanzar excepciones descriptivas cuando sea necesario;
* evitar modificar directamente los datos originales;
* mantener independencia respecto a otros plugins;
* reutilizar las clases y funciones ya disponibles en ODPlate siempre que sea posible.

---

# Compartiendo plugins

Una de las ventajas de esta arquitectura es que los plugins pueden distribuirse como paquetes independientes.

Esto facilita que distintos grupos de investigación desarrollen sus propias colecciones de:

* métricas específicas;
* modelos para microorganismos particulares;
* algoritmos de clasificación;
* visualizaciones especializadas.

Sin modificar nunca el núcleo de ODPlate.

---

# Futuro del sistema de plugins

El diseño modular de ODPlate permitirá incorporar nuevas categorías de plugins en versiones futuras.

Entre las posibles extensiones se encuentran:

* nuevos formatos de exportación;
* lectores para otros tipos de archivos;
* nuevos métodos de normalización;
* algoritmos de selección automática de modelos;
* nuevas estrategias de procesamiento de datos.

Gracias a esta arquitectura, la evolución de la biblioteca podrá realizarse sin comprometer la compatibilidad con proyectos existentes.
# Preguntas frecuentes (FAQ)

A continuación se presentan algunas de las dudas más comunes al utilizar ODPlate.

---

## ¿Qué versiones de Python son compatibles?

Actualmente ODPlate es compatible con **Python 3.10 o superior**.

Se recomienda utilizar siempre una versión reciente para aprovechar las mejoras de rendimiento y compatibilidad.

---

## ¿Puedo utilizar ODPlate en Google Colab?

Sí.

La biblioteca puede instalarse directamente desde GitHub mediante:

```bash
!pip install "git+https://github.com/miguelcimat/odplate-analysis.git#egg=odplate-analysis[all]"
```

Después de la instalación se recomienda reiniciar el entorno de ejecución.

---

## ¿Es necesario utilizar el diseñador de placas?

No.

El diseñador es la forma recomendada de construir la configuración experimental, pero también es posible crearla manualmente mediante un diccionario de Python.

---

## ¿Puedo reutilizar la misma configuración para varios experimentos?

Sí.

Siempre que todos los experimentos compartan el mismo diseño experimental, basta con reutilizar el mismo archivo JSON.

---

## ¿ODPlate modifica los archivos originales?

No.

Los archivos de absorbancia nunca son modificados.

Todas las operaciones se realizan sobre estructuras internas generadas por la biblioteca.

---

## ¿Puedo analizar únicamente una parte del experimento?

Sí.

La mayoría de los métodos permiten seleccionar:

* grupos específicos;
* tratamientos concretos;
* controles;
* identificadores individuales.

---

## ¿Es posible agregar nuevas métricas?

Sí.

ODPlate dispone de un sistema de plugins que permite incorporar nuevas métricas sin modificar el núcleo de la biblioteca.

---

## ¿Puedo implementar mis propios modelos matemáticos?

Sí.

Los modelos pueden registrarse dinámicamente mediante el sistema de plugins.

---

## ¿Qué formatos de salida soporta la biblioteca?

Actualmente pueden generarse reportes en:

* Excel
* CSV
* Microsoft Word
* HTML

Además de figuras y tablas auxiliares.

---

## ¿Puedo utilizar únicamente algunos módulos?

Sí.

Aunque la forma recomendada consiste en trabajar mediante `ExperimentoOD`, todos los módulos pueden utilizarse de manera independiente.

---

# Ejemplos completos

En la carpeta `examples/` del repositorio se incluyen diversos ejemplos de uso que ilustran los flujos de trabajo más habituales.

Entre ellos:

* análisis básico de un experimento;
* utilización del diseñador de placas;
* generación automática de reportes;
* personalización de gráficas;
* exportación de matrices procesadas;
* cálculo de rankings personalizados.

Se recomienda revisar estos ejemplos antes de desarrollar aplicaciones propias.

---

# Buenas prácticas

Para obtener el máximo provecho de ODPlate se recomienda:

* conservar siempre los archivos originales del experimento;
* almacenar el archivo JSON junto con los datos experimentales;
* utilizar nombres descriptivos para tratamientos y grupos;
* revisar las matrices procesadas antes de interpretar los resultados;
* documentar claramente los parámetros utilizados durante el análisis;
* conservar todos los reportes generados junto con los datos originales.

Estas recomendaciones facilitan la reproducibilidad y el intercambio de resultados entre distintos investigadores.

---

# Cómo contribuir

Las contribuciones son bienvenidas.

Si desea colaborar con el desarrollo de ODPlate puede hacerlo de diversas maneras:

* reportando errores;
* proponiendo nuevas funcionalidades;
* mejorando la documentación;
* implementando nuevas métricas;
* incorporando nuevos modelos matemáticos;
* desarrollando nuevos criterios de ranking;
* creando nuevos ejemplos de uso.

Antes de realizar una contribución importante se recomienda abrir un *Issue* para discutir la propuesta.

---

# Reporte de errores

Si encuentra algún problema durante el uso de la biblioteca, por favor incluya la siguiente información al crear un reporte:

* versión de ODPlate;
* versión de Python;
* sistema operativo;
* mensaje completo del error;
* fragmento mínimo de código para reproducir el problema;
* archivos de configuración utilizados (cuando sea posible).

Esto facilitará la reproducción y corrección del error.

---

# Versionado

ODPlate sigue el esquema de versionado semántico (**Semantic Versioning**).

Las versiones se identifican mediante el formato:

```text
MAJOR.MINOR.PATCH
```

donde:

* **MAJOR** indica cambios incompatibles con versiones anteriores.
* **MINOR** incorpora nuevas funcionalidades manteniendo la compatibilidad.
* **PATCH** corrige errores sin modificar la interfaz pública.

---

# Cómo citar ODPlate

Si ODPlate contribuyó al análisis realizado en una publicación científica, por favor cite la biblioteca.

Mientras se publica un artículo específico de descripción del software, puede citarse de la siguiente manera:

```text
Álvarez-Carmona, M. Á.
ODPlate: A Python Library for Optical Density Plate Analysis.
GitHub Repository.
https://github.com/miguelcimat/odplate-analysis
```

También se recomienda citar la versión exacta utilizada durante el análisis.

---

## BibTeX

```bibtex
@software{AlvarezCarmona_ODPlate,
  author = {Miguel Ángel Álvarez-Carmona},
  title = {ODPlate: A Python Library for Optical Density Plate Analysis},
  year = {2026},
  url = {https://github.com/miguelcimat/odplate-analysis},
  version = {1.0.3}
}
```

---

# Licencia

ODPlate se distribuye bajo la licencia especificada en el archivo `LICENSE` incluido en el repositorio.

Consulte dicho archivo para conocer las condiciones de uso, modificación y distribución del software.

---

# Contacto

**Dr. Miguel Ángel Álvarez-Carmona**

Centro de Investigación en Matemáticas (CIMAT), Unidad Monterrey

Investigadoras e Investigadores por México — SECIHTI

Correo electrónico: *(agregar dirección de contacto)*

GitHub:

https://github.com/miguelcimat

---

# Agradecimientos

El desarrollo de ODPlate ha sido posible gracias al trabajo de investigadores, estudiantes y colaboradores que han participado en la validación de la biblioteca y en el diseño de nuevas funcionalidades.

Se agradece especialmente a todos los usuarios que han contribuido mediante sugerencias, pruebas y reportes de errores, los cuales han permitido mejorar continuamente la calidad y robustez del proyecto.

---

# Estado del proyecto

ODPlate es un proyecto en desarrollo activo.

Nuevas funcionalidades, modelos matemáticos, métricas, herramientas de visualización y capacidades de exportación continuarán incorporándose en futuras versiones.

Las sugerencias y contribuciones de la comunidad científica son fundamentales para seguir ampliando las capacidades de la biblioteca.

---

<p align="center">

## Gracias por utilizar ODPlate

**Esperamos que esta biblioteca contribuya a hacer el análisis de experimentos de densidad óptica más reproducible, automatizado y accesible para toda la comunidad científica.**

</p>

