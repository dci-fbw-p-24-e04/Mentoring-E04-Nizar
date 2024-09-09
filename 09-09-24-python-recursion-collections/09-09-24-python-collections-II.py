import pprint
# List of orders
orders = [
    {"order_id": 1, "customer": "John Doe", "books": ["The Great Gatsby", "1984"], "total": 40.0},
    {"order_id": 2, "customer": "Jane Smith", "books": ["To Kill a Mockingbird"], "total": 20.0},
    {"order_id": 3, "customer": "Emily Johnson", "books": ["The Great Gatsby", "1984", "To Kill a Mockingbird"], "total": 60.0}
]



first_order = orders[0] 
print(first_order)
print(first_order['books'])
total_rev = sum([order['total'] for order in orders])
print(total_rev)
ordered_1984 = [(order['order_id'],order['customer']) for order in orders if '1984' in order['books']]
print(ordered_1984)
print('-'*50)
orders[1]['books'].append('Da vincci Code')
print(orders)
print('-'*50)
#updating a list of book based on user input
id = int(input('enter your id '))
for order in orders:
    if order['order_id'] == id:
        order['books'].append('Harry Potter')

pprint.pprint(orders)
print('-'*50)
# Inventory dictionary
inventory = {
    "The Great Gatsby": {"stock": 5, "price": 20.0},
    "1984": {"stock": 8, "price": 20.0},
    "To Kill a Mockingbird": {"stock": 3, "price": 20.0}
}
stock_1984 = inventory['1984']['stock']
print(stock_1984)
inventory['The Great Gatsby']['stock'] -= 2 #updating the value of the stock by removing 2 books
print("The Great Gatsby",inventory["The Great Gatsby"])
inventory["To Kill a Mockingbird"]["stock"] += 5
print('To Kill a Mockingbird',inventory["To Kill a Mockingbird"])
print('-'*50)
inventory["Moby Dick"] = {"stock": 10, "price": 25.0}
pprint.pprint(inventory)
print('-'*50)
for details in inventory.values():
    print(details)
print('-'*50)
total_sum = sum([detail['stock']*detail['price']for detail in inventory.values()])
print('Total:',total_sum)
