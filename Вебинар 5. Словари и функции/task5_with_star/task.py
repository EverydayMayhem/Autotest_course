def to_roman(val):
    """Преобразование арабского числа в римское
    :param val: арабское число
    :return: римское число
    """
    result = '' # результат - римское число

    # сначала соберем словарь из римских цифр. Ключом будет арабская цифра, значением - римская
    dict = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

    roman_numbers = list(dict.values()) # в этом списке будут значения
    occurrence_list = [] # а тут будет количество вхождений римских цифр, т.е. сколько тысяч, сотен, десятков и единиц есть в числе

    # идем по ключам нашего словаря, и начиная с левого разряда (тысяча) делаем целочисленное деление исходного числа на ключ.
    # Результат записываем в наш список и уменьшаем исходное число на произведение ключ ** результат деления,
    # т.е на примере 1800: 1800 // 1000 = 1, записываем в список occurance_list = 1, оставшееся число = 1800 - 1000 = 800
    # дальше 800 // 900 = 0, в occurance_list записываем 0, берем следующий ключ = 500, 800 // 500 = 1, записываем в occurance_list = 1,
    # берем следующее число 800 - 500 = 300, 300 // 400 = 0, записываем в occurance_list = 0 и так далее

    for key in dict.keys():
        occurrence = val // key
        val -= key * (val // key)
        occurrence_list.append(occurrence)

    # дальше список вхождений каждого числа и соответсвующая римская цифра записывается в список через генератор
    roman_digits = [[roman_numbers[i], occurrence_list[i]] for i in range(len(roman_numbers))]

    # теперь просто склеиваем строку конкатенацией через умножение количества вхождений на строчную римскую цифру
    for i in range(len(roman_digits)):
        result += roman_digits[i][0] * roman_digits[i][1]

    return result
