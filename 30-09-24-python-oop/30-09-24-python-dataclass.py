from dataclasses import dataclass

@dataclass
class Exercise:
    name : str
    reps : int
    sets : int
    time : float
    
#or we can do the usual way:
# class Exercise:
#     def __init__(self,name,reps,sets,time):
#         self.name=name
#         self.reps = reps
#         self.sets = sets
#         self.time = time
        
    
push_up = Exercise('Push Ups',10,5,30)
print(push_up.name)
print(push_up.reps)