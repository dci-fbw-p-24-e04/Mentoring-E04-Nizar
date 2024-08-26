
### 1. Valid Username Function

```python
import re

def valid_username(username):
    pattern = r"\w+\d{2,}$"  # Matches usernames with letters/numbers followed by at least two digits
    match = re.match(pattern, username)
    if match:
        return f"{username} is valid"
    else:
        return f"{username} is not valid, try again"

username = input('Enter your username ')
print(valid_username(username))
```

- **Explanation**:
  - **`pattern = r"\w+\d{2,}$"`**:
    - **`\w+`**: Matches one or more word characters (letters, digits, or underscores).
    - **`\d{2,}$`**: Ensures that the username ends with at least two digits.
  - **`re.match(pattern, username)`**: Checks if the username matches the pattern.
  - The function returns whether the username is valid or not.

- **Example**:
  - Input: `nizar123` → Output: "nizar123 is valid"
  - Input: `nizar` → Output: "nizar is not valid, try again"

### 2. Valid Phone Number Function

```python
def valid_phone_number(phone_number):
    pattern = r"\b[\+]?[(]?[1-9]{2,3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}"
    match = re.findall(pattern, phone_number)
    return match

list_of_numbers = """this is my number +919 367788755 and this my other number 8989829304"""
print(valid_phone_number(list_of_numbers))
```

- **Explanation**:
  - **`pattern = r"\b[\+]?[(]?[1-9]{2,3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}"`**:
    - **`\b`**: Word boundary to ensure accurate matching.
    - **`[\+]?`**: Optional "+" sign for international numbers.
    - **`[(]?[1-9]{2,3}[)]?`**: Matches country codes (2 or 3 digits) optionally enclosed in parentheses.
    - **`[-\s\.]?`**: Allows for separators like hyphens, spaces, or dots.
    - **`[0-9]{3}`**: Matches the next 3 digits (area code).
    - **`[0-9]{4,6}`**: Matches 4 to 6 digits (main phone number).
  - **`re.findall(pattern, phone_number)`**: Finds all matching phone numbers in the input string.

- **Output**:
  - The function prints a list of all valid phone numbers found in the input string.

### 3. Valid Date Function

```python
def valid_date(date):  # yyyy-mm-dd
    pattern = r"(19|20)\d\d-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])"
    match = re.match(pattern, date)
    if match:
        print('date is valid')
    else:
        print('not valid')

valid_date('1998-06-12')
valid_date('1800-06-12')
valid_date('1998-13-12')
valid_date('1998-06-42')
```

- **Explanation**:
  - **`pattern = r"(19|20)\d\d-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])"`**:
    - **`(19|20)\d\d`**: Matches years starting with 19 or 20, followed by two digits.
    - **`(0[1-9]|1[0-2])`**: Matches months from 01 to 12.
    - **`(0[1-9]|[12][0-9]|3[01])`**: Matches valid days in a month (01-31).
  - **`re.match(pattern, date)`**: Checks if the date matches the pattern.

- **Output**:
  - The function prints whether the provided date is valid or not.

### Summary:

- **`valid_username`**: Validates if a username ends with at least two digits.
- **`valid_phone_number`**: Extracts valid phone numbers from a string.
- **`valid_date`**: Validates a date string in the `yyyy-mm-dd` format, ensuring that the date is realistic and well-formed.