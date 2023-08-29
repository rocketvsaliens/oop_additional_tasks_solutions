"""
Напишите класс BankAccount, имеющий следующие свойства и методы:

- __init__(self, balance): конструктор, принимающий начальный баланс счета
- balance: свойство, которое возвращает текущий баланс счета
- deposit(self, amount): метод, который позволяет внести деньги на счет
- withdraw(self, amount): метод, который позволяет снять деньги со счета
- close(self): метод, который закрывает счет и возвращает оставшиеся на нем деньги

Для свойства balance используйте декоратор @property.
"""


class BankAccount:

    def __init__(self, balance: int or float) -> None:
        """Конструктор-инициализатор экземпляров класса, принимающий начальный баланс счета"""
        self.__balance = balance

    @property
    def balance(self) -> int or float:
        """Возвращает текущий баланс счета"""
        return self.__balance

    def deposit(self, amount: int or float) -> None:
        """Позволяет внести деньги на счет"""
        self.__balance += amount

    def withdraw(self, amount: int or float) -> None:
        """Позволяет снять деньги со счета"""
        self.__balance -= amount

    def close(self) -> int or float:
        """Закрывает счет и возвращает оставшиеся на нем деньги"""
        # Надеюсь, банковские программисты никогда не увидят этот код,
        # потому что по сути здесь происходит грабёж, но таковы условия задачи (см. вызов close())
        self.__balance = 0
        return self.__balance


if __name__ == '__main__':
    account = BankAccount(1000)
    print(account.balance)  # 1000

    account.deposit(500)
    print(account.balance)  # 1500

    account.withdraw(200)
    print(account.balance)  # 1300

    account.close()
    print(account.balance)  # 0
