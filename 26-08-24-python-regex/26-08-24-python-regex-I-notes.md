
### 1. Matching Strings that Start with a Pattern

```python
import re  # Regular expressions

string_1 = 'hello'
pattern = r"^he"  # ^ means the string should start with 'he'
match = re.match(pattern, string_1)
print(match)  # <re.Match object; span=(0, 2), match='he'>
print(match.group())  # 'he'
if match:
    print('the string is matching our pattern')
else:
    print('no match try later')
```

- **Explanation**:
  - **`pattern = r"^he"`**: The `^` symbol specifies that the string should start with "he".
  - **`re.match(pattern, string_1)`**: Matches the pattern at the beginning of `string_1`.
  - **Output**: It matches "he" at the start of "hello", so it prints that the string matches the pattern.

### 2. Matching Strings that End with a Pattern

```python
print('-'*50)
string = 'hellop'
pattern = r"p$"  # $ means the string should end with 'p'
match = re.findall(pattern, string)
print(match)  # ['p']
if match:
    print('the string is matching our pattern')
else:
    print('no match try later')
```

- **Explanation**:
  - **`pattern = r"p$"`**: The `$` symbol specifies that the string should end with "p".
  - **`re.findall(pattern, string)`**: Finds all occurrences of the pattern. Here, it finds "p" at the end of "hellop".
  - **Output**: The pattern is found, so it prints that the string matches the pattern.

### 3. Matching Strings with a Specific Pattern

```python
print('-'*50)
pattern = r"he..o"  # . matches any character
text_1 = "hel1o"
text_2 = "he12o"
text_3 = "hellllo"
print(re.match(pattern, text_1))  # Match
print(re.match(pattern, text_2))  # Match
print(re.match(pattern, text_3))  # No match
```

- **Explanation**:
  - **`pattern = r"he..o"`**: The `.` symbol matches any character. This pattern expects "he" followed by any two characters and then "o".
  - **Output**:
    - "hel1o" and "he12o" match the pattern.
    - "hellllo" does not match because it has more than two characters between "he" and "o".

### 4. Matching Strings that Start with 'H' or 'h' and End with 'l'

```python
print('-'*50)
pattern = r"^[Hh].*l$"  # ^ start, .* any character(s), $ end
text_1 = "Helllllooooo"
text_2 = "Hell"
text_3 = "hierarchical"
print(re.match(pattern, text_1))  # Match
print(re.match(pattern, text_2))  # Match
print(re.match(pattern, text_3))  # Match
```

- **Explanation**:
  - **`pattern = r"^[Hh].*l$"`**: This pattern matches strings that start with "H" or "h" and end with "l".
  - **Output**:
    - All the provided texts match the pattern.

### 5. Extracting Years from a String

```python
print('-'*50)
history = '''and then in the year 1906 something happened
and in the year 1405 nothing happened and after that in year 1784
the weather was nice and the year 501 it was raining and we ate 124566978 chicken wings'''
# We are extracting the year

pattern_1 = r"\s\d+"  # Any digit(s) following a whitespace
print(re.findall(pattern_1, history))  # [' 1906', ' 1405', ' 1784', ' 501', ' 124566978']

pattern_2 = r"\s\d{4}\s"  # Exactly 4 digits following and preceding a whitespace
print(re.findall(pattern_2, history))  # [' 1906 ', ' 1405 ', ' 1784 ']

pattern_3 = r"\s\d{3,4}\s"  # 3 or 4 digits following and preceding a whitespace
print(re.findall(pattern_3, history))  # [' 1906 ', ' 1405 ', ' 1784 ', ' 501 ']

christian_pattern = r"(?<!\d)\d{3,4}(?!\d)"  # 3 or 4 digits not surrounded by other digits
print(re.findall(christian_pattern, history))  # ['1906', '1405', '1784', '501']
```

- **Explanation**:
  - **`pattern_1 = r"\s\d+"`**: Matches any sequence of digits preceded by a whitespace.
  - **`pattern_2 = r"\s\d{4}\s"`**: Matches exactly 4 digits preceded and followed by a whitespace.
  - **`pattern_3 = r"\s\d{3,4}\s"`**: Matches sequences of 3 or 4 digits with whitespace around them.
  - **`christian_pattern = r"(?<!\d)\d{3,4}(?!\d)"`**: Uses lookbehind and lookahead to match 3 or 4 digits that are not surrounded by other digits.
  - **Output**:
    - `pattern_1`: Finds all digit sequences.
    - `pattern_2` and `pattern_3`: Focus on finding year-like patterns.
    - `christian_pattern`: More precisely isolates year-like patterns without additional surrounding digits.
