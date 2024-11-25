def modification(lst):
    """Изменение списка
    :param lst: список
    :return: преобразованный список
    """
    # todo Здесь нужно написать код
    last = lst[-1]
    first = lst[0]
    lst[0] = last
    lst[-1] = first
    return lst
