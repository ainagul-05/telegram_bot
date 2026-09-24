create_products_table = """ CREATE TABLE IF NOT EXISTS products (
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     name TEXT NOT NULL,
     price INTEGER ,
     product_id INTEGER NOT NULL,
     photo TEXT
     ) """


create_products_detaiil_table = """
CREATE TABLE IF NOT EXISTS products_detail (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT,
    product_id INTEGER NOT NULL,
    category TEXT 
    )
    """





create_orders_table = """ CREATE TABLE IF NOT EXISTS orders (
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     order_id INTEGER NOT NULL,
     size TEXT NOT NULL,
     stuffing TEXT NOT NULL,
     address TEXT NOT NULL
     )"""

create_orders_detail_table = """ CREATE TABLE IF NOT EXISTS orders_detail (
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     order_id INTEGER NOT NULL,
     status TEXT NOT NULL ,
     photo TEXT
     )"""




select_orders = 'SELECT * FROM orders'


insert_product = 'INSERT INTO products (name, price, product_id, photo) VALUES (?, ?, ?, ?)'
insert_product_detail = 'INSERT INTO products_detail (description, product_id, category) VALUES (?, ?, ?)'

insert_order = 'INSERT INTO orders (size, stuffing, address) VALUES (?, ?, ?)'
insert_order_detail = 'INSERT INTO orders_detail (order_id, status, photo) VALUES (?, ?, ?)'


get_products = """
     SELECT products.name, products.price, products_detail.description, products_detail.category, products.product_id , products.photo
     FROM products
     INNER JOIN products_detail on products.product_id = products_detail.product_id
"""

update_product = 'UPDATE {table} SET {field} = ? WHERE products.product_id= ?;'
