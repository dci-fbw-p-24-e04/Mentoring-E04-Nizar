

### 1. **Accessing and Printing First Order Details:**
   ```python
   first_order = orders[0]
   print(first_order)
   ```
   - Retrieves the first order from the `orders` list and prints its details.
   - Output will be:
     ```
     {'order_id': 1, 'customer': 'John Doe', 'books': ['The Great Gatsby', '1984'], 'total': 40.0}
     ```

### 2. **Printing the List of Books in the First Order:**
   ```python
   print(first_order["books"])
   ```
   - Prints the list of books in the first order, which is `['The Great Gatsby', '1984']`.

### 3. **Calculating the Total Revenue:**
   ```python
   total_rev = sum([order["total"] for order in orders])
   print(total_rev)
   ```
   - Uses list comprehension to sum the `total` values from each order in the `orders` list.
   - Total revenue will be `120.0` (i.e., `40.0 + 20.0 + 60.0`).

### 4. **Finding Orders That Include the Book "1984":**
   ```python
   ordered_1984 = [
       (order["order_id"], order["customer"])
       for order in orders
       if "1984" in order["books"]
   ]
   print(ordered_1984)
   ```
   - Creates a list of tuples containing the `order_id` and `customer` for orders that include the book "1984".
   - Output will be: `[(1, 'John Doe'), (3, 'Emily Johnson')]`.

### 5. **Adding a New Book to the Second Order:**
   ```python
   orders[1]["books"].append("Da Vinci Code")
   print(orders)
   ```
   - Adds `"Da Vinci Code"` to the list of books in the second order (`order_id: 2`).
   - The updated `orders` list will reflect this addition:
     ```python
     [{'order_id': 1, 'customer': 'John Doe', 'books': ['The Great Gatsby', '1984'], 'total': 40.0},
      {'order_id': 2, 'customer': 'Jane Smith', 'books': ['To Kill a Mockingbird', 'Da Vinci Code'], 'total': 20.0},
      {'order_id': 3, 'customer': 'Emily Johnson', 'books': ['The Great Gatsby', '1984', 'To Kill a Mockingbird'], 'total': 60.0}]
     ```

### 6. **Updating Orders with User Input:**
   ```python
   id = int(input("enter your id "))
   for order in orders:
       if order["order_id"] == id:
           order["books"].append("Harry Potter")
   pprint.pprint(orders)
   ```
   - Prompts the user to enter an `order_id` and adds `"Harry Potter"` to the list of books for the corresponding order.
   - Example: If the user enters `1`, the first order will have the new book added:
     ```python
     [{'order_id': 1, 'customer': 'John Doe', 'books': ['The Great Gatsby', '1984', 'Harry Potter'], 'total': 40.0},
      ...
     ```

### 7. **Working with Inventory:**
   - **Printing the Stock of "1984":**
     ```python
     stock_1984 = inventory["1984"]["stock"]
     print(stock_1984)
     ```
     - Prints the stock of the book `"1984"`, which is `8`.
   
   - **Updating Stock for "The Great Gatsby":**
     ```python
     inventory["The Great Gatsby"]["stock"] -= 2
     print("The Great Gatsby", inventory["The Great Gatsby"])
     ```
     - Reduces the stock of `"The Great Gatsby"` by `2` and prints the updated inventory for this book.

   - **Increasing Stock for "To Kill a Mockingbird":**
     ```python
     inventory["To Kill a Mockingbird"]["stock"] += 5
     print("To Kill a Mockingbird", inventory["To Kill a Mockingbird"])
     ```
     - Increases the stock of `"To Kill a Mockingbird"` by `5`.

   - **Adding a New Book "Moby Dick" to Inventory:**
     ```python
     inventory["Moby Dick"] = {"stock": 10, "price": 25.0}
     pprint.pprint(inventory)
     ```
     - Adds `"Moby Dick"` to the inventory with a stock of `10` and price `25.0`.

### 8. **Printing Each Book's Details in Inventory:**
   ```python
   for details in inventory.values():
       print(details)
   ```
   - Iterates over the inventory dictionary and prints the details (stock and price) of each book.

### 9. **Calculating the Total Value of Inventory:**
   ```python
   total_sum = sum([detail["stock"] * detail["price"] for detail in inventory.values()])
   print("Total:", total_sum)
   ```
   - Calculates the total value of the inventory by summing up the product of `stock` and `price` for each book.
   - Example total sum will be calculated by multiplying each stock and price and summing them up.

These steps demonstrate manipulating nested data structures in Python, focusing on accessing, modifying, filtering, and aggregating data in dictionaries and lists.