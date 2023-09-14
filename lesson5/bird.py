"""
Напишите класс Bird, представляющий птицу, имеющий следующие методы:
- fly(self): метод, который выводит сообщение "Flying".
Напишите класс Penguin, наследующийся от класса Bird, представляющий пингвина, имеющий следующие методы:
- fly(self): метод, который выводит сообщение "I am a penguin and cannot fly".
Напишите класс Eagle, наследующийся от класса Bird, представляющий орла, имеющий следующие методы:
- hunt(self): метод, который выводит сообщение "Hunting".
"""


class Bird:
    """Класс, представляющий птицу"""

    def fly(self) -> None:
        """Метод, который выводит сообщение 'Flying'"""
        print('Flying')


class Penguin(Bird):
    """Класс, наследующийся от класса Bird, представляющий пингвина"""

    def fly(self) -> None:
        """Метод, который выводит сообщение, что пингвин не летает"""
        print('I am a penguin and cannot fly')


class Eagle(Bird):
    """Класс, наследующийся от класса Bird, представляющий орла"""

    def hunt(self) -> None:
        """Метод, который выводит сообщение 'Hunting'"""
        print('Hunting')


# Создаём экземпляр класса Bird
bird = Bird()
# Выводим сообщение при помощи метода fly()
bird.fly()  # Flying

# Создаём пингвина
penguin = Penguin()
# Выводим сообщение, что пингвин не умеет летать
penguin.fly()  # I am a penguin and cannot fly

# Создаём орла
eagle = Eagle()
# Выводим сообщение, что орёл летает --
# метод fly() подтягивается из родительского класса Bird
eagle.fly()  # Flying
# Выводим сообщение, что орёл охотится
eagle.hunt()  # Hunting
