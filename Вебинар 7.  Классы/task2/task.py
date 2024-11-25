class PersonInfo:
    def __init__(self, fi, age, *deps):
        self.fi = fi
        self.age = age
        self.deps = deps

    def short_name(self):
        """Краткая запись Фамилия И."""
        # todo Здесь нужно написать код
        shortened_list = self.fi.split()
        shortened_str = self.fi
        shortened = f'{shortened_list[1]} {shortened_str[0]}.'
        return shortened

    def path_deps(self):
        """Путь до подразделения"""
        # todo Здесь нужно написать код
        deps = self.deps
        full_path = ''
        if len(deps) > 2:
            for i in deps:
                full_path += f' --> {i}'
            full_path = full_path.replace(" --> ", "", 1)
        elif len(deps) == 2:
            full_path = f'{deps[0]} --> {deps[1]}'
        else:
            full_path = f'{deps[0]}'
        return full_path.strip()

    def new_salary(self):
        """Новая зарплата"""
        # todo Здесь нужно написать код
        age = self.age
        deps = self.deps
        deps_str = ''
        for i in range(len(deps)):
            deps_str += deps[i]
        frequent = 0
        # создадим словарь, где ключ - буква, значение - количество вхождений. Таким образом, если мы встретим букву, которая уже была в словаре
        # , то мы её перезапишем, а не добавим в список новое значение
        dict_salary = {key: deps_str.count(key) for key in deps_str}
        dict_values = [i for i in dict_salary.values()]

        for i in range(3):
            maximum = max(dict_values)
            frequent += maximum
            dict_values.remove(maximum)

        print(dict_values, type(dict_values))
        return age * 1337 * frequent

