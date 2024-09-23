import matplotlib.pyplot as plt
import timeit

def measure_time(source,algorithm, arr):
    setup_code = f"from {source} import {algorithm}"
    stmt = f"{algorithm}({arr})"
    execution_time = timeit.timeit(stmt, setup=setup_code, number=1)
    return execution_time*1000#in ms 


input_sizes = [50,100,200,500,750]
bubble_times = []
quick_times = []
for size in input_sizes:
    input_array = list(range(size, 0, -1)) #reversed list
    time = measure_time(source='bubbles',algorithm='bubble_sort',arr=input_array.copy())
    bubble_times.append(time)
    time_1 = measure_time(source='quicks',algorithm='quick_sort',arr=input_array.copy())
    quick_times.append(time_1)
    
plt.plot(input_sizes,bubble_times,label='bubble sort')
plt.plot(input_sizes,quick_times,label='quick sort')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Time Complexity of Sorting Algorithms')
plt.legend()
plt.show() 


