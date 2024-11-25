class PublicTransport:
    def __init__(self, brand, engine_power, year, color, max_speed):
        self.brand = brand
        self._engine_power = engine_power
        self.year = year
        self.color = color
        self.max_speed = max_speed


    @property
    def info(self):
        """Информация о транспорте"""
        return self.brand, self.color, self.year, self._engine_power


class Bus(PublicTransport):
    def __init__(self, brand, engine_power, year, color, max_speed, passengers, park, fare):
        super().__init__(brand, engine_power, year, color, max_speed)
        self.passengers = passengers
        self.__park = park
        self._fare = fare

    @property
    def park(self):
        return self.__park

    @park.setter
    def park(self, park):
        assert 1000 <= park <= 9999, 'Проверка на ограничение диапазона НЕ пройдена: '
        self.__park = park

class Tram(PublicTransport):
    def __init__(self, brand, engine_power, year, color, max_speed, route, path, fare):
        super().__init__(brand, engine_power, year, color, max_speed)
        self.__route = route
        self.path = path
        self._fare = fare

    @property
    def how_long(self):
        """Время прохождения маршрута"""
        max_speed = self.max_speed
        path = self.path
        return max_speed / (4*path)
