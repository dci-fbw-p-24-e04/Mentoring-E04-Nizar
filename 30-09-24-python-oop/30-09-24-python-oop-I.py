class Animal:
    def __init__(self,name,num_of_legs,sound):
        self.name = name
        self.num_of_legs = num_of_legs
        self.sound = sound
        
    def walk(self):
        return f"{self.name} is walking on {self.num_of_legs} legs"
    
    def make_sound(self):
        return f"{self.name} said {self.sound}"
    
    
   
cat = Animal('Cat',4,'Meow')
print(type(cat))
print(dir(cat))
print(cat.name)
print(cat.num_of_legs)
print(cat.sound)
#acces the methods
print(cat.walk())
print(cat.make_sound())
cat.name = 'dog'#setting
print(cat.make_sound())

        