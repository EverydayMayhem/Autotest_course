def sum_and_multiplication(a, b):
    """Сумма и произведение двух чисел
    :param a: первое число
    :param b: второе число
    :return: сумму и произведение
    """
    # todo Здесь нужно написать код
    # через ф-строки
    a_b_sum = f"{a} + {b} = {a+b}"
    a_b_multi = f"{a}*{b} = {a*b}"

   # колхозный вариант
   # a_b_sum = str(a) +" + " + str(b) + " = " + str(a+b)
   # a_b_multi = str(a) +"*" + str(b) + " = " + str(a*b)
    return a_b_sum, a_b_multi
