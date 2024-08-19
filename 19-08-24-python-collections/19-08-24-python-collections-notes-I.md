
### Working with Lists, Tuples, and Dictionaries

1. **Lists: Mutable**
    ```python
    list_of_fruits = [
        "apple",
        "banana",
        "kiwi",
        "orange",
        "mango"
    ]
    ```

2. **Tuples: Immutable**
    ```python
    user_data = ('nizar', 28, 'nizar@python.py')
    ```

3. **Dictionaries: Mutable**
    ```python
    store_items = {
        'laptop': 1000,
        'smartphone': 500,
        'plasmaTV': 600
    }
    ```

4. **Single-element Tuple and List**
    ```python
    tuple_with_one_element = (0,)
    list_with_one_element = ['julie']
    dict_with_one_item = {'name': 'Taras'}
    print(type(tuple_with_one_element))
    ```
   - This prints the type of `tuple_with_one_element`, which is `<class 'tuple'>`.

5. **Iterating over a List**
    ```python
    for fruit in list_of_fruits:
        print(fruit)
    ```
   - Iterates through each element in `list_of_fruits` and prints it.

6. **Iterating using `range`**
    ```python
    for i in range(len(list_of_fruits)):
        print(list_of_fruits[i])
    ```
   - Iterates using index values and prints each element in `list_of_fruits`.

7. **Joining List Elements into a String**
    ```python
    string_of_fruit = ' '.join(list_of_fruits)  # is string
    print(string_of_fruit)
    ```
   - Joins elements of `list_of_fruits` into a single string separated by spaces.

8. **Iterating through a Tuple**
    ```python
    for data in user_data:
        print(data)
    ```
   - Prints each element in the tuple `user_data`.

9. **Iterating through a Tuple using `range`**
    ```python
    for i in range(len(user_data)):
        print(user_data[i])
    ```
   - Prints each element in `user_data` using index values.

10. **Unpacking a Tuple**
    ```python
    user_data = ('nizar', '28', 'nizar@python.py')
    name, age, email = user_data  # unpacking
    print(name)
    print(age)
    print(email)
    ```
    - Assigns each element of `user_data` to the variables `name`, `age`, and `email`.
    - Prints the unpacked values.

11. **Joining Tuple Elements into a String**
    ```python
    string_data = ' '.join(user_data)
    print(string_data)
    ```
   - Joins elements of `user_data` into a single string separated by spaces.

12. **Iterating through a Dictionary**
    ```python
    for i in store_items:
        print(i)  # will print the keys
    ```
   - Prints each key in `store_items`.

13. **Iterating through Dictionary Items**
    ```python
    for item in store_items.items():
        print(item)
    ```
   - Prints each key-value pair as a tuple.

14. **Unpacking Dictionary Items**
    ```python
    for key, val in store_items.items():
        print(f"item {key}, price {val}")
    ```
   - Prints each key-value pair in a formatted string.

15. **Iterating through Dictionary Values**
    ```python
    for val in store_items.values():
        print(val)
    ```
   - Prints each value in `store_items`.

### Summary
- Demonstrates different data structures: lists, tuples, and dictionaries.
- Shows how to iterate through these structures using loops and unpacking.
- Utilizes string methods to join elements.
- Highlights the immutability of tuples and mutability of lists and dictionaries.