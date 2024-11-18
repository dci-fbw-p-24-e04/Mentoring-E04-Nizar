import sys

args = sys.argv[1:]
#m + n
#m - n
#m * n
#m / n
#the arg in args are strings
m = int(args[0])
n = int(args[2])
op = args[1]

if op == '+':
    print(f'the result is {m+n}')

elif op == '-':
    print(f'the result is {m-n}')

elif op == 'x':
    print(f'the result is {m*n}')

elif op == '/':
    try:
        print(f'the result is {m/n}')
    except ZeroDivisionError:
        print("you cannot divide by zero")

else :# 4 ? 7
    print("invalid argument")

