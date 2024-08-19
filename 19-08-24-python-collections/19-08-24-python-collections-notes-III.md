
### List Comprehension for Mapping

1. **Square Numbers in List**
    ```python
    list_of_nums = [1,2,3,4,5,6]
    squared_nums = [i**2 for i in list_of_nums]  # [1, 4, 9, 16, 25, 36]
    print(squared_nums)
    print('-'*30)
    ```
   - Creates a new list `squared_nums` where each element is the square of the corresponding element in `list_of_nums`.
   - Outputs: `[1, 4, 9, 16, 25, 36]`.

2. **Abbreviate Colors**
    ```python
    colors = ["red", "green", "blue", "yellow"]  # ===> ['R', 'G', 'B', 'Y']
    accr = [color[0].upper() for color in colors]
    print(accr)
    print('-'*30)
    ```
   - Creates a new list `accr` where each element is the first letter of the corresponding color in uppercase.
   - Outputs: `['R', 'G', 'B', 'Y']`.

### List Comprehension for Filtering

3. **Filter Even and Odd Numbers**
    ```python
    list_of_ints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    even_nums = [i for i in list_of_ints if i % 2 == 0]
    odd_nums = [i for i in list_of_ints if i % 2 != 0]
    print('even', even_nums)
    print('odd', odd_nums)
    print("-" * 50)
    ```
   - Creates `even_nums` list with all even numbers from `list_of_ints`.
   - Creates `odd_nums` list with all odd numbers from `list_of_ints`.
   - Outputs: `even [2, 4, 6, 8, 10, 12]`, `odd [1, 3, 5, 7, 9, 11]`.

4. **Filter Fruits Containing 'a'**
    ```python
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    fruit_with_a = [fruit for fruit in fruits if 'a' in fruit]
    fruit_with_a_2 = [fruit for fruit in fruits if fruit.count('a') > 0]
    print(fruit_with_a)
    print(fruit_with_a_2)
    print("-" * 50)
    ```
   - Creates `fruit_with_a` list with all fruits containing the letter 'a'.
   - Another method, `fruit_with_a_2`, achieves the same result using `count('a') > 0`.
   - Outputs: `['apple', 'banana', 'mango']`.

### List Comprehension with Conditional Logic

5. **FizzBuzz Using List Comprehension**
    ```python
    list_of_ints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    fizzbuzz = ["fizz" if i % 3 == 0 else "buzz" for i in list_of_ints]
    print(fizzbuzz)
    print("-" * 50)
    ```
   - Creates `fizzbuzz` list where each element is "fizz" if the number is divisible by 3, otherwise "buzz".
   - Outputs: `['buzz', 'buzz', 'fizz', 'buzz', 'buzz', 'fizz', 'buzz', 'buzz', 'fizz', 'buzz', 'buzz', 'fizz']`.

### Nested List Comprehension

6. **Flattening and Squaring Nested Lists**
    ```python
    nums = [[1, 2, 3], [4, 5, 6, 7], [8, 9]]
    flat_nums = [x for n in nums for x in n]
    squared_nested = [x**2 for n in nums for x in n]
    list_of_sums = [sum(n) for n in nums]
    print(flat_nums)
    print(squared_nested)
    print(list_of_sums)
    ```
   - **Flatten Nested List:** Creates `flat_nums` list which flattens the nested lists in `nums`.
     - Outputs: `[1, 2, 3, 4, 5, 6, 7, 8, 9]`.
   - **Square Nested List Elements:** Creates `squared_nested` list where each element in the nested lists is squared.
     - Outputs: `[1, 4, 9, 16, 25, 36, 49, 64, 81]`.
   - **Sum of Nested Lists:** Creates `list_of_sums` list where each element is the sum of the corresponding nested list in `nums`.
     - Outputs: `[6, 22, 17]`.

### Summary
- **Mapping with List Comprehension:** Efficiently creates new lists by applying an operation to each element.
- **Filtering with List Comprehension:** Efficiently creates new lists by including elements that meet a condition.
- **Nested List Comprehension:** Allows working with nested structures in a concise manner.