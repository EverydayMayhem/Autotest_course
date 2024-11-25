class Trigon:
    def __init__(self, *args):
        for arg in args:
            if len(args) != 3:
                raise IndexError(f'Передано {len(args)} аргументов, а ожидается 3')
            elif not isinstance(arg, int):
                raise TypeError('Стороны должны быть числами')
            elif arg <= 0:
                raise ValueError('Стороны должны быть положительными')
        # если три вышеперечисленных ошибки не стрельнули, то проверяем сумму сторон
        if (args[0] > args[1] + args[2]) or (args[1] > args[0] + args[2]) or (args[2] > args[1] + args[0]):
            raise Exception('Не треугольник')

        # todo Здесь нужно написать код


