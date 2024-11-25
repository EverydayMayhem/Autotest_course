import math


def square_calculation(a):
    """Вычисление квадрата
    :param a: сторона квадрата
    :return: периметр квадрата, площадь квадрата и диагональ квадрата
    """
    # a = input ("Введите сторону квадрата: ")
    # a = 10
    perimeter = round((a * 4), 2)
    square = round ((a * a), 2)
    diagonal = round((math.sqrt(a*a + a*a)), 2)
    return perimeter, square, diagonal
