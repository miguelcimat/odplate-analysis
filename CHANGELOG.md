# Changelog

## 1.0.2
- Se corrigió la visualización de PlateDesigner en Google Colab.
- La placa ahora se inserta directamente como GridBox persistente, sin envolverla en Output.
- Se mantiene la misma apariencia, selección, colores, validación, edición y exportación.


## 1.0.0

- Catálogo único de series para tratamientos, controles y referencias.
- Clases `Serie`, `Grupo`, `Experimento` y alias compatible `ExperimentoOD`.
- Migración automática de configuraciones 0.x.
- Ranking y gráficas filtrables con `tipo="tratamiento"`, `"control"` o `"todos"`.
- Tablas de ranking con nombre, tipo, grupo, aceite y concentración.
- Validaciones estrictas de IDs, pozos, filas, columnas y superposiciones.
- Base de caché invalidada al cargar o reprocesar datos.
