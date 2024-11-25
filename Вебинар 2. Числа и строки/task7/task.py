def minimum_length_slice(first_string, second_string):
    """Срез минимальной длины
    :param first_string: первая строка
    :param second_string: вторая строка
    :return: min_slice срез минимальной длины строки second_string
    """
    # т.к. все символы первой строки неповторяющиеся, а вторая строка точно содержит в себе символы первой, то
    # заменим во второй строке все символы первой на одинаковый - первый символ первой строки
    # потом найдем индекс первого и последнего вхождения этого символа во второй строке и сделаем срез

    # tempo_string = second_string.replace(first_string[1],first_string[0]).replace(first_string[2],first_string[0])
    # lindex = tempo_string.find(first_string[0])
    # rindex = tempo_string.rfind(first_string[0])
    # min_slice = second_string[lindex:rindex+1]

    # через мин-макс

    min_index = min(second_string.find(first_string[0]), second_string.find(first_string[1]), second_string.find(first_string[2]))
    max_index = max(second_string.find(first_string[0]), second_string.find(first_string[1]), second_string.find(first_string[2]))
    min_slice = second_string[min_index:max_index+1]
    return min_slice
