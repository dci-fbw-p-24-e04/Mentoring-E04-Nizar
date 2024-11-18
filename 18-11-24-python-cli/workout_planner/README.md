## `WorkoutPlanner` System

#### 1. Importing Libraries:
```python
import json
import os
import datetime
import time
from stringcolor import cs
```
- **`json`**: Used to work with JSON data. It allows us to read from and write to JSON files, which is how we store workout and report information.
- **`os`**: Provides functionality to interact with the file system, such as checking if files exist.
- **`datetime`**: Used to work with date and time, which is helpful when adding timestamps to reports.
- **`time`**: Provides various time-related functions. Here, it's used to add delays in print statements to simulate realistic output behavior.
- **`stringcolor.cs`**: A third-party library that allows us to add color to printed text, making the output more readable and visually appealing.

---

#### 2. Defining Constants:
```python
WORKOUT_FILE = 'workout_planner.json'
REPORT_FILE = 'workout_report.json'
```
- **`WORKOUT_FILE`**: Specifies the filename where workout data is stored.
- **`REPORT_FILE`**: Specifies the filename where generated reports will be stored.

---

#### 3. Defining Custom Exceptions:
```python
class WorkoutNotFoundError(Exception): 
    pass

class InvalidInputError(Exception):
    pass
```
- **`WorkoutNotFoundError`**: A custom exception that is raised when an attempt is made to update or delete a workout that doesn't exist.
- **`InvalidInputError`**: A custom exception that is raised when trying to add a workout that already exists, ensuring data integrity.

---

#### 4. The `WorkoutPlanner` Class:
```python
class WorkoutPlanner:
    def __init__(self):
        self.workouts = self.load_workouts()
```
- **`__init__`**: The constructor method that is automatically called when a `WorkoutPlanner` object is created. It initializes the `workouts` attribute by loading existing workouts from the JSON file using the `load_workouts` method.

---

#### 5. Loading Workouts from JSON:
```python
def load_workouts(self):
    if os.path.exists(WORKOUT_FILE):
        with open(WORKOUT_FILE,'r') as file:
            return json.load(file)
    return {}
```
- **`load_workouts`**: This method checks if the `WORKOUT_FILE` exists. If it does, it reads and loads the workout data from the JSON file. If the file doesn’t exist, it returns an empty dictionary.
- **`os.path.exists(WORKOUT_FILE)`**: This checks if the workout file exists in the system.
- **`json.load(file)`**: Reads the workout data from the JSON file and converts it into a Python dictionary.

---

#### 6. Saving Workouts to JSON:
```python
def save_workouts(self):
    with open(WORKOUT_FILE, 'w') as file:
        json.dump(self.workouts, file, indent=4)
```
- **`save_workouts`**: Writes the current workout data stored in `self.workouts` to the `WORKOUT_FILE` in JSON format.
- **`json.dump(self.workouts, file, indent=4)`**: Writes the dictionary to the file with pretty printing (`indent=4`).

---

#### 7. Adding New Workouts:
```python
def add_workouts(self, name, duration, difficulty):
    if name in self.workouts:
        raise InvalidInputError(f"Workout '{name}' already exists.")
    self.workouts[name] = {"duration": duration, "difficulty": difficulty}
    time.sleep(0.5)
    self.save_workouts()
    print(f"Added workout: {name}")
```
- **`add_workouts`**: Adds a new workout to the `workouts` dictionary. It accepts the workout's `name`, `duration`, and `difficulty` as input.
- **`raise InvalidInputError(...)`**: Ensures no duplicate workout names are allowed by raising an error if the workout already exists.
- **`self.save_workouts()`**: Saves the updated workout data to the JSON file.
- **`time.sleep(0.5)`**: Adds a 0.5-second delay to make the output more realistic.
- **`print(...)`**: Displays a success message once the workout is added.

---

#### 8. Viewing Workouts:
```python
def view_workouts(self):
    if not self.workouts:
        print(cs('No workouts found get up and do something', 'red'))
    else:
        for name, details in self.workouts.items():
            print(f"Workout: {name}, Duration: {details['duration']}, Difficulty: {details['difficulty']}")
            time.sleep(0.2)
```
- **`view_workouts`**: Displays all the workouts stored in `self.workouts`.
- **`if not self.workouts:`**: If no workouts are found, a message in red color is printed using `cs`.
- **`for name, details in self.workouts.items()`**: Iterates through all the workouts and prints their name, duration, and difficulty.
- **`time.sleep(0.2)`**: Adds a small delay between printing each workout for smoother output.

---

#### 9. Updating an Existing Workout:
```python
def update_workout(self, name, duration=None, difficulty=None):
    if name not in self.workouts:
        raise WorkoutNotFoundError(f"Workout {name} not found.")
    if duration:
        self.workouts[name]['duration'] = duration
    if difficulty:
        self.workouts[name]['difficulty'] = difficulty
    self.save_workouts()
    time.sleep(0.5)
    print(cs(f"Updated workout: {name}", 'green'))
```
- **`update_workout`**: Updates the `duration` and/or `difficulty` of an existing workout.
- **`raise WorkoutNotFoundError(...)`**: If the workout doesn't exist, it raises a custom error.
- **`if duration: ...` and `if difficulty: ...`**: Updates the respective fields if new values are provided.
- **`self.save_workouts()`**: Saves the updated workouts to the JSON file.
- **`print(...)`**: Displays a success message in green after updating the workout.

---

#### 10. Deleting a Workout:
```python
def delete_workout(self, name):
    if name not in self.workouts:
        raise WorkoutNotFoundError(f"Workout {name} not found.")
    del self.workouts[name]
    self.save_workouts()
    time.sleep(0.5)
    print(cs(f"Deleted workout: {name}", 'yellow'))
```
- **`delete_workout`**: Deletes an existing workout.
- **`raise WorkoutNotFoundError(...)`**: Raises an error if the workout is not found.
- **`del self.workouts[name]`**: Deletes the workout from the dictionary.
- **`self.save_workouts()`**: Saves the updated workout list.
- **`print(cs(..., 'yellow'))`**: Prints a message in yellow, confirming that the workout was deleted.

---

### Additional Details:
- **Color Output**: The `stringcolor.cs` function is used to add colored text in the terminal for better user interaction.
- **Error Handling**: Custom exceptions (`WorkoutNotFoundError` and `InvalidInputError`) are used to handle specific error conditions, such as missing workouts or duplicate names.

## Creating commands

### Explanation of `argparse` Code for CLI Workout Planner

---

#### 1. **Creating the Argument Parser:**
```python
def create_parser():
    parser = argparse.ArgumentParser(description="Your new workout planner using CLI")
    subparsers = parser.add_subparsers(dest='command')
```
- **`argparse.ArgumentParser()`**: Creates the main parser for the CLI tool. The `description` argument provides a short explanation of the program.
- **`subparsers = parser.add_subparsers(dest='command')`**: Creates subparsers, each of which will handle different commands (e.g., `add`, `view`, `update`, `delete`). The `dest='command'` specifies where the selected sub-command will be stored.

---

#### 2. **Adding a Workout Sub-Command:**
```python
# add workout parser
add_workout_parser = subparsers.add_parser('add', help='Add new workout')
add_workout_parser.add_argument('name', type=str)
add_workout_parser.add_argument('duration', type=int)
add_workout_parser.add_argument('difficulty', type=str, choices=['easy', 'medium', 'hard'])
```
- **`subparsers.add_parser('add')`**: Adds a sub-command called `add` for adding new workouts. This allows the user to type `add` in the terminal and provide the required arguments to add a workout.
- **`add_workout_parser.add_argument()`**: Defines the arguments that the `add` command accepts:
  - **`name`**: The name of the workout (string).
  - **`duration`**: The duration of the workout in minutes (integer).
  - **`difficulty`**: The difficulty level of the workout, which must be one of the choices: `'easy'`, `'medium'`, or `'hard'`.

---

#### 3. **Viewing Workouts Sub-Command:**
```python
subparsers.add_parser('view', help='View all workouts')
```
- **`subparsers.add_parser('view')`**: Creates a `view` sub-command to display all the workouts when executed. No arguments are required for this command, and the help message provides a brief explanation of its function.

---

#### 4. **Updating a Workout Sub-Command:**
```python
# update workout parser
update_parser = subparsers.add_parser('update', help='Update new workout')
update_parser.add_argument('name', type=str)
update_parser.add_argument('--duration', type=int)  # --optional
update_parser.add_argument('--difficulty', type=str, choices=['easy', 'medium', 'hard'])
```
- **`subparsers.add_parser('update')`**: Adds an `update` sub-command for modifying an existing workout. This allows the user to update the duration and/or difficulty of an existing workout.
- **Arguments**:
  - **`name`**: The name of the workout to update (required).
  - **`--duration`**: The new duration (optional). The `--` prefix makes it an optional argument.
  - **`--difficulty`**: The new difficulty level (optional) with the same choices as before: `'easy'`, `'medium'`, or `'hard'`.

---

#### 5. **Deleting a Workout Sub-Command:**
```python
# delete workout parser
delete_parser = subparsers.add_parser('delete', help='Delete a workout')
delete_parser.add_argument('name', type=str, help='Name of the workout to delete')
```
- **`subparsers.add_parser('delete')`**: Adds a `delete` sub-command for removing a workout.
- **Argument**:
  - **`name`**: The name of the workout to delete (required).

---

### Summary of Commands:
- **`add`**: Allows users to add a new workout by specifying its name, duration, and difficulty.
- **`view`**: Displays all saved workouts.
- **`update`**: Allows users to update an existing workout by providing the name and optionally changing the duration and/or difficulty.
- **`delete`**: Removes a workout by its name.

## The Main Script


#### 1. **Imports**:
```python
from planner import WorkoutPlanner, InvalidInputError, WorkoutNotFoundError
from parser_commands import create_parser
```
- **`from planner import WorkoutPlanner, InvalidInputError, WorkoutNotFoundError`**: Imports the `WorkoutPlanner` class and custom exceptions (`InvalidInputError`, `WorkoutNotFoundError`) from the `planner` module.
- **`from parser_commands import create_parser`**: Imports the function `create_parser()` from `parser_commands.py` (which defines the argument parsing logic).


---

#### 2. **Main Function**:
```python
def main():
    workout_planner = WorkoutPlanner()
    parser = create_parser()
    args = parser.parse_args()
```
- **`workout_planner = WorkoutPlanner()`**: Creates an instance of `WorkoutPlanner` to manage the workouts.
- **`parser = create_parser()`**: Initializes the argument parser for handling command-line input.
- **`args = parser.parse_args()`**: Parses the command-line arguments provided by the user when running the program.

---

#### 3. **Handling Commands**:
```python
try:
    if args.command == 'add':
        workout_planner.add_workouts(args.name, args.duration, args.difficulty)
    elif args.command == 'view':
        workout_planner.view_workouts()
    elif args.command == 'update':
        workout_planner.update_workout(args.name, args.duration, args.difficulty)
    elif args.command == 'delete':
        workout_planner.delete_workout(args.name)
    else:
        parser.print_help()
```
- **Command Execution**: Based on the `command` argument parsed by `argparse` (stored in `args.command`), the program performs different actions:
  - **`add`**: Calls `add_workouts()` method with the provided workout `name`, `duration`, and `difficulty`.
  - **`view`**: Calls `view_workouts()` to display all workouts.
  - **`update`**: Calls `update_workout()` with the `name` and optional `duration` and `difficulty` arguments.
  - **`delete`**: Calls `delete_workout()` to remove a workout by its name.
  - **Invalid command**: If no valid command is given, it prints the help message using `parser.print_help()`.

---

#### 4. **Exception Handling**:
```python
except (WorkoutNotFoundError, InvalidInputError) as e:
    print(f"Error: {e}")
```
- **`try`/`except` Block**: Wraps the command execution in a `try` block to catch any custom exceptions:
  - **`WorkoutNotFoundError`**: Raised if a workout does not exist when trying to update or delete it.
  - **`InvalidInputError`**: Raised if an invalid input is provided (e.g., trying to add a workout that already exists).
- **Error Message**: If an exception occurs, an error message is printed.

---

#### 5. **Program Entry Point**:
```python
if __name__ == '__main__':
    main()
```
- **`if __name__ == '__main__'`**: Ensures that the `main()` function is only executed when the script is run directly, not when it's imported as a module in another script.

---

### How the Program Works

1. When the script is run, the command-line arguments are parsed using `argparse`.
2. Based on the command (e.g., `add`, `view`, `update`, `delete`), the corresponding method in the `WorkoutPlanner` class is called.
3. If an error occurs (e.g., the workout doesn't exist), an appropriate custom exception is raised and caught, displaying an error message.
4. The CLI provides feedback or performs actions such as adding, viewing, updating, or deleting workouts from the JSON file.