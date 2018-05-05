import sqlite3

conn = sqlite3.connect('labelA.db')
cursor = conn.cursor()

class Cart():

    def __init__(self):

        self = self