# ООП - Обьект Класс
# Инкапсуцляция, полимоМИЗМ, аБСТРАКЦИЯ, НАСЛЕДОВАНИЕ
# ДИЗАЙН ------ СОЛИД!!!




class Figure:    # клас(вданныом случае это обстрактный класс, от которого наследуются дети , мыв не можем его инстанциировать)
    expected_sides_count = int
    figure_name = 'figure'           # атрибут

    def __init__(self, sides_count, length):
        # if sides_count != self.expected_sides_count:
        #     raise ValueError(f"{self.figure_name} sides count must be equal to {self.expected_sides_count} ")
        # if length <= 0:
        #     raise ValueError(f"{self.figure_name} lengse must be greater than 0 ")
        self.sides_count = sides_count
        self.length = length

    def perimeter_and_area(self, ):   # Метод      (полиморфизм) много имплементаций, один интерфейс
        self._get_area()
        self._get_perimeter()

    def _get_area(self):              # инкапсуляция, приватный метод, могут быть использованы только внутри класса
        raise NotImplementedError

    def _get_perimeter(self):
        raise NotImplementedError


class Triangle(Figure):
    expected_sides_count = 3
    figure_name = 'triangle'

    def _get_area(self):
        area = self.length ** 2 * 3 ** 1 / 2 / 4
        print(area)

    def _get_perimeter(self):
        print(self.length * self.sides_count)


class Circle(Figure):
    expected_sides_count = 0
    figure_name = 'circle'

    def _get_area(self):
        area = self.length ** 2 * 3.14
        print(area)

    def _get_perimeter(self):
        print(3.14 * 2 * self.length)


# a = Triangle(3, 5)        #объект
#
# a.perimeter_and_area()


class SuperTriangle(Triangle):
    def _get_side_half(self):
        print(self.length / 2)

    def perimeter_and_area(self):
        super().perimeter_and_area()    # расширяю родительского метода и изменяю под себя
        self._get_side_half()


b = SuperTriangle(3, 5)
b.perimeter_and_area()   # ОБЬЕКТ

# c = Triangle(3, 1)
