def move_zeros(lst):
    """Перемещение нулей
    :param lst: список из цифр
    :return: список из цифр с нулями в конце
    """
    # todo Здесь нужно написать код
    # посчитаем количество нулей в списке
    counter = lst.count(0)

    # создадим список из N нулей, которые потом соединим с урезанным списком
    zeroes = lst.count(0)
    zeroes_list = [0 for i in range(zeroes)]

    # пройдемся по списку и удалим ровно counter нулей
    while counter != 0:
        lst.remove(0)
        counter -= 1
    lst.extend(zeroes_list)
    return lst
