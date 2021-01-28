# Инкапсуляция - Пример с точкой в плоскости

class Point:  # У точки есть два атрибута положение по оси Х и положение по оси Y

    def __init__(self, x=1, y=None):
        self.x = x
        self.__y = y

    def set_y(self):
        self.__y = self.x * 2
        return self.__y


    def setCoords(self, x, y):
        if self.__y == None:
            raise ValueError ('Сначала вызовите метод set_y')
        return self.x, self.__y


    def getCoords(self):
        return self.x, self.__y

    def __repr__(self):
        return f'положение точки = {self.x}, {self.__y}'


pt = Point()
print(pt.getCoords())
print(pt.setCoords(3,6))

# print(pt.x)