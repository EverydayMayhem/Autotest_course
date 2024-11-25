def max_division_by_3(num):
    """Преобразование числа
    :param num: натуральное число
    :return: другое натуральное число, удовлетворяющее условиям
    """
    # разобъем исходную задачу на 4 маленьких - по условиям генерации

    # Для начала сгенерируем числа по первому условию. Фиксируем все числа, кроме итерируемого, и наполняем список числами

    num_list = [int(i) for i in str(num)]
    # temp_number = int(''.join(str(x) for x in num_list))
    final_number = 0
    final_list = []
    # метод для суммирования цифр внутри
    for digit in range(len(num_list)):
        counter = 9
        num_list = [int(i) for i in str(num)]

        while counter > 0:
            summ = 0

            num_list.pop(digit)
            num_list.insert(digit, counter)
            if (digit == 0) and (counter == 0):
                continue

            # print(num_list)
            for i in num_list:
                summ += int(i)
            print(summ)

            if summ % 3 == 0:
                final_number = ''.join(str(x) for x in num_list)
                final_list.append(final_number)
                print(final_number)
                counter -= 1
                break
            counter -= 1
    if final_list.count(str(num)) > 0:
        final_list.remove(str(num))
    last_number = max(final_list)



    return int(last_number)
