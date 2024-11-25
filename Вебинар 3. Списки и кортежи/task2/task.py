def get_list_info(lst):
    """Получение информации о списке
    :param lst: список из чисел
    :return: min_elem, max_elem, sum_list, average
    """
    min_elem = min(lst)
    max_elem = max(lst)
    sum_list = sum(lst)
    average =  round((sum_list / len(lst)), 2)
    # собираем из этого кортеж
    lst = (min_elem, max_elem, sum_list, average)
    return lst
