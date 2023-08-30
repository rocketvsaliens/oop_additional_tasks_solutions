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
        # По умолчанию оба поля должны принимать значение False
        self._is_admin = False
        self._is_logged_in = False

    @property
    def name(self) -> str:
        """Возвращает имя пользователя"""
        return self.__name

    @property
    def password(self) -> str:
        """Возвращает пароль пользователя"""
        # в реальной жизни никто так не делает, потому что
        # пароли хранятся в зашифрованном виде в специальной таблице
        return self.__password

    @password.setter
    def password(self, new_password: str) -> None:
        """Устанавливает или изменяет пароль пользователя"""
        # Без всякого подтверждения, что мы знаем старый пароль ))
        # Чтобы узнать, что пользователь тот самый, достаточно добавить один параметр "old_password"
        # таким образом, мы будем передавать старый пароль, сравнивать его с текущим,
        # и если они совпадают, устанавливать новый пароль. Но в задаче этого нет, поэтому нет и в реализации.
        self.__password = new_password

    @property
    def is_admin(self) -> bool:
        """Возвращает, является ли пользователь администратором или нет"""
        # в задаче речь идёт почему-то о свойстве, хотя свойство ничего возвращать не может,
        # поэтому реализация сделана методом
        return self._is_admin

    @is_admin.setter
    def is_admin(self, value: bool) -> None:
        """Устанавливает или снимает права администратора"""
        self._is_admin = value

    @property
    def is_logged_in(self) -> None:
        return self._is_logged_in

    def login(self, password: str) -> None:
        """
        Проверяет, соответствует ли введённый пароль паролю пользователя.
        Если совпадает, устанавливает статус залогинен.
        :param password: введённый пароль
        """
        # Имитируем логин: если пароль введён правильно, меняем значение _is_logged_in на True.
        # В реальности нам бы не помешало проверить имя пользователя тоже)
        # Вместо пароля принято хранить его хэш, но это отдельная история.
        if password == self.__password:
            self._is_logged_in = True

    def logout(self) -> None:
        """
        Проверяет, залогинен ли пользователь.
        Если да, то меняет на разлогинен.
        """
        if self._is_logged_in:
            self._is_logged_in = False


if __name__ == '__main__':
    # создаём экземпляр класса
    user1 = User("Alice", "qwerty")
    # выводим имя пользователя
    print(user1.name)  # Alice
    # выводим пароль пользователя (ай-яй-яй)
    print(user1.password)  # qwerty
    # проверяем, является ли пользователь админом
    print(user1.is_admin)  # False

    # устанавливаем новый пароль пользователя
    user1.password = "newpassword"
    # печатаем новый пароль
    print(user1.password)  # newpassword

    # делаем пользователя админом
    user1._is_admin = True
    # снова проверяем, есть ли у пользователя права админа
    print(user1.is_admin)  # True

    # имитуруем логин с паролем
    user1.login("newpassword")
    # выводим статус логина
    print(user1.is_logged_in)  # True
    # разлогиниваемся
    user1.logout()
    # снова выводим статус логина
    print(user1.is_logged_in)  # False
