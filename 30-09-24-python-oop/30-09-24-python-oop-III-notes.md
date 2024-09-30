

### Class Definitions

#### Flyer Class

```python
class Flyer:
    def fly(self):
        return 'I can fly'
    
    def run(self):
        return 'I can run at full speed'
```
- The `Flyer` class has two methods:
  - `fly()`: Returns a string indicating that the entity can fly.
  - `run()`: Returns a string indicating that the entity can run at full speed.

#### SuperStrength Class

```python
class SuperStrength:
    def lift_heav_objects(self):
        return 'I can lift heavy objects'
    
    def run(self):
        return 'I can run'
```
- The `SuperStrength` class also has two methods:
  - `lift_heav_objects()`: Returns a string indicating that the entity can lift heavy objects.
  - `run()`: Returns a string indicating that the entity can run.

#### Teleporter Class

```python
class Teleporter:
    def teleport(self):
        return 'I can teleport'
    
    def run(self):
        return 'I dont need to run because i teleport'
```
- The `Teleporter` class defines two methods:
  - `teleport()`: Returns a string indicating that the entity can teleport.
  - `run()`: Returns a string indicating that the entity doesn't need to run because it can teleport.

### SuperHero Class

```python
class SuperHero(Teleporter, SuperStrength, Flyer):
```
- The `SuperHero` class inherits from `Teleporter`, `SuperStrength`, and `Flyer`. This means that the `SuperHero` class has access to all the methods defined in these three classes.

#### Constructor Method

```python
def __init__(self, name):
    self.name = name
```
- The constructor initializes the `SuperHero` instance with a `name` attribute.

#### Additional Methods

```python
def shoot_laser(self):
    return f"I am {self.name} and I can shoot laser"
```
- This method returns a string indicating that the superhero can shoot lasers.

```python
def code(self):
    return f"I am {self.name} and I can fight bugs and errors in your code"
```
- This method returns a string indicating that the superhero can help with coding issues.

### Creating an Instance

```python
super_python = SuperHero('SP')
```
- This line creates an instance of the `SuperHero` class named `super_python`, initializing it with the name `"SP"`.

### Accessing Methods

```python
print(super_python.fly())
```
- This calls the `fly` method from the `Flyer` class, which returns:  
  **Output:** `I can fly`

```python
print(super_python.teleport())
```
- This calls the `teleport` method from the `Teleporter` class, which returns:  
  **Output:** `I can teleport`

```python
print(super_python.lift_heav_objects())
```
- This calls the `lift_heav_objects` method from the `SuperStrength` class, which returns:  
  **Output:** `I can lift heavy objects`

```python
print(super_python.shoot_laser())
```
- This calls the `shoot_laser` method defined in the `SuperHero` class, which returns:  
  **Output:** `I am SP and I can shoot laser`

```python
print(super_python.run())
```
- This calls the `run` method. Due to the method resolution order (MRO), it will call the `run` method from the `Teleporter` class because it appears first in the inheritance list. Thus, it returns:  
  **Output:** `I dont need to run because I teleport`

### Method Resolution Order (MRO)

```python
print(SuperHero.__mro__)
```
- This line prints the MRO of the `SuperHero` class. The output will show the order in which Python looks for methods:
  ```
  (<class '__main__.SuperHero'>, <class '__main__.Teleporter'>, <class '__main__.SuperStrength'>, <class '__main__.Flyer'>, <class 'object'>)
  ```

```python
print(super_python.__class__.__mro__)
```
- This line achieves the same result as the previous line, but it uses the instance to access its class. The output will also show the MRO:
  ```
  (<class '__main__.SuperHero'>, <class '__main__.Teleporter'>, <class '__main__.SuperStrength'>, <class '__main__.Flyer'>, <class 'object'>)
  ```

### Summary

- The `SuperHero` class inherits from three different classes, each contributing its methods.
- The instance of `SuperHero` can call methods from any of the parent classes, and it also has its own methods.
- The MRO helps determine which method gets called when there are multiple classes in the inheritance chain, ensuring that Python knows the order to look for methods.
- This demonstrates the principles of multiple inheritance, where a class can inherit from multiple parent classes and gain their functionalities.

