import sqlite3
from entity.customer import Customer
from entity.customer import Customer
from entity.customer import Customer
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
        id int AUTOINCREMENT PRIMARY KEY
        name text,
        email text,
        password text,
        created date
    )""")

    cursor.execute("""CREATE TABLE order (
        id int AUTOINCREMENT PRIMARY KEY
        date text,
        status text,
        customer text
    )""")

    cursor.execute("""CREATE TABLE delivery (
        id int AUTOINCREMENT PRIMARY KEY
        pref_date datetime,
        order text,
    )""")

    cursor.execute("""CREATE TABLE cart (
        id int AUTOINCREMENT PRIMARY KEY
        pref_date datetime,
        order text,
    )""")

    cursor.execute("""CREATE TABLE order_product (
        id int AUTOINCREMENT PRIMARY KEY
        order text,
        product text,
        quantity int
    )""")

    cursor.execute("""CREATE TABLE product (
        id int AUTOINCREMENT PRIMARY KEY
        name text,
        price int,
        description text,
        stock int
    )""")

    conn.commit()
    conn.close()

cursor.execute("SELECT * FROM customer")