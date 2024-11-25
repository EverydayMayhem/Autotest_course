number = 1
string = 'Hello'


def global_changes():
    """Глобальные переменные
    :return: number, string
    """
    global number
    global string
    number = 5
    string = 'Hello, dear friend'
    return number, string
