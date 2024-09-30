### Exercise Task: Inheritance in Python

**Objective**: Create a Python program that demonstrates 3-level inheritance using a parent class, two child classes, and a subclass that inherits from the two child classes. You will also print the method resolution order (MRO) for the subclass.

**Instructions**:

1. **Choose a Topic**: Decide on a theme for your classes. Here are some examples:
   - **Animals**: Parent class `Animal`, child classes `Mammal` and `Bird`, subclass `Bat` that inherits from both `Mammal` and `Bird`.
   - **Vehicles**: Parent class `Vehicle`, child classes `Car` and `Bike`, subclass `ElectricBike` that inherits from both `Car` and `Bike`.
   - **Shapes**: Parent class `Shape`, child classes `2DShape` and `3DShape`, subclass `Cube` that inherits from both.

2. **Define Your Classes**:
   - Create a **parent class** with at least one method.
   - Create **two child classes** that inherit from the parent class, each having its own methods.
   - Create a **subclass** that inherits from both child classes and has its own methods.

3. **Implement MRO**: In the subclass, print the method resolution order (MRO) using the `__mro__` attribute or the `mro()` method.

4. **Example Structure**:
   Here’s a structure to guide you (you can modify it according to your chosen theme):

```python
# Step 1: Define the Parent Class
class ParentClass:
    def parent_method(self):
        return "This is a method from the parent class."

# Step 2: Define the First Child Class
class ChildClass1(ParentClass):
    def child1_method(self):
        return "This is a method from Child Class 1."

# Step 3: Define the Second Child Class
class ChildClass2(ParentClass):
    def child2_method(self):
        return "This is a method from Child Class 2."

# Step 4: Define the Subclass
class SubClass(ChildClass1, ChildClass2):
    def subclass_method(self):
        return "This is a method from the Subclass."

# Step 5: Print MRO
print(SubClass.__mro__)
```

5. **Expected Output**: You should see the methods from the parent and child classes being accessible from the subclass, as well as the MRO printed, which indicates the order in which Python looks for methods.

### Example Solution
Using the Animals theme as an example, the structure might look like this:

```python
class Animal:
    def sound(self):
        return "Some generic animal sound."

class Mammal(Animal):
    def walk(self):
        return "I can walk."

class Bird(Animal):
    def fly(self):
        return "I can fly."

class Bat(Mammal, Bird):
    def echolocate(self):
        return "I can echolocate."

# Create an instance of the subclass
bat = Bat()

# Call methods from all levels
print(bat.sound())        # Output: Some generic animal sound.
print(bat.walk())        # Output: I can walk.
print(bat.fly())         # Output: I can fly.
print(bat.echolocate())  # Output: I can echolocate.

# Print the MRO
print(Bat.__mro__)
```

### Submission
- Submit your Python code demonstrating the 3-level inheritance and the printed MRO.
- Include comments explaining your design choices.


