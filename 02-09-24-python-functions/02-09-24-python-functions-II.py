import time
def decorate(flag=False):#higher order function
    def count_time_exec(function):#decorator
        def wrapper(*args,**kwargs):#wrapper
            if flag == True:
                start = time.time()
                result = function(*args,**kwargs)
                end = time.time()
                exec_time = end-start
                print(f'{function.__name__} took {exec_time:.2f}s to execute')
                return result
            else: 
                print(f'{function.__name__} is just called')
                result = function(*args,**kwargs)
                return result
        return wrapper
    return count_time_exec

@decorate(flag=False)
def func(first,last)->str:
    time.sleep(2)
    return f'{first},{last}'     

print(func('nizar','py')) 
print('-'*50)
@decorate(flag=True)
def func(first,last)->str:
    time.sleep(2)
    return f'{first},{last}'     

print(func('nizar','py')) 
print('-'*50)
from datetime import datetime
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} at {datetime.now()} with args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log# a good way to keep track of your functions
def add(x, y):
    return x + y 

print(add(5,3))