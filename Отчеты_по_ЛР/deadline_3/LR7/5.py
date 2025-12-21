from dataclasses import dataclass

class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self._salary = salary
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value: float):
        if value < 0:
            print("зарплата не может быть отрицательной")
        else:
            self._salary = value

class LoggableMixin:
    def log(self, message: str):
        class_name = self.__class__.__name__
        print(f"[INFO] {class_name}: {message}")

class EmployeeWithLog(Employee, LoggableMixin):
    pass

@dataclass
class Product:
    name: str
    price: float
    weight: float
    is_available: bool = True

class ProductWithLog(Product, LoggableMixin):
    pass

emp = EmployeeWithLog("Manager", 50000)
emp.log("Сотрудник создан")

product = ProductWithLog("cisco", 500.0, 0.5, True)
product.log("Товар создан")