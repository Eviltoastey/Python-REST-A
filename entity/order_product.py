import sqlite3

conn = sqlite3.connect('labelA.db')
cursor = conn.cursor()

class Order_product():

    def __init__(self):

        self = self