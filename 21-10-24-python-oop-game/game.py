from characters import Character,Warrior,Witcher
from stringcolor import cs
import random
class StoryGame:
    def __init__(self) :
        self.player = None
        self.enemy = None
        self.story_progress = 0
        self._maps = [
            "1. Explore the forest",
            "2. Enter the dark cave",
            "3. Return to village",
            "4. Exit the game",
        ]
        
    def start(self):
        print(cs("Welcome to the OOP game","red"))
        player_name = input("Enter your character name ")
        player_class = input("Enter your character class (Warrior/Witcher): ")
        if player_class.lower() == 'warrior':#waRrior,WaRrIoR
            self.player = Warrior(player_name)
            
        elif player_class.lower() =='witcher':
            self.player = Witcher(player_name)
            
        else :
            random_character = random.choice([Warrior(player_name),Witcher(player_name)])
            print(cs(f"Invalid input, you gonna go as a {type(random_character).__name__}","blue"))
            self.player = random_character
        
        self._play_game()
        
    def _play_game(self):
        print(cs(
            f"Welcome {self.player.name} the amazing {type(self.player).__name__}","green"
        ))
        print(cs("...","green"))
        print(cs("You find yourself at a crossroad. What will you do?\n","red"))
        while self.player.is_alive():
            print("\n".join(self._maps))
            choice = input("Enter your choice ")
            if choice == "1":
                self.explore_the_forest()
            elif choice == "2":
                self.enter_cave()
            elif choice == "3":
                self.return_to_village()
            elif choice == "4":
                print(cs("Thank your for playing our game. See you next time","purple"))
            else:
                print("Invalid input. Try again")
        print(cs("Game over until next time",'red'))
    
    def explore_the_forest(self):
        print("You entered the forst and you found the 3 headed Snake!")
        self.enemy = Character("Hydra",100,35)
        self.battle()
        
    def enter_cave(self):
        print("You enteredthe cave and found a Dragon!")
        self.enemy = Character('Dragon',100,35)
        self.battle()
        
    def return_to_village(self):
        print('You returned to village')
        self.player.health_points += 10
        self.story_progress += 1
        if self.story_progress % 4 ==0 :
            self.player.damage_points += 10
        print(f"story game progress : {self.story_progress}")
        
    def battle(self):
        counter = 0
        while self.player.is_alive() and self.enemy.is_alive():
            print(cs(
                f"{self.player.name} (Health : {self.player.health_points}) VS {self.enemy.name} (Health : {self.enemy.health_points})" ,'red')
            )
            action = input(
                "Enter 'a' to attack or 's' to special attack or 'f' to flee "
            )
            if action =='a':
                counter+=1
                self.player.attack(self.enemy)
                if self.enemy.is_alive():
                    self.enemy.attack(self.player)
            
            elif action =='s':
                if counter %3 == 0:
                    self.player.special_attack(self.enemy)
                    if self.enemy.is_alive():
                        self.enemy.attack(self.player)
                else:
                    counter+=1
                    self.player.attack(self.enemy)
                    if self.enemy.is_alive():
                        self.enemy.attack(self.player)
            elif action == "f":
                print("you escaped from the battle")
                self.story_progress -= 1 
                break
            else:
                print("Invalid input")  
        if not self.enemy.is_alive():
            print("you defeated the monster")
            self.story_progress += 1  
               
        elif not self.player.is_alive():
            print('You lost against the monster')