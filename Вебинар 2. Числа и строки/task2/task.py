import math


def quadratic(b, c):
    """Решение квадратного уравнения
    :param b: коэффициент b
    :param c: коэффициент c
    :return: корни квадратного уравнения
    """
    # todo Здесь нужно написать код
    discriminant = round((b*b - 4*c), 2)
    x1 = round(((-b + math.sqrt(discriminant)) / 2), 2)
    x2 = round(((-b - math.sqrt(discriminant)) / 2), 2)
    return x1, x2
