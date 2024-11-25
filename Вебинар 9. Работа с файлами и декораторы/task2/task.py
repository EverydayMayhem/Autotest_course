from pathlib import Path
def three_most_expensive_purchases():
    """Три самые дорогие покупки
    :return: сумму трех самых дорогих покупок
    """
    file_path = "test_file/task_2.txt"
    abs_path = Path(Path.cwd(), file_path)
    purchases_list = [] # список покупок, делаем по разделителю
    summ_list = [] # сумма каждой отдельно взятой покупки
    counter = 0 # бегунок для разбиения покупок
    with open(abs_path, mode='r', encoding='utf-8') as file:
        temp = file.readlines()
        trimmed_list = [s.strip() for s in temp] # убираем символы новой строки, которые есть в считанном файле
        for indexx, line in enumerate(trimmed_list):
            if line == '':
                purchases_list += [trimmed_list[counter:indexx]]
                counter = indexx + 1
    # переводим все в целочисленные значения, проходимся по списку и суммируем покупки
        for i in range(len(purchases_list)):
            summ = 0
            for j in range(len(purchases_list[i])):
                summ += int(purchases_list[i][j])
            summ_list += [summ]
        # сортируем этот список и суммируем первые три элемента
        summ_list.sort(reverse=True)
        most_expensive_purchases = summ_list[0] + summ_list[1] + summ_list[2]

    return most_expensive_purchases
