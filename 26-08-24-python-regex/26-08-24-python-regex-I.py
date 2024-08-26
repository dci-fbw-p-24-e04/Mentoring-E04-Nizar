import re#regular expressions 

string_1 = 'hello'
pattern = r"^he"# ^ means starts with 'he'
match = re.match(pattern,string_1)
print(match)
print(match.group())
if match:
    print('the string is matching our pattern')
else:
    print('no match try later')
print('-'*50) 
string = 'hellop'
pattern =r"p$"
match = re.findall(pattern,string)
print(match)
if match:
    print('the string is matching our pattern')
else:
    print('no match try later')
    
print('-'*50) 
pattern = r"he..o"#. is any character
text_1 = "hel1o"
text_2 = "he12o"
text_3 = "hellllo"
print(re.match(pattern,text_1))
print(re.match(pattern,text_2))
print(re.match(pattern,text_3))
print('-'*50) 
pattern=r"^[Hh].*l$"
text_1 = "Helllllooooo"
text_2 ="Hell"
text_3 = "hierarchical"
print(re.match(pattern,text_1))
print(re.match(pattern,text_2))
print(re.match(pattern,text_3))
print('-'*50) 
history = '''and then in the year 1906 something happened
and in the year 1405 nothing happened and after that in year 1784
the weather was nice and the year 501 it was raining and we ate 124566978 chicken wings'''
#we are extracting the year
pattern_1 = r"\s\d+"
print(re.findall(pattern_1,history))
pattern_2 = r"\s\d{4}\s"
print(re.findall(pattern_2,history))
pattern_3 = r"\s\d{3,4}\s"
print(re.findall(pattern_3,history))
christian_pattern = r"(?<!\d)\d{3,4}(?!\d)"#we are testing
print(re.findall(christian_pattern,history))