
import pytest

from calculadora import (
    sumar,
    restar,
    multiplicar,
    dividir
)


# Pruebas de suma
def test_sumar_positivos():
    assert sumar(2, 3) == 5


def test_sumar_negativos():
    assert sumar(-2, -3) == -5


# Pruebas de resta
def test_restar_positivos():
    assert restar(5, 3) == 2


def test_restar_negativos():
    assert restar(-5, -3) == -2


# Pruebas de multiplicacion
def test_multiplicar_positivos():
    assert multiplicar(3, 4) == 12


def test_multiplicar_negativos():
    assert multiplicar(-3, 4) == -12


# Pruebas de division
def test_dividir_exactamente():
    assert dividir(10, 2) == 5


def test_dividir_decimal():
    assert dividir(7, 2) == 3.5


def test_dividir_entre_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)


def test_dividir_cero_entre_numero():
    assert dividir(0, 5) == 0


# Prueba de validacion de tipos
def test_dividir_con_texto():
    with pytest.raises(TypeError):
        dividir("diez", 2)
