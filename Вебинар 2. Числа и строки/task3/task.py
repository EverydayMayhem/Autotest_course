def string_concatenation(str1, str2):
    """Объединение строк
    :param str1: первая строка
    :param str2: вторая строка
    :return: преобразованную строку
    """

    # todo Здесь нужно написать код
    # result_string = str2[:2] + str1[2:] + " " + str1[0:2] + str2[2:]
    result_string = str1.replace(str1[:2], str2[:2], 1) + " " + str2.replace(str2[:2], str1[:2], 1)
    return result_string
