def repeats(our_str):
    """Повторы букв
    :param our_str: строка
    :return: новая строка с повторами букв
    """
    # судя по тематике вебинара, решать надо через словари
    # но мне видится простое решение через срезы
    new_str = ""
    # for i in range(len(our_str)):
    #     new_str += our_str[i] + "_" + str(our_str[:i+1].count(our_str[i]))
    # через словари сделаем так: ключами будет номер элемента строки, значением - кортеж (символ, число вхождений)
    # будем идти по строке и считать текущее количество повторений через срезы
    # затем значения выцепим через dict.values() и распакуем кортежи в нужный для нас вид через форматирование строки
    dict = {}
    for i in range(len(our_str)):
        dict[i] = (our_str[i], our_str[:i+1].count(our_str[i]))

    for j in dict.values():
        new_str += f'{j[0]}_{j[1]}'
    return new_str

repeats("letter")