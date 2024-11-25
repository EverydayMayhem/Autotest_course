def segment(first_point, second_point):
    """Сумма всех координат точек
    :param first_point: координаты первой точки
    :param second_point: координаты второй точки
    :return: текст исключения наоборот или сумму всех координат
    """
    summ = 0
    summ_i = 0
    summ_j = 0
    try:
        # сумма первых координат
        for i in range(len(first_point)):
            summ_i = first_point[i] + summ_i
        # сумма вторых координат
        for j in range(len(second_point)):
            summ_j = summ_j + second_point[j]
        # сумма всех координат
        summ = summ_j + summ_i
    except Exception as e:
        # получаем текст ошибки через str()
        err_str = str(e)
        # срезом получаем обратную строку
        err_str = err_str[::-1]
        return err_str
    else:
        return summ
    return
