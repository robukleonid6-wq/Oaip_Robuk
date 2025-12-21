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

emp = Employee("мага", 50000)
print(f"начальная зарплата: {emp.salary}")

emp.salary = -100
print({emp.salary})

emp.salary = 60000
print(f"зарплата: {emp.salary}")