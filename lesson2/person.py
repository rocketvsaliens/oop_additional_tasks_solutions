"""
Напишите класс Person, имеющий следующие методы:

- __init__(self, name, age): конструктор, принимающий имя и возраст человека
- display(self): метод, выводящий на экран имя и возраст человека
- from_birth_year(cls, name, birth_year): класс-метод, принимающий имя и год рождения человека и
возвращающий объект класса Person;
- is_adult(cls, age): статический метод, принимающий возраст человека и возвращающий True,
если он старше 18 лет, и False в противном случае
"""

# Импортируем datetime для получения текущего года,
# чтобы посчитать возраст человека по году его рождения
from datetime import datetime


class Person:

    def __init__(self, name: str, age: int):
        """Конструктор-инициализатор экземпляров класса, принимающий имя и возраст человека"""
        self.name = name
        self.age = age

    def display(self) -> None:
        """Выводим на экран имя и возраст человека"""
        print(f'{self.name} is {self.age} years old')  # "выводящий на экран" -- значит используем print, а не return

    @classmethod
    def from_birth_year(cls, name: str, birth_year: int):
        """
        Считаем возраст человека, зная год его рождения
        <текущий год> - <год рождения> = <возраст>
        и возвращаем экземпляр класса Person
        :param cls: будет передан неявно, автоматически интерпретатором Python
        :param name: имя человека, нужно для формирования экземпляра класса
        :param birth_year: год рождения человека, чтобы посчитать возраст
        """
        current_year = datetime.now().year  # при помощи datetime получаем текущий год
        age = current_year - birth_year  # вычисляем возраст
        return cls(name, age)  # вернёт экземпляр, где вместо cls подставится имя класса

    @staticmethod
    def is_adult(age: int):
        """
        Вернёт True, если возраст больше или равно 18 и False в противном случае
        :param age: возраст человека
        """
        return age >= 18  # цифру 18 можно вынести в константу


if __name__ == '__main__':
    # создаём экземпляр класса классическим способом
    person1 = Person("John", 28)
    # выводим на экран имя и возраст из созданного экземпляра класса
    person1.display()  # John is 28 years old

    # создаём экземпляр класса через метод класса from_birth_year
    # с вычислением возраста по году рождения
    person2 = Person.from_birth_year("Mike", 1997)
    # выводим на экран имя и возраст из созданного экземпляра класса
    person2.display()  # Mike is 26 years old (в зависимости от текущего года возраст может меняться)

    # проверяем на взрослость
    # staticmethod позволяет вызывать метод класса как обычную функцию
    print(Person.is_adult(20))  # True
    print(Person.is_adult(15))  # False
