def uppercase_decorator(func):
    def wrapper(name):
        uppercase_name = name.upper()
        return func('WOW'+uppercase_name+'WOW')
    return wrapper

def emphasis_decorator(func):
    def wrapper(name):
        emphasized_name = f"!!!{name}!!!"
        return func(emphasized_name)
    return wrapper

def question_decorator(func):
    def wrapper(name):
        question_name = f"???{name}???"
        return func(question_name)
    return wrapper

@question_decorator
@emphasis_decorator
@uppercase_decorator
def greet(name):
    return (f"Hello, {name}")
print(greet("John") )
print('-'*50)
@uppercase_decorator
@emphasis_decorator
@question_decorator
def greet(name):
    return (f"Hello, {name}")
print(greet("John") )