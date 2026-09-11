create_products_table = """ CREATE TABLE IF NOT EXISTS products (
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     name TEXT NOT NULL,
     price INTEGER,
     description TEXT
     ) """


insert_product = 'INSERT INTO products (name, price, description) VALUES (?, ?, ?)'


create_orders_table = """ CREATE TABLE IF NOT EXISTS orders (
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     size TEXT NOT NULL,
     stuffing TEXT NOT NULL,
     address TEXT NOT NULL
     )"""

insert_order = 'INSERT INTO orders (size, stuffing, address) VALUES (?, ?, ?)'


select_orders = 'SELECT * FROM orders'
