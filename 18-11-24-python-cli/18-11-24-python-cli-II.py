import sys

args = sys.argv # arguments vector

print(args)
#['18-11-24-python-cli-II.py', 'Hello', 'there', 'amazing', 'mind']
#args[0] stands for the file name
print(args[1:])


def help():#help or -h
    print("this function is a help function")


def make_file(filename):#makefile or -mf
    with open(filename, "w") as file:
        file.write("welcome to cli course")


def create_table(table):#createtable or -ct
    print(f"table {table} was created")

extra_args = args[1:]

if "help" in extra_args or "-h" in extra_args:
    help()

if "makefile" in extra_args or "-mf" in extra_args:
    make_file('somefile.txt')

if "createtable" in extra_args or "-ct" in extra_args:
    create_table("sometable")