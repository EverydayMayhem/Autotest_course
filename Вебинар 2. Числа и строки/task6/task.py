def delete_symbols(string):
    """Удаление символов с нечетными индексами
    :param string: строка
    :return: строку без символов с нечетными индексами исходной строки
    """

    new_string = string[::2] # оставляем только четные
    return new_string
