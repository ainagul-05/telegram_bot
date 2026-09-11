import sqlite3
from database.queries import create_products_table, insert_product , create_orders_table, insert_order , select_orders

path_db = 'database/sqlite3.db'




def init_db():
    conn = sqlite3.connect(database=path_db)
    cursor = conn.cursor()
    cursor.execute(create_products_table)
    cursor.execute(create_orders_table)
    print("БД подключена!")
    conn.commit()
    conn.close()


def add_product_db(name, price, description):
    conn = sqlite3.connect(database=path_db)
    cursor = conn.cursor()
    cursor.execute(insert_product, (name, price, description))
    conn.commit()
    conn.close()



def init_orders_db():
    conn = sqlite3.connect(database=path_db)
    cursor = conn.cursor()
    cursor.execute(create_orders_table)
    print("БД подключена!")
    conn.commit()
    conn.close()





def add_order_db(size, stuffing, address):
    conn = sqlite3.connect(database=path_db)
    cursor = conn.cursor()
    cursor.execute(insert_order, (size, stuffing, address))
    conn.commit()
    conn.close()

def get_orders_db():
    conn = sqlite3.connect(database=path_db)
    cursor = conn.cursor()
    cursor.execute(select_orders)
    orders = cursor.fetchall()
    conn.close()
    return orders
