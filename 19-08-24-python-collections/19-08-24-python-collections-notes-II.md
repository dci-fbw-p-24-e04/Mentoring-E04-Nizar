
### Working with Sets and Counters

1. **List of Website History**
    ```python
    history = ['facebook','instagram','facebook','youtube','linkedin',
               'facebook','linkedin','youtube','linkedin','reddit']
    ```

2. **Removing Duplicates with a Set**
    ```python
    set_history = set(history)  # we are removing duplicates
    print(set_history)
    ```
   - Converts the `history` list to a set, `set_history`, to remove duplicates.
   - Prints the `set_history`, which contains unique website names.

3. **Converting Set Back to List**
    ```python
    list_of_websites = list(set_history)
    ```
   - Converts the `set_history` back to a list, `list_of_websites`.

4. **Iterating Through the List of Websites**
    ```python
    for website in list_of_websites:
        print(f'user has visited {website}')
    ```
   - Iterates through `list_of_websites` and prints a message for each website indicating that the user has visited it.

5. **Using the Counter from collections Module**
    ```python
    from collections import Counter
    website_count = Counter(history)
    print(website_count)
    ```
   - Imports the `Counter` class from the `collections` module.
   - Creates a `Counter` object, `website_count`, which counts the occurrences of each website in the `history` list.
   - Prints the `website_count`, which shows how many times each website was visited.

### Explanation of Output

1. **Removing Duplicates**
    ```python
    set_history = set(history)
    print(set_history)
    ```
    - Output will be a set with unique website names, e.g., `{'facebook', 'linkedin', 'instagram', 'youtube', 'reddit'}`.

2. **Converting Set to List and Iterating**
    ```python
    list_of_websites = list(set_history)
    for website in list_of_websites:
        print(f'user has visited {website}')
    ```
    - Output will print messages for each unique website:
        ```
        user has visited facebook
        user has visited linkedin
        user has visited instagram
        user has visited youtube
        user has visited reddit
        ```

3. **Counting Occurrences with Counter**
    ```python
    website_count = Counter(history)
    print(website_count)
    ```
    - Output will be a `Counter` object showing the frequency of each website in the `history` list, e.g., `Counter({'facebook': 3, 'linkedin': 3, 'youtube': 2, 'instagram': 1, 'reddit': 1})`.

### Summary
- **Set**: Used to remove duplicates from the list.
- **List**: Converted from set to allow iteration.
- **Counter**: Used to count occurrences of each website in the history.

This approach effectively removes duplicates and counts the frequency of each website visit, leveraging Python's `set` and `collections.Counter` for these tasks.