import re

def valid_username(username):
    pattern=r"\w+\d{2,}$"#nizar123,nizar_something123
    match= re.match(pattern,username)
    if match:
        return f"{username} is valid"
    else :
        return f"{username} is not valid try again"
        
username = input('Enter your username ')
print(valid_username(username))

def valid_phone_number(phone_number):
    pattern = r"\b[\+]?[(]?[1-9]{2,3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}"
    match = re.findall(pattern,phone_number)
    return match

list_of_numbers = """this is my number +919 367788755 and this my other number 8989829304"""
print(valid_phone_number(list_of_numbers))
print('-'*50)
def valid_date(date):#yyyy-mm-dd
    pattern = r"(19|20)\d\d-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])"
    match = re.match(pattern,date)
    if match :
        print('date is valid')
    else:
        print('not valid')
        
        
valid_date('1998-06-12')
valid_date('1800-06-12')
valid_date('1998-13-12')
valid_date('1998-06-42')
