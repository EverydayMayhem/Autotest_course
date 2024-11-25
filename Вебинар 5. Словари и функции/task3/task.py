def everything_for_your_cat(cats_data):
    """Котики и их владельцы
    :param cats_data: информация о котах и их владельцах
    :return: информация о котах и их владельцах в виде строки
    """
    # todo Здесь нужно написать код
    # т.к. у одного человека может быть несколько котиков, то у одного ключа должно быть несколько значений, например
    # в виде списка. Ключом будет кортеж (Фамилия, Имя) , а значением - список котиков [Кличка, Возраст]
    # будем обращаться к словарю по ключу и добавлять в значение новый список [Кличка, Возраст] через .append()
    # cat_book - словарь, в который занесем данные по владельцам (ключ) и котикам (значение)
    # result - финальная строка
    cat_book = {}
    result = ""
    for i in range(len(cats_data)):
        # нужна проверка на наличие ключа. Если ключ уже есть, то добавим к нему новое значение, если нет -
        # setdefault()
        if cat_book.get((cats_data[i][-2], cats_data[i][-1])) == None:
            cat_book.setdefault((cats_data[i][-2], cats_data[i][-1]), [cats_data[i][0], cats_data[i][1]])
        else:
            cat_book[(cats_data[i][-2], cats_data[i][-1])].append(cats_data[i][0])
            cat_book[(cats_data[i][-2], cats_data[i][-1])].append(cats_data[i][1])

    #   пройдемся по словарю и соберем из него строковые ФИО владельца, и информацию о котиках
    for key, value in cat_book.items():
        owner_name = key[0] + " " + key[1]
        cat_name = ""
        for j in range(len(value)):
            # точку с запятой ставим только после возраста котика, чтобы разделить инфу о разных котиках
            if type(value[j]) == int:
                cat_name += str(value[j]) + "; "
            else:
                cat_name += str(value[j]) + ", "

        cat_name = cat_name[:-2] # убираем последние два символа строки
        result += f"{owner_name}: {cat_name}\n" # собираем в кучу нашу строку
    return result

