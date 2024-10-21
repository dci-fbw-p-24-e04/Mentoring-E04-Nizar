class Character:
    def __init__(self,name,health_points,damage_points) :
        self.name = name
        self.health_points = health_points
        self.damage_points = damage_points
        
    def is_alive(self):
        return self.health_points > 0
    
    def take_damage(self,dp):
        self.health_points -= dp
        if self.health_points < 0:
            self.health_points = 0 #setting the hp to zero 
            
    def attack(self,enemy):#enemy is a character
        enemy.take_damage(self.damage_points)
        
        
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health_points=100, damage_points=30)
        
    def special_attack(self,enemy):
        enemy.take_damage(2*self.damage_points)
        
class Witcher(Character):
    def __init__(self, name):
        super().__init__(name, health_points=85, damage_points=45)
        
    def special_attack(self,enemy):
        self.health_points += 10
        for _ in range(3):
            enemy.take_damage(12)


