items = ["apple", "banana", "coconuts", "orange", "kiwi"]
items_title = [item.title() for item in items]
print(items_title)
#or we can do this
print('-'*50)
titled_items = map(lambda x:x.title(),items)
print(list(titled_items))
print('-'*50)
prices = [12, 15, 2, 7, 10,8,5]
less_than_10 = filter(lambda x:x<10,prices)
print(list(less_than_10))
print('-'*50)
emails = ['alice@example.com',
'bob@example.net',
'charlie@example.org',
'dave@example.com',
'eve@example.net','alien@invade.mars']
safe_email = list(filter(lambda email: not email.endswith('.mars'),emails))
print(safe_email)
print('-'*50)
students = [("John", 90, 2.5), ("Jane", 85, 3.2), ("Joe", 80, 0.1), ("Jack", 95, 1.5)]
sorted_by_name = sorted(students,key=lambda x:x[0])
print(sorted_by_name)
sorted_by_grade = sorted(students,key=lambda x:x[1])
print(sorted_by_grade)
#we are reversing the order
sorted_by_grade = sorted(students,key=lambda x:x[1],reverse=True)
print(sorted_by_grade)