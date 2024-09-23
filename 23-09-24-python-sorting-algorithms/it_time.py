import timeit#library to measure the iteration time
import random
from bubbles import bubble_sort


def run_algorithm(source,func,data):
    
    
    setup_code = f"from {source} import {func}"#from bubbles import bubble_sort
    function_call = f"{func}({data})"#bubble_sort(arr)
    time = timeit.repeat(setup=setup_code,stmt=function_call,repeat=3,number=10)
    print(f"Algorithm: {func}. Minimum execution time: {min(time)} s")
    
if __name__ == '__main__':
    array = list(range(50,0,-1))
    run_algorithm(source='bubbles',func='bubble_sort',data=array.copy())
    run_algorithm(source='quicks',func='quick_sort',data=array.copy())