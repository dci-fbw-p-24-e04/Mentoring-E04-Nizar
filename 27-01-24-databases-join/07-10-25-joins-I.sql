create database super_store ;

\c super_store;

CREATE TABLE Customers (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE
);

CREATE TABLE Products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100),
    price DECIMAL(10, 2)
);

CREATE TABLE Orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES Customers(customer_id),
    order_date DATE DEFAULT CURRENT_DATE
);

CREATE TABLE OrderDetails (
    order_detail_id SERIAL PRIMARY KEY,
    order_id INT REFERENCES Orders(order_id),
    product_id INT REFERENCES Products(product_id),
    quantity INT
);

INSERT INTO Customers (name, email)
VALUES 
    ('Alice Johnson', 'alice@example.com'),
    ('Bob Smith', 'bob@example.com'),
    ('Carol Taylor', 'carol@example.com');

INSERT INTO Products (product_name, price)
VALUES 
    ('Laptop', 1200.00),
    ('Smartphone', 800.00),
    ('Tablet', 400.00);

INSERT INTO Orders (customer_id)
VALUES 
    (1), (2), (1);

INSERT INTO OrderDetails (order_id, product_id, quantity)
VALUES 
    (1, 1, 1), -- Alice bought 1 Laptop
    (1, 3, 2), -- Alice bought 2 Tablets
    (2, 2, 1), -- Bob bought 1 Smartphone
    (3, 2, 2); -- Alice bought 2 Smartphones

SELECT o.order_id, c.name AS customer_name FROM 
Orders o INNER JOIN Customers c 
ON o.customer_id = c.customer_id;

INSERT INTO Customers (name, email)
VALUES 
    ('John Doe', 'john@example.com');

SELECT o.order_id, c.name AS customer_name FROM 
Orders o right JOIN Customers c 
ON o.customer_id = c.customer_id;

SELECT o.order_id, c.name AS customer_name FROM 
Orders o LEFT JOIN Customers c 
ON o.customer_id = c.customer_id;

SELECT o.order_id, c.name AS customer_name FROM 
Orders o FULL outer JOIN Customers c 
ON o.customer_id = c.customer_id;

select o.order_id, c.name as customer_name,od.quantity                
from Orders o INNER JOIN Customers c ON o.customer_id = c.customer_id
INNER JOIN OrderDetails od ON o.order_id = od.order_id;
select o.order_id, c.name as customer_name, p.product_name,od.quantity,(p.price*od.quantity) as total_price
from Orders o INNER JOIN Customers c ON o.customer_id = c.customer_id
INNER JOIN OrderDetails od ON o.order_id = od.order_id
INNER Join Products p ON od.product_id = p.product_id;

SELECT o.order_id, c.name AS customer_name FROM 
Orders o right JOIN Customers c 
ON o.customer_id = c.customer_id WHERE o.order_id is null;

SELECT o.order_id, c.name AS customer_name FROM 
Customers c  LEFT JOIN  Orders o 
ON  c.customer_id = o.customer_id  WHERE o.order_id is null;