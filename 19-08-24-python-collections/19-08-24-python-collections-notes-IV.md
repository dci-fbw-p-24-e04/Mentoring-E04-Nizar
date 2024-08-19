### Using List Comprehensions and Lambda Functions

#### Capitalizing Items

1. **List Comprehension for Capitalizing Items:**
    ```python
    items = ["apple", "banana", "coconuts", "orange", "kiwi"]
    items_title = [item.title() for item in items]
    print(items_title)
    ```
    - Creates a new list `items_title` where each item is capitalized using the `title()` method.
    - Outputs: `['Apple', 'Banana', 'Coconuts', 'Orange', 'Kiwi']`.

2. **Using `map` and Lambda for Capitalizing Items:**
    ```python
    print('-'*50)
    titled_items = map(lambda x: x.title(), items)
    print(list(titled_items))
    ```
    - Applies the `title()` method to each item in `items` using `map` and a lambda function.
    - Converts the map object to a list and prints it.
    - Outputs: `['Apple', 'Banana', 'Coconuts', 'Orange', 'Kiwi']`.

#### Filtering Prices

3. **Using `filter` and Lambda for Prices Less Than 10:**
    ```python
    print('-'*50)
    prices = [12, 15, 2, 7, 10, 8, 5]
    less_than_10 = filter(lambda x: x < 10, prices)
    print(list(less_than_10))
    ```
    - Filters `prices` to include only those values less than 10 using `filter` and a lambda function.
    - Converts the filter object to a list and prints it.
    - Outputs: `[2, 7, 8, 5]`.

#### Filtering Emails

4. **Using `filter` and Lambda for Safe Emails:**
    ```python
    print('-'*50)
    emails = [
        'alice@example.com',
        'bob@example.net',
        'charlie@example.org',
        'dave@example.com',
        'eve@example.net',
        'alien@invade.mars'
    ]
    safe_email = list(filter(lambda email: not email.endswith('.mars'), emails))
    print(safe_email)
    ```
    - Filters `emails` to exclude those ending with '.mars' using `filter` and a lambda function.
    - Converts the filter object to a list and prints it.
    - Outputs: `['alice@example.com', 'bob@example.net', 'charlie@example.org', 'dave@example.com', 'eve@example.net']`.

#### Sorting Students

5. **Sorting Students by Name:**
    ```python
    print('-'*50)
    students = [("John", 90, 2.5), ("Jane", 85, 3.2), ("Joe", 80, 0.1), ("Jack", 95, 1.5)]
    sorted_by_name = sorted(students, key=lambda x: x[0])
    print(sorted_by_name)
    ```
    - Sorts `students` by the first element (name) of each tuple using `sorted` and a lambda function.
    - Outputs: `[('Jack', 95, 1.5), ('Jane', 85, 3.2), ('Joe', 80, 0.1), ('John', 90, 2.5)]`.

6. **Sorting Students by Grade (Ascending):**
    ```python
    sorted_by_grade = sorted(students, key=lambda x: x[1])
    print(sorted_by_grade)
    ```
    - Sorts `students` by the second element (grade) of each tuple in ascending order using `sorted` and a lambda function.
    - Outputs: `[('Joe', 80, 0.1), ('Jane', 85, 3.2), ('John', 90, 2.5), ('Jack', 95, 1.5)]`.

7. **Sorting Students by Grade (Descending):**
    ```python
    sorted_by_grade = sorted(students, key=lambda x: x[1], reverse=True)
    print(sorted_by_grade)
    ```
    - Sorts `students` by the second element (grade) of each tuple in descending order using `sorted` and a lambda function with `reverse=True`.
    - Outputs: `[('Jack', 95, 1.5), ('John', 90, 2.5), ('Jane', 85, 3.2), ('Joe', 80, 0.1)]`.

### Summary
- **List Comprehension:** Provides a concise way to create lists by applying an expression to each element in an iterable.
- **`map` and `filter` with Lambda Functions:** Offers functional programming approaches to transform and filter iterables.
- **Sorting with `sorted` and Lambda Functions:** Allows for custom sorting based on key functions.