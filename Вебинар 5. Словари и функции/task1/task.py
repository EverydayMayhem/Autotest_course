def letter_stat(our_str):
    """Буквенная статистика
    :param our_str: строка
    :return: словарь со статистикой по буквам
    """
    # todo Здесь нужно написать код
    # решаем через генератор словаря и функцию count()
    dict = {item: our_str.count(item) for item in our_str}
    return dict

