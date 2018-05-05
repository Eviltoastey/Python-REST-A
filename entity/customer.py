import sqlite3

conn = sqlite3.connect('C:\\xampp\\htdocs\\Python\\LabelA\\labelA.db')
cursor = conn.cursor()

class Customer():

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def new_customer(self): 

        cursor.execute("INSERT INTO customer VALUES ('{}', '{}')".format(self.name, self.email))

        conn.commit()
        conn.close()

        return 'customer created'

    def get_all_customers(self):

        value = cursor.execute("SELECT * FROM customer")

        return value

    def get_customer(self):

        value = cursor.execute("SELECT * FROM customer WHERE 'name' = '{}'").format(self.name)

        return value
