def memorize(function):
    def wrapper(*args, **kwargs):
        res = function(*args, **kwargs)
        dict1.setdefault(args, function(*args, **kwargs)) # если такого ключа нет, добавим его, если есть - просто вернем значение
        # по ключу, но словарь останется неизменным, что нас устраивает
        return res, dict1
    dict1 = {}
    return wrapper

@memorize
def get_kinetic_energy(weight, speed):
    """Кинетическая энергия
    :param weight: масса
    :param speed: скорость
    :return: кинетическую энергию
    """
    return (weight * speed ** 2)/2