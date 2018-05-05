import sqlite3
from entity.customer import Customer
import os

conn = sqlite3.connect('labelA.db')
cursor = conn.cursor()

if os.path.isfile('labelA.db') == False :

    create_db('labelA.db')

    print("db created")

else :

    print( "db already exists")



def create_db() :


    cursor.execute("""CREATE TABLE customer (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        password TEXT,
        created date
    )""")

    cursor.execute("""CREATE TABLE order (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        status TEXT,
        customerId INTEGER,
        FORGEIN KEY(customerId) REFERENCES customer(id)
    )""")

    cursor.execute("""CREATE TABLE delivery (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pref_date datetime,
        orderId INTEGER,
        FORGEIN KEY(orderId) REFERENCES order(id)
    )""")

    cursor.execute("""CREATE TABLE cart (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pref_date datetime,
        orderId INTEGER,
        FORGEIN KEY(orderId) REFERENCES order(id)
    )""")

    cursor.execute("""CREATE TABLE order_product (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        orderId INTEGER,
        productId INTEGER,
        quantity INTEGER,
        FORGEIN KEY(orderId) REFERENCES order(id),
        FORGEIN KEY(productId) REFERENCES product(id)
    )""")

    cursor.execute("""CREATE TABLE product (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price INTEGER,
        description TEXT,
        stock INTEGER
    )""")

    conn.commit()
    conn.close()
