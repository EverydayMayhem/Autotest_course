from math import sqrt

class Segment:
    def __init__(self, first_point, second_point):
        self.first_point = first_point
        self.second_point = second_point

    def length(self):
        """Вычисление длины отрезка"""
        # todo Здесь нужно написать код
        first_point = self.first_point
        second_point = self.second_point
        segmentLength = round(sqrt((second_point[0] - first_point[0])**2 + ((second_point[1] - first_point[1])**2)), 2)
        return segmentLength

    def x_axis_intersection(self):
        """Пересечение оси абсцисс"""
        # todo Здесь нужно написать код
        # ось абсцисс имееет координаты (х, 0). Если  наш отрезок пересекает ее, то координаты Y двух точек должны быть с разным знаком (+ и -)
        first_point = self.first_point
        second_point = self.second_point
        intersection = False
        if first_point[1] >= 0 and second_point[1] <= 0:
                intersection = True
        elif first_point[1] <= 0 and second_point[1] >= 0:
                intersection = True
        else:
                intersection = False
        return intersection

    def y_axis_intersection(self):
        """Пересечение оси ординат"""
        # todo Здесь нужно написать код
        first_point = self.first_point
        second_point = self.second_point
        intersection = False
        if first_point[0] >= 0 and second_point[0] <= 0:
            intersection = True
        elif first_point[0] <= 0 and second_point[0] >= 0:
            intersection = True
        else:
            intersection = False
        return intersection
