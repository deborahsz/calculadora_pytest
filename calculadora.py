def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    if b == 0:
        raise ZeroDivisionError("divisao por zero")
    return a / b


def fatorial(n):
    if n < 0:
        raise ValueError("numero negativo")
    if n == 0:
        return 1

    resultado = 1
    for i in range(1, n + 1):
        resultado *= i

    return resultado


def potencia(a, b):
    return a ** b