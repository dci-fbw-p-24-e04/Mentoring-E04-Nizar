#lists ==> mutable
list_of_fruits = [
    "apple",
    "banana",
    "kiwi",
    "orange",
    "mango"
    ]
#tuples ==> immutable
user_data = ('nizar',28,'nizar@python.py')
#dicts ==> mutable
store_items = {
    'laptop':1000,
    'smartphone':500,
    'plasmaTV':600
}
#tuple with one element
tuple_with_one_element=(0,)
list_with_one_element= ['julie']
dict_with_one_item = {'name':'Taras'}
print(type(tuple_with_one_element))
print('-'*50)
#lets do some iteration
for fruit in list_of_fruits:
    print(fruit)
print('#'*50)   
#or we can say
for i in range(len(list_of_fruits)):
    print(list_of_fruits[i])
print('-'*50)
string_of_fruit = ' '.join(list_of_fruits)#is string
print(string_of_fruit)
print('-'*50)
#how to iterate through a tuple 
#hint: there are 3 ways to do it
for data in user_data:
    print(data)
print('-'*50)
for i in range(len(user_data)):
    print(user_data[i])
print('-'*50)
user_data = ('nizar','28','nizar@python.py')
name,age,email = user_data#unpacking
print(name)
print(age)
print(email)
string_data = ' '.join(user_data)
print(string_data)
print('-'*50)
#now dicts
store_items = {
    'laptop':1000,
    'smartphone':500,
    'plasmaTV':600
}
for i in store_items:
    print(i) #will print the keywords
print('-'*50)
for item in store_items.items():
    print(item)
#item : laptop, price:1000
#we use unpacking
print('-'*50)
for key,val in store_items.items():
    print(f"item {key}, price {val}")
    
print('-'*50)
for val in store_items.values():
    print(val)
