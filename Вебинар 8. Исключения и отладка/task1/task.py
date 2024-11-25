def treatment_sum(our_tuple):
    """Обработка суммы элементов кортежа
    :param our_tuple: кортеж
    :return: сумму элементов кортежа
    """
    # todo Здесь нужно написать код
    tuple_sum = 0
    exception1 = 'Нельзя сложить эти данные'
    if len(our_tuple) == 2:
        try:
            if type(our_tuple[0]) == int:
                for i in range(len(our_tuple)):
                    tuple_sum += our_tuple[i]
            else:
                tuple_sum = ''
                for i in range(len(our_tuple)):
                    tuple_sum += our_tuple[i]
        except TypeError:
            return exception1
        else:
            return tuple_sum
    elif len(our_tuple) > 2:
        raise Exception('Много данных')
    else:
        tuple_sum = 'Недостаточно данных'
    return tuple_sum

treatment_sum((1,))