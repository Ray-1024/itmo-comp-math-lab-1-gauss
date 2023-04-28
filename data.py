import math

methods = ['Метод прямоугольников', 'Метод трапеций', 'Метод Симпсона']


def f0(x):
    return 4 * (x ** 3) - 2 * (x ** 2) - 7 * x + 30


def f1(x):
    return math.sin(x)


def f2(x):
    return math.floor(x)


names = ['4x^3 - 2x^2 - 7x + 30', 'sin(x)', '[x]']

functions = [f0, f1, f2]
