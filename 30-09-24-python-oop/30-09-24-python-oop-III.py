class Flyer:
    def fly(self):
        return 'I can fly'
    def run(self):
        return 'I can run at full speed'
class SuperStrength:
    def lift_heav_objects(self):
        return 'I can lift heavy objects'
    def run(self):
        return 'I can run'
class Teleporter:
    def teleport(self):
        return 'I can teleport'
    def run(self):
        return 'I dont need to run because i teleport'
    
class SuperHero(Teleporter,SuperStrength,Flyer):
    def __init__(self,name):
        self.name = name
        
    def shoot_laser(self):
        return f"I am {self.name} and i can shoot laser"   
    
    def code(self):
        return f"I am {self.name} and i can fight bugs and error in your code"     
    
super_python = SuperHero('SP')
print(super_python.fly())
print(super_python.teleport())
print(super_python.lift_heav_objects())
print(super_python.shoot_laser())
print(super_python.run())
print(SuperHero.__mro__)#method resolution order
print(super_python.__class__.__mro__) 
