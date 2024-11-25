def which_triangle(a, b, c):
    """Определение типа треугольника
    :param a: длина стороны
    :param b: длина стороны
    :param c: длина стороны
    :return: тип треугольника
    """
    # todo Здесь нужно написать код

    if a == b == c :
        triangle_type = "Равносторонний"
    elif (a == b) or (b == c) or (c == a):
        triangle_type = "Равнобедренный"
    elif (a < b + c) and (b < a + c) and (c < a + b):
        triangle_type = "Обычный"
    else:
        triangle_type = "Не треугольник"
    return triangle_type

