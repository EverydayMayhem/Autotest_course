def create_phone_number(num_tuple):
    """Создание номера телефона
    :param num_tuple: кортеж из цифр
    :return: строку в виде номера телефона
    """
    # приведем кортеж к строке
    str_index = str(num_tuple)

    # удалим ненужные символы, такие как " ", "(", ")", ","
    str_index = str_index.replace(",", "").replace(")", "").replace("(", "").replace(" ", "")

    # с помощью f-строки запишем номер
    phone_number = f"({str_index[:3]}) {str_index[3:6]}-{str_index[6:]}"

    return phone_number
