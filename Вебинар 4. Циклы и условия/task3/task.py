def sum_digits(num):
    """Нахождение суммы цифр числа
    :param num: число
    :return: сумма цифр числа
    """
    # todo Здесь нужно написать код
    summ = 0
    num_str = str(num)
    for i in range(len(num_str)):
        temp = int(num_str[i])
        summ += temp
    return summ

