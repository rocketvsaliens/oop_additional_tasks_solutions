"""
Напишите класс Employee, представляющий сотрудника, имеющий следующие методы:

- __init__(self, name, salary): конструктор, принимающий имя сотрудника и его зарплату;
- get_salary(self): метод, который возвращает зарплату сотрудника.

Напишите класс Manager, наследующийся от класса Employee, представляющий менеджера, имеющий следующие методы:

- __init__(self, name, salary, bonus): конструктор, принимающий имя менеджера, его зарплату и бонус;
- get_salary(self): метод, который возвращает зарплату менеджера плюс его бонус.
"""


class Employee:
    """Класс, представляющий сотрудника"""

    def __init__(self, name: str, salary: int or float) -> None:
        """Конструктор, принимающий имя сотрудника и его зарплату"""
        self._name = name
        self._salary = salary

    def get_salary(self) -> int or float:
        """Метод, который возвращает зарплату сотрудника"""
        return self._salary


class Manager(Employee):
    """Класс, наследующийся от класса Employee, представляющий менеджера"""

    def __init__(self, name: str, salary: int or float, bonus: int or float) -> None:
        """Конструктор, принимающий имя менеджера, его зарплату и бонус"""
        # за именем и зарплатой обращаемся в инициализатор родительского класса
        super().__init__(name, salary)
        # добавляем бонус
        self.bonus = bonus

    def get_salary(self) -> int or float:
        """Метод, который возвращает зарплату менеджера плюс его бонус"""
        return self._salary + self.bonus


# Создаём работника
employee = Employee("John", 5000)
# Выводим зарплату работника
print(employee.get_salary())  # 5000

# Создаём работника-менеджера
manager = Manager("Jane", 10000, 5000)
# Выводим зарплату менеджера с учётом бонуса
print(manager.get_salary())  # 15000
