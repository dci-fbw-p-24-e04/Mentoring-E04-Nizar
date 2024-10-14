### Exercise Task: Abstraction and Encapsulation in Python

**Objective**: Create a Python program that demonstrates **abstraction** using abstract classes and methods, along with **encapsulation** by using private variables and getter/setter methods.

### Instructions:

1. **Choose a Topic**: Select a theme for your classes. Some possible examples:
   - **Appliances**: Abstract class `Appliance` with abstract methods like `turn_on()`. Concrete classes like `WashingMachine` and `Oven` implement the abstract methods.
   - **Payment System**: Abstract class `Payment` with abstract methods like `process_payment()`. Concrete classes like `CreditCard` and `PayPal` implement the methods.
   - **Employees**: Abstract class `Employee` with abstract methods like `calculate_salary()`. Concrete classes like `FullTimeEmployee` and `ContractEmployee` implement the methods.

2. **Abstraction**:
   - Create an **abstract class** using Python’s `abc` module.
   - The abstract class should have at least one abstract method.
   - Create at least **two concrete classes** that inherit from the abstract class and implement its abstract methods.

3. **Encapsulation**:
   - In one of the concrete classes, define **private variables** using double underscores (`__`).
   - Provide **getter** and **setter** methods to access and modify the private variables.

4. **Example Structure**:
   Here’s a structure to guide you (you can modify it based on your theme):

```python
from abc import ABC, abstractmethod

# Step 1: Define the Abstract Class
class ParentClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

# Step 2: Define the First Concrete Class
class ChildClass1(ParentClass):
    def abstract_method(self):
        return "Abstract method implemented by ChildClass1."

# Step 3: Define the Second Concrete Class with Encapsulation
class ChildClass2(ParentClass):
    def __init__(self):
        self.__private_var = "I am private"
    
    def abstract_method(self):
        return "Abstract method implemented by ChildClass2."
    
    def get_private_var(self):
        return self.__private_var
    
    def set_private_var(self, value):
        self.__private_var = value
```

5. **Expected Output**: You should see the abstract method being implemented by both child classes, as well as the encapsulated variable accessed and modified through getter and setter methods.

### Example Solution
Using the **Appliances** theme as an example, the structure might look like this:

```python
from abc import ABC, abstractmethod

# Step 1: Abstract class
class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass

# Step 2: Concrete class 1
class WashingMachine(Appliance):
    def turn_on(self):
        return "Washing Machine is now running."

# Step 3: Concrete class 2 with Encapsulation
class Oven(Appliance):
    def __init__(self, temperature):
        self.__temperature = temperature  # private variable
    
    def turn_on(self):
        return f"Oven is heating to {self.__temperature}°C."

    # Getter
    def get_temperature(self):
        return self.__temperature

    # Setter
    def set_temperature(self, value):
        self.__temperature = value

# Create instances
washing_machine = WashingMachine()
oven = Oven(200)

# Call the abstract method implementations
print(washing_machine.turn_on())  # Output: Washing Machine is now running.
print(oven.turn_on())  # Output: Oven is heating to 200°C.

# Use encapsulation (getter and setter)
print(oven.get_temperature())  # Output: 200
oven.set_temperature(220)
print(oven.get_temperature())  # Output: 220
```

### Submission:
- Submit your Python code demonstrating **abstraction** with abstract classes and **encapsulation** using private variables and getter/setter methods.
- Include comments explaining your design choices and how abstraction and encapsulation are applied in your code.

