import argparse

def create_parser():
    parser = argparse.ArgumentParser(description="Your new trainer using CLI")
    subparsers = parser.add_subparsers(dest="command")
    #add workout command
    add_workout_parser = subparsers.add_parser('add',help="Add new workout")
    add_workout_parser.add_argument('name',type=str)
    add_workout_parser.add_argument("duration",type=int)
    add_workout_parser.add_argument("difficulty",type=str,choices=['easy','medium','hard'])
    #view workout parser
    subparsers.add_parser('view',help='View all workouts')
    #update workout parser
    update_workout_parser = subparsers.add_parser("update",help="Update a workout")
    update_workout_parser.add_argument("name",type=str)
    update_workout_parser.add_argument("--duration",type=int)
    update_workout_parser.add_argument('--difficulty',type=str,choices=['easy','medium','hard'])
    #delete workout parser
    delete_workout_parser = subparsers.add_parser('delete', help='Delete a workout')
    delete_workout_parser.add_argument('name', type=str, help='Name of the workout to delete')

    return parser
