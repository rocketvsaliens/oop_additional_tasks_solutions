"""
Напишите класс User, имеющий следующие свойства и методы:

- __init__(self, name, password): конструктор, принимающий имя пользователя и пароль
- name: свойство, которое возвращает имя пользователя
- password: свойство, которое позволяет установить или изменить пароль пользователя
- is_admin: свойство, которое возвращает, является ли пользователь администратором или нет
- _is_admin: свойство-помощник, которое определяет, является ли пользователь администратором или нет
- login(self, password): метод, который проверяет, соответствует ли введенный пароль паролю пользователя
- logout(self): метод, который выходит из аккаунта пользователя
(устанавливает значение свойства _is_logged_in в False при условии, что пользователь залогинен)

Для свойств name и password используйте декораторы @property и @password.setter.
"""


class User:

    def __init__(self, name: str, password: str) -> None:
        """Конструктор экземпляра класса"""
        self.__name = name
        self.__password = password
        # доп. поля, является ли экземпляр класса админом и залогинен ли он.
        # По умолчанию оба поля принимают значение False
        self._is_admin = False
        self._is_logged_in = False

    @property
    def name(self) -> str:
        """Возвращает имя пользователя"""
        return self.__name

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, new_password):
        """Устанавливает или изменяет пароль пользователя"""
        self.__password = new_password

    @property
    def is_admin(self):
        """Возвращает, является ли пользователь администратором или нет"""
        # в задаче речь идёт почему-то о свойстве, хотя свойство ничего возвращать не может,
        # поэтому реализация сделана методом
        return self._is_admin

    @is_admin.setter
    def is_admin(self, value):
        """Устанавливает или снимает права администратора"""
        self._is_admin = value

    @property
    def is_logged_in(self):
        return self._is_logged_in

    def login(self, password):
        """
        Проверяет, соответствует ли введённый пароль паролю пользователя.
        Если совпадает, устанавливает статус залогинен.
        :param password: введённый пароль
        """
        if password == self.__password:
            self._is_logged_in = True

    def logout(self):
        """
        Проверяет, залогинен ли пользователь.
        Если да, то меняет на разлогинен.
        """
        if self._is_logged_in:
            self._is_logged_in = False


if __name__ == '__main__':
    user1 = User("Alice", "qwerty")
    print(user1.name)  # Alice
    print(user1.password)  # qwerty
    print(user1.is_admin)  # False

    user1.password = "newpassword"
    print(user1.password)  # newpassword

    user1._is_admin = True
    print(user1.is_admin)  # True

    user1.login("newpassword")
    print(user1.is_logged_in)  # True
    user1.logout()
    print(user1.is_logged_in)  # False
