import pytest
from calculadora import soma, subtracao, multiplicacao, divisao, fatorial, potencia


def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0


def test_subtracao():
    assert subtracao(5, 3) == 2
    assert subtracao(0, 5) == -5


def test_multiplicacao():
    assert multiplicacao(2, 3) == 6
    assert multiplicacao(-2, 3) == -6


def test_divisao():
    assert divisao(10, 2) == 5
    assert divisao(5, 2) == 2.5


def test_divisao_erro():
    with pytest.raises(ZeroDivisionError):
        divisao(10, 0)


def test_fatorial():
    assert fatorial(5) == 120
    assert fatorial(0) == 1


def test_fatorial_erro():
    with pytest.raises(ValueError):
        fatorial(-1)


def test_potencia():
    assert potencia(2, 3) == 8
    assert potencia(2, 0) == 1
    assert potencia(2, -1) == 0.5