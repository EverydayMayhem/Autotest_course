def josephus_task(num_people, kill_num):
    """Задача Иосифа Флавия
    :param num_people: количество воинов
    :param kill_num: номер воина
    :return: номер последнего оставшегося воина
    """
    # генерируем список
    people_list = [i + 1 for i in range(num_people)]

    # с помощью while будем проходить по списку людей, пока там не останется один человек
    while len(people_list) > 1:
        # смотрим по остатку от деления, чтобы определить позицию (position), с которой будем удалять человека
        # если остаток больше нуля, значит удаляем человека и
        # склеиваем правый (после position) кусок списка с левым (до position), как бы закольцовываем список (делаем круг)
        # если равен нулю, значит просто удаляем последний элемент списка
        if kill_num % len(people_list) != 0:
            position = (kill_num % len(people_list))
            people_list.pop(position - 1)
            people_list = people_list[position - 1::] + people_list[:position - 1]

        else:
            people_list.pop(-1)

    return people_list[0]