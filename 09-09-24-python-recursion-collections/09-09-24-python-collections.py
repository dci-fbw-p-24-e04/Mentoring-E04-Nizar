#This is a list of dicts
#bank database with list of users
users_data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
    {"name": "Nizar", "age": 28},
]

user_1 = users_data[0]
print('user 1', user_1)
print('user 1 name',user_1.get("name"))#get will give you None if the key does not exist
print('user 1 name',user_1["age"])#with throw a keyerror
print('-'*50)
for data in users_data:
    #for dict in list
    print(data['name'])
print('-'*50)   
for data in users_data:
    #for dict in list
    data['location'] = 'Berlin' 
    
print(users_data)
print('-'*50)
print(users_data[2]['name'])
print('-'*50)
less_than_30 = [user for user in users_data if user['age'] < 30]
print(less_than_30)