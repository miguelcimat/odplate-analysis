import numpy as np
import pytest

from odplate import Experimento, ExperimentoOD
from odplate.processing import promediar_submatrices, procesar_matrices
from odplate.metrics import calificacion_inversa, metricas_serie
from odplate.ranking import ranking
from odplate.plotting import graficar
from odplate.config import cargar_configuracion

CONFIG = {
    "filas": 2,
    "columnas": 6,
    "submatriz": 3,
    "control": {"nombre": "Control", "fila": "B", "columnas_originales": [1, 2, 3]},
    "grupos": [{
        "nombre": "G1", "aceite": "A1",
        "series": [
            {"nombre": "Baja", "cantidad": 1, "fila": "A", "columnas_originales": [1, 2, 3]},
            {"nombre": "Alta", "cantidad": 2, "fila": "A", "columnas_originales": [4, 5, 6]},
        ],
    }],
}


def matrices_prueba():
    blanco = np.zeros((2, 6))
    t0 = np.array([[1, 1, 1, 4, 4, 4], [2, 2, 2, 0, 0, 0]], float)
    t1 = np.array([[2, 2, 2, 8, 8, 8], [3, 3, 3, 0, 0, 0]], float)
    return procesar_matrices({"blanco": blanco, 0: t0, 1: t1}, 3)


def test_promedio():
    a = np.arange(24, dtype=float).reshape(2, 12)
    d = promediar_submatrices(a, 3)
    assert d["mean"].shape == (2, 4)
    assert d["mean"][0, 0] == 1


def test_config_antigua_se_normaliza_a_catalogo_unico():
    cfg = cargar_configuracion(CONFIG)
    assert len(cfg["series"]) == 3
    assert {x["tipo"] for x in cfg["series"]} == {"control", "tratamiento"}
    assert all("id" in x for x in cfg["series"])


def test_experimento_expone_series_tipadas():
    exp = ExperimentoOD(CONFIG)
    assert len(exp.series) == 3
    assert len(exp.obtener_series(tipo="control")) == 1
    assert len(exp.obtener_series(tipo="tratamiento")) == 2
    assert isinstance(exp, Experimento)


def test_pipeline():
    b = np.zeros((2, 6))
    crudas = {"blanco": b, 0: np.ones((2, 6)), 1: np.ones((2, 6)) * 2}
    matrices = procesar_matrices(crudas, 3)
    serie = {"fila": "A", "columnas_originales": [1, 2, 3]}
    metricas = metricas_serie(matrices, serie, 3)
    assert metricas["od_final"] == 2
    assert calificacion_inversa(matrices, serie, 3) > 0


def test_ranking_tratamientos_por_defecto():
    tabla = ranking(cargar_configuracion(CONFIG), matrices_prueba(), criterio=calificacion_inversa)
    assert len(tabla) == 2
    assert set(tabla["tipo"]) == {"tratamiento"}
    assert tabla.iloc[0]["nombre"] == "Baja"


def test_ranking_incluye_control_con_tipo_todos():
    tabla = ranking(cargar_configuracion(CONFIG), matrices_prueba(), criterio=calificacion_inversa, tipo="todos")
    assert len(tabla) == 3
    assert "control" in set(tabla["tipo"])
    assert list(tabla.columns) == [
        "posicion", "id", "nombre", "tipo", "grupo", "aceite", "concentracion", "calificacion"
    ]


def test_ranking_solo_control():
    tabla = ranking(cargar_configuracion(CONFIG), matrices_prueba(), criterio="calificacion_inversa", tipo="control")
    assert len(tabla) == 1
    assert tabla.iloc[0]["nombre"] == "Control"


def test_grafica_mejores_exige_criterio():
    with pytest.raises(ValueError, match="requieren un criterio"):
        graficar(cargar_configuracion(CONFIG), matrices_prueba(), modo="mejores", n_mejores=1, mostrar=False)


def test_grafica_ranking_todos_incluye_control_en_tabla():
    resultado = graficar(
        cargar_configuracion(CONFIG), matrices_prueba(), modo="ranking",
        criterio=calificacion_inversa, top=3, tipo="todos",
        mostrar_control=False, mostrar=False,
    )
    assert len(resultado["ranking"]) == 3
    assert "control" in set(resultado["ranking"]["tipo"])


def test_import_publico():
    import odplate
    assert odplate.__version__ == "1.0.4"
    assert callable(odplate.registrar_criterio)
