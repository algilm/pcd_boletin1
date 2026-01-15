import pytest
from juego_3_en_raya import mostrar_tablero

@pytest.fixture
def tablero_dimension():
    return 3

@pytest.fixture
def movimientos_ambos_jugadores():
    return [{}, {}]

def test_mostrar_tablero(tablero_dimension, movimientos_ambos_jugadores, capsys):
    mostrar_tablero(tablero_dimension, movimientos_ambos_jugadores)
    captured = capsys.readouterr()
    lineas = captured.out.strip().split("\n")
    lineas = [l for l in lineas if l]
    assert len(lineas) == tablero_dimension
    for linea in lineas:
        assert len(linea.replace(' ', '')) == tablero_dimension

from juego_3_en_raya import movimiento_valido

@pytest.fixture
def tablero_dimension():
    return 3

@pytest.fixture
def movimientos_vacios():
    return {}

@pytest.fixture
def movimientos_ocupados():
    return {1: [1]}


def test_movimiento_fuera_tablero(tablero_dimension, movimientos_vacios):
    assert not movimiento_valido(tablero_dimension, -1, 0, movimientos_vacios)
    assert not movimiento_valido(tablero_dimension, 3, 0, movimientos_vacios)

def test_movimiento_casilla_ocupada(tablero_dimension, movimientos_ocupados):
    assert not movimiento_valido(tablero_dimension, 1, 1, movimientos_ocupados)

def test_movimiento_correcto(tablero_dimension, movimientos_vacios):
    assert movimiento_valido(tablero_dimension, 0, 0, movimientos_vacios)

from juego_3_en_raya import jugada_ganadora
@pytest.fixture
def movimientos_no_ganador():
    return {1: [0, 2]}

@pytest.fixture
def movimientos_ganador():
    return {1: [0, 1, 2]}

def test_no_ganador(movimientos_no_ganador):
    assert not jugada_ganadora(movimientos_no_ganador)

def test_ganador(movimientos_ganador):
    assert jugada_ganadora(movimientos_ganador)
