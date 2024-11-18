import json
import os
import time
import datetime

WORKOUT_FILE = "workout.json"

class WorkoutNotFoundError(Exception):
    pass

class InvalidInputError(Exception):
    pass

class WorkoutPlanner:
    def __init__(self):
        self.workouts = self.load_workouts()

    def load_workouts(self):
        if os.path.exists(WORKOUT_FILE):
            with open(WORKOUT_FILE,'r') as file:
                return json.load(file)
            
        return {} 
    
    def save_workouts(self):
        with open(WORKOUT_FILE,"w") as file:
            json.dump(self.workouts,file,indent=4)

    def add_workout(self,name,duration,difficulty):
        if name in self.workouts:
            raise InvalidInputError(f"workout {name} already exists")
        self.workouts[name] = {
            "Duration":duration,
            "Difficulty":difficulty
        }
        time.sleep(0.5)
        self.save_workouts()
        print(f"Added workout: {name}")


    def view_workouts(self):
        if not self.workouts:
            print("No workouts here. Get up and do something you lazy!")
        else:
            for name,details in self.workouts.items():
                print(f"Workout : {name}, Duration : {details['Duration']} mins, Difficulty : {details['Difficulty']}")
                time.sleep(0.2)
    
    def update_workout(self,name,duration=None,difficulty=None):
        if name not in self.workouts:
            raise WorkoutNotFoundError(f"Workout {name} not found.")

        if duration :
            self.workouts[name]["duration"] = duration
        if difficulty :
            self.workouts[name]['difficulty'] = difficulty

        self.save_workouts()
        time.sleep(0.5)
        print(f"Workout {name} Updated")

    def delete_workout(self,name):
        if name not in self.workouts:
            raise WorkoutNotFoundError(f"Workout {name} not found.")

        del self.workouts[name]
        self.save_workouts()
        time.sleep(0.5)
        print(f"Workout {name} Deleted")
