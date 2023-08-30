"""
Напишите класс Point, представляющий собой точку на плоскости, имеющий следующие методы:

- __init__(self, x, y): конструктор, принимающий координаты точки;
- __repr__(self): магический метод, возвращающий строковое представление точки, которое можно использовать для создания нового объекта класса Point;
- __str__(self): магический метод, возвращающий строковое представление точки;
- __add__(self, other): магический метод, который позволяет складывать точки и возвращать новую точку.
"""


class Point:

    def __init__(self, x: int, y: int) -> None:
        """Конструктор, принимающий координаты x и y точки"""
        if isinstance(x, int) and isinstance(y, int):  # проверяем значения на тип числа
            self.x = x
            self.y = y
        else:
            # если введены не числа, выбрасываем исключение TypeError
            raise TypeError('Значения x и y должны быть целыми числами')

    def __repr__(self) -> str:
        """
        Возвращает строковое представление точки,
        которое можно использовать для создания нового объекта класса
        """
        return f'{self.__class__.__name__}({self.x}, {self.y})'

    def __str__(self) -> str:
        """Возвращает строковое представление точки"""
        return f'Координаты точки (x, y): ({self.x}, {self.y})'

    def __add__(self, other):
        """Складывает точки и возвращает новый объект класса"""
        return self.__class__(self.x + other.x, self.y + other.y)


if __name__ == '__main__':
    # создаём экземпляр класса
    point1 = Point(1, 2)
    # выводим строковое представление, по которому можно создать новый объект
    print(repr(point1))  # Point(1, 2)
    # выводим человеческое строковое представление
    print(str(point1))  # Координаты точки (x, y): (1, 2)

    # создаём ещё один экземпляр класса
    point2 = Point(3, 4)
    # складываем два экземпляра класса -- получаем третий
    point3 = point1 + point2
    # выводим человеческую информацию о новом экземпляре класса
    print(point3)  # Координаты точки (x, y): (4, 6)
