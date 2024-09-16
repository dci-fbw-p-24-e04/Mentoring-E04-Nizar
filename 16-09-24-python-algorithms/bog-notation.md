Big O notation is a mathematical notation used to describe the efficiency and performance of an algorithm in terms of the time (or space) it takes as the input size grows. It focuses on the upper bound of the algorithm's growth rate, providing a high-level understanding of its behavior for large input sizes.

### Common Big O Notations

1. **O(1) - Constant Time**
2. **O(log n) - Logarithmic Time**
3. **O(n) - Linear Time**
4. **O(n log n) - Log-Linear Time**
5. **O(n^2) - Quadratic Time**
6. **O(2^n) - Exponential Time**
7. **O(n!) - Factorial Time**

### Examples and Code Explanations

#### O(1) - Constant Time
An operation that takes the same amount of time regardless of the input size.

```python
def get_first_element(arr):
    return arr[0]

# Example usage:
arr = [1, 2, 3, 4, 5]
print(get_first_element(arr))  # Output: 1
```
**Explanation**: Accessing the first element of an array is a constant time operation because it doesn't matter how large the array is; it always takes the same amount of time.

#### O(log n) - Logarithmic Time
An algorithm that reduces the problem size by a constant factor each step.

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(arr, 7))  # Output: 6
```
**Explanation**: Binary search repeatedly divides the search interval in half, reducing the problem size logarithmically.

#### O(n) - Linear Time
An algorithm that scales linearly with the input size.

```python
def find_max(arr):
    max_element = arr[0]
    for num in arr:
        if num > max_element:
            max_element = num
    return max_element

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(find_max(arr))  # Output: 10
```
**Explanation**: Finding the maximum element involves checking each element once, resulting in linear time complexity.

#### O(n log n) - Log-Linear Time
An algorithm that performs a linear number of operations for each logarithmic division of the input.

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        merge_sort(left_half)
        merge_sort(right_half)
        
        i = j = k = 0
        
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

# Example usage:
arr = [10, 7, 8, 9, 1, 5]
print(merge_sort(arr))  # Output: [1, 5, 7, 8, 9, 10]
```
**Explanation**: Merge sort divides the array into halves logarithmically and then performs a linear number of operations to merge them.

#### O(n^2) - Quadratic Time
An algorithm that scales quadratically with the input size.

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(arr))  # Output: [11, 12, 22, 25, 34, 64, 90]
```
**Explanation**: Bubble sort compares and swaps adjacent elements, leading to a quadratic number of operations.

#### O(2^n) - Exponential Time
An algorithm whose growth doubles with each additional input.

```python
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Example usage:
print(fibonacci(6))  # Output: 8
```
**Explanation**: Each call to the `fibonacci` function results in two more calls, leading to exponential growth in the number of calls.

#### O(n!) - Factorial Time
An algorithm that scales factorially with the input size.

```python
def permutations(string):
    if len(string) == 1:
        return [string]
    perms = []
    for i in range(len(string)):
        for perm in permutations(string[:i] + string[i+1:]):
            perms.append(string[i] + perm)
    return perms

# Example usage:
print(permutations("abc"))  # Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
```
**Explanation**: Generating all permutations of a string involves factorially many operations as the number of possible permutations of a string of length n is n!.
