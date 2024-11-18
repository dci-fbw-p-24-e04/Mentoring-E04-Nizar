from planner import WorkoutPlanner,WorkoutNotFoundError,InvalidInputError
from parser_com import create_parser

def main():
    planner = WorkoutPlanner()
    parser = create_parser()

    args = parser.parse_args()
    print(args)
    try :
        if args.command == "add":
            planner.add_workout(args.name,args.duration,args.difficulty)
        elif args.command == 'view':
            planner.view_workouts()

        elif args.command == 'update':
            planner.update_workout(args.name, args.duration, args.difficulty)
        elif args.command == 'delete':
            planner.delete_workout(args.name)
    except (WorkoutNotFoundError,InvalidInputError) as e:
        print("Error",e)

if __name__ == '__main__':
    main()