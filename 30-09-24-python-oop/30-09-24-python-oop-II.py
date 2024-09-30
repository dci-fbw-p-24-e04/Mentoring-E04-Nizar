class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display_info(self):
        print(f"name : {self.name}")
        print(f"age : {self.age}")
        print(f"salary : {self.salary}")

    def work(self):
        return f"{self.name} is working"

    def leave(self, time):
        if time < 17:
            return self.work()
        else:
            return f"{self.name} is going to drink a beer"


class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"deparment {self.department}")

    def work(self):
        return f"{self.name} is not working he is the manager"

    def go_on_vacation(self):
        return f"{self.name} is on vacation"


john = Employee("John", 30, 50)
boss = Manager("Boss", 45, 755566, "Finance")
print(dir(john))
print("-" * 50)
print(dir(boss))
print("-" * 50)
john.display_info()
print(john.leave(16))
# print(john.go_on_vacation())
print("-" * 50)
boss.display_info()
print(boss.leave(16))
print(boss.go_on_vacation())
