
### 1. Email Finder Function

```python
import re

text = """
Hello, you can contact John at john.doe@example.com for sales inquiries.
For support, reach out to Jane at jane_doe123@service.net.
Additionally, our HR department can be contacted via hr@company.org.
"""

def email_finder(text):
    pattern = r"\w+[\w.%+-]*@\w+\.\w{2,3}"
    matches = re.findall(pattern, text)
    return matches

emails_list = email_finder(text)
for email in emails_list:
    print(f"{email} found at {text.find(email)}")
```

- **Explanation**:
  - **`pattern = r"\w+[\w.%+-]*@\w+\.\w{2,3}"`**:
    - **`\w+`**: Matches one or more word characters (letters, digits, or underscores).
    - **`[\w.%+-]*`**: Matches zero or more characters that can be word characters, dots, percentages, pluses, or hyphens.
    - **`@\w+`**: Matches the "@" symbol followed by one or more word characters.
    - **`\.\w{2,3}`**: Matches a dot followed by 2 or 3 word characters, which is typical for domain extensions (e.g., .com, .net, .org).
  - **`re.findall(pattern, text)`**: Finds all matches of the pattern in the provided text.
  - **`text.find(email)`**: Finds the position of each email in the original text.

- **Output**: The code prints each email found in the text along with its position.

### 2. Data Encryption Function

```python
def encrypt_data(text, c=0):
    pattern = r"\w+[\w.%+-]*@\w+\.\w{2,3}"
    res = re.sub(pattern, '***********', text, count=c)
    return res

new_text = encrypt_data(text)
print(new_text)
print('-'*50)
new_text = encrypt_data(text, 1)
print(new_text)
print('-'*50)
new_text = encrypt_data(text, 2)
print(new_text)
```

- **Explanation**:
  - **`encrypt_data(text, c=0)`**: This function replaces email addresses in the text with "***********".
  - **`re.sub(pattern, '***********', text, count=c)`**:
    - **`re.sub`**: Substitutes matches of the pattern with the given replacement string.
    - **`count=c`**: Limits the number of replacements to `c`. If `c=0`, all matches are replaced (the default behavior).
  - The function is called three times:
    - **`encrypt_data(text)`**: Replaces all email addresses.
    - **`encrypt_data(text, 1)`**: Replaces the first email address only.
    - **`encrypt_data(text, 2)`**: Replaces the first two email addresses.

- **Output**:
  - The original text is printed with the email addresses replaced by "***********" as per the specified count.

### Summary:

- **Email Finding**: The `email_finder` function identifies and prints the email addresses within a given text.
- **Data Encryption**: The `encrypt_data` function replaces email addresses with a placeholder, demonstrating how you can protect or anonymize sensitive information in text data. The function's flexibility in choosing how many email addresses to replace (via the `count` parameter) allows for tailored data protection.