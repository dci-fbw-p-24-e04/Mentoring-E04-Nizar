import time
def dec_with_parameter(bool_value):
    if bool_value=='True':
        def count_exec_time(func):
            def wrapper(*args,**kwargs):
                start = time.time()
                result = func(*args, **kwargs)
                end = time.time()
                print(f"{func.__name__} call took {end-start}s to execute")
                return result
            return wrapper
        return count_exec_time
    else:
        def no_decorator(func):
            print(f"Decorator is disabled for {func.__name__}, so it will show no execution time.")
            return func
        return no_decorator


#Test cases
@dec_with_parameter('True')
def test_function_1(x, y):
    time.sleep(1)
    return x + y

print(test_function_1(2, 3))

@dec_with_parameter('False')
def test_function_2(x, y):
    time.sleep(1)
    return x * y

print(test_function_2(2, 3))