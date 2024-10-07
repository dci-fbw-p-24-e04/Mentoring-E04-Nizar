# first and last name : public
#social security number : private
#facebook credentials : protected
class MyClass:
    def __init__(self):
        self.my_public_attribute = "I am a public attribute"
    def my_public_method(self):
        print("I am a public method")
        
obj = MyClass()
print(obj.my_public_attribute)
obj.my_public_method()

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

rectangle = Rectangle(5, 3)
area = rectangle.calculate_area()

#The protected access modifier allows the access of class members within the class and its subclasses. 
# To denote a member as protected, you can prefix it conventionally with a single underscore (_).

class MyBaseClass:
    def __init__(self):
        self._my_protected_attribute = "I am a protected attribute"

    def _my_protected_method(self):
        print("I am a protected method")
print('-'*50)
class MyDerivedClass(MyBaseClass):
    def __init__(self):
        super().__init__()
        
    def access_protected_member(self):
        print(self._my_protected_attribute)
        self._my_protected_method()
 
 
# Accessing protected members       
obj = MyDerivedClass()
obj.access_protected_member()
print(obj._my_protected_attribute)
obj._my_protected_method()

class Animal:
    def __init__(self, name):
        self._name = name

    def _make_sound(self):
        pass

class Dog(Animal):
    def _make_sound(self):
        print(f"{self._name} barks")

# Accessing protected members
animal = Animal('Cat')
print(animal._name)
dog = Dog("Buddy")
print(dog._name)
dog._make_sound()
print('-'*50)
#The private access modifier allows the access of class members to within the class only.
# To denote a member as private, you can prefix it conventionally with double underscores (__).
class MyClass:
    def __init__(self):
        self.__my_private_attribute = "I am a private attribute"

    def __my_private_method(self):
        print("I am a private method")
        
obj = MyClass()
#print(obj.__my_private_attribute)#not working
#we can use name mangling
print(obj._MyClass__my_private_attribute)#object.__ClassName+mehtod/attribute

class Person:
    def __init__(self, name, age,ssn):
        self.__name = name
        self.__age = age
        self.__ssn = ssn

    def __display_info(self):
        print(f"Name: {self.__name}, Age: {self.__age}")

    def introduce(self):
        self.__display_info()

# Accessing private members
person = Person("Alice", 30,'14785236')
print(person._Person__age)
person.introduce()
