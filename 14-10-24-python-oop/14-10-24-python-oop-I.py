class Animal:
    def sound(self):
        pass
    
class Dog(Animal):
    def sound(self):
        print('Woof')
        
class Cat(Animal):
    def sound(self):
        print('Meow')
        
    def run(self):
        print('this cat is running')
        
class Duck(Animal):
    def sound(self):
        print('Quack')
        
    def swim(self):
        print('duck is swimming in the lake')
        
        
def make_sound(obj):
    print(f"{type(obj).__name__} said")
    obj.sound()#obj can be dog cat or a duck
    
cat = Cat()
dog = Dog()
duck = Duck()

make_sound(dog)
print('-'*30)
make_sound(cat)
print('-'*30)
make_sound(duck)
print('-'*30)
list_of_animals = []
for _ in range(4):
    list_of_animals.append(cat)
    list_of_animals.append(dog)
    list_of_animals.append(duck)
    
import random 
random.shuffle(list_of_animals)
for animal in list_of_animals:
    make_sound(animal)
    #animal.sound()