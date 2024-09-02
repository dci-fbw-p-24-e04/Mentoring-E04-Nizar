#what is a decorator
def add_greeting(func):
    def wrapper(*args,**kwargs):
        result = "Hello "+func(*args,**kwargs)
        return result   
    return wrapper
@add_greeting
def function(first,last):
    return f"{first} {last}"

result = function('John','Doe')
print(result)
#Hello John Doe
print('-'*50)
#we want to measure the excution time of our function
import time

def count_exec_time(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start}s to execute")
        return result
    return wrapper

@count_exec_time
def say_name(first,last):
    time.sleep(2)
    return f"{first} {last}"

result = say_name('John','Doe')
print(result)
print('-'*25)
@count_exec_time
def function(first,last):
    time.sleep(3)
    return f"{first} {last}"

result = function('John','Doe')
print(result)
print('-'*50)
#we need to define a higher order function

def repeat(n):#higher order function : if your decorator takes args
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
                print(result)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    return ('Hi')

say_hi()
print('-'*25)
@repeat(10)
def say_hi():
    return 'Hi'

say_hi()
