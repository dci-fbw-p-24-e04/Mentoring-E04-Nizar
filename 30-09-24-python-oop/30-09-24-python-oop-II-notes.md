
### Class Definitions

#### Employee Class

```python
class Employee:
```
- This line defines a new class called `Employee`, which represents an employee with specific attributes and methods.

##### Constructor Method

```python
def __init__(self, name, age, salary):
```
- The `__init__` method initializes an instance of the `Employee` class with the provided `name`, `age`, and `salary` parameters.

```python
self.name = name
self.age = age
self.salary = salary
```
- These lines assign the values of the parameters to instance variables:
  - `self.name` stores the employee's name.
  - `self.age` stores the employee's age.
  - `self.salary` stores the employee's salary.

##### Instance Methods

```python
def display_info(self):
```
- This method prints the employee's information.

```python
print(f"name : {self.name}")
print(f"age : {self.age}")
print(f"salary : {self.salary}")
```
- These lines print the employee's name, age, and salary.

```python
def work(self):
```
- This method returns a string indicating that the employee is working.

```python
return f"{self.name} is working"
```

```python
def leave(self, time):
```
- This method takes a `time` parameter and checks if the employee is leaving early or going to relax.

```python
if time < 17:
    return self.work()
```
- If the time is less than 17 (5 PM), it calls the `work` method to indicate that the employee is still working.

```python
else:
    return f"{self.name} is going to drink a beer"
```
- If the time is 17 or greater, it returns a message that the employee is going to drink a beer.

#### Manager Class

```python
class Manager(Employee):
```
- This line defines a new class `Manager`, which inherits from the `Employee` class. This means that the `Manager` class has all the attributes and methods of the `Employee` class but can also have additional features or overridden methods.

##### Constructor Method

```python
def __init__(self, name, age, salary, department):
```
- The constructor for the `Manager` class takes an additional `department` parameter.

```python
super().__init__(name, age, salary)
```
- This line calls the constructor of the parent class (`Employee`) to initialize the `name`, `age`, and `salary` attributes.

```python
self.department = department
```
- This line initializes the `department` attribute specific to the `Manager` class.

##### Overridden Methods

```python
def display_info(self):
```
- This method overrides the `display_info` method from the `Employee` class.

```python
super().display_info()
```
- This line calls the parent class's `display_info` method to display the employee's name, age, and salary.

```python
print(f"department: {self.department}")
```
- This line prints the manager's department.

```python
def work(self):
```
- This method overrides the `work` method from the `Employee` class.

```python
return f"{self.name} is not working he is the manager"
```
- This line returns a message indicating that the manager is not working since they are in charge.

##### Additional Method

```python
def go_on_vacation(self):
```
- This method returns a message indicating that the manager is on vacation.

```python
return f"{self.name} is on vacation"
```

### Creating Instances

```python
john = Employee("John", 30, 50)
```
- This line creates an instance of the `Employee` class named `john`, with the name `"John"`, age `30`, and salary `50`.

```python
boss = Manager("Boss", 45, 755566, "Finance")
```
- This line creates an instance of the `Manager` class named `boss`, with the name `"Boss"`, age `45`, salary `755566`, and department `"Finance"`.

### Inspecting the Instances

```python
print(dir(john))
```
- This prints a list of all attributes and methods of the `john` object, including those inherited from the `Employee` class.

```python
print("-" * 50)
print(dir(boss))
```
- This prints a list of all attributes and methods of the `boss` object, including those inherited from both the `Employee` and `Manager` classes.

```python
print("-" * 50)
```
- This line prints a separator line for better readability.

### Accessing Instance Methods

```python
john.display_info()
```
- This calls the `display_info` method of the `john` object, which outputs:
  ```
  name : John
  age : 30
  salary : 50
  ```

```python
print(john.leave(16))
```
- This calls the `leave` method of the `john` object with the time `16`. Since `16` is less than `17`, it calls the `work` method, resulting in:
  ```
  John is working
  ```

```python
# print(john.go_on_vacation())
```
- This line is commented out, but if it were executed, it would raise an `AttributeError` since the `go_on_vacation` method is not defined for `Employee`.

```python
print("-" * 50)
```
- Another separator line for clarity.

```python
boss.display_info()
```
- This calls the `display_info` method of the `boss` object, which will output:
  ```
  name : Boss
  age : 45
  salary : 755566
  department: Finance
  ```

```python
print(boss.leave(16))
```
- This calls the `leave` method of the `boss` object with the time `16`. Since `16` is less than `17`, it calls the `work` method, resulting in:
  ```
  Boss is not working he is the manager
  ```

```python
print(boss.go_on_vacation())
```
- This calls the `go_on_vacation` method of the `boss` object, which outputs:
  ```
  Boss is on vacation
  ```

### Summary

- The `Employee` class represents an employee with attributes for name, age, and salary, along with methods for displaying information, working, and leaving.
- The `Manager` class inherits from `Employee`, adding a department attribute and overriding methods to change their behavior.
- Instances of both classes are created, and their methods are called to demonstrate their functionality, including displaying information and determining if they are working or on vacation.

