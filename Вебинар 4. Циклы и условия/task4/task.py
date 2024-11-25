def multiplication_chain(num):
    """Цепочка умножений
    :param num: положительное число
    :return: количество перемножений
    """
    num_str = str(num)
    num_array = []
    # генерируем список из цифр входного числа
    for digit in range(len(num_str)):
        num_array.append(int(num_str[digit]))

    multi_result = 1  # переменная для хранения результата умножения цифр числа
    multi_chain = 0  # наш результат - количество циклов умножения

    # для начала оборачиваем наш код в while, будем находиться в нем, пока длина числа > 1 (двузначное число)
    while len(num_array) > 1:

        # получаем результат умножения всех цифр числа
        for i in num_array:
            multi_result *= i
        multi_result_str = str(multi_result)

        # чистим список
        num_array.clear()
        
        # заполняем новыми цифрами из результата умножения
        for digit in range(len(multi_result_str)):
            num_array.append(int(multi_result_str[digit]))

        # чистим результат умножения и плюсуем конечный счетчик
        multi_result = 1
        multi_chain += 1
    return multi_chain
