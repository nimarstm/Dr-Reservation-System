from Login import Login 
from config import *
class Signup:
    def __init__(self, username, phonenumber, password):
        self.username = username
        self.phonenumber = phonenumber
        self.password = password

    def insert(self):
        if self.username and self.phonenumber and self.password:
            connection = Connection0()
            cursor = connection.cursor()
            insert_query = "INSERT INTO userinfo (Username, phonenumber, password) VALUES (%s, %s, %s)"
            values = (self.username, self.phonenumber, self.password)
            cursor.execute(insert_query, values)
            connection.commit()
            print(cursor.rowcount, "record inserted.")
            cursor.close()
            connection.close()
            return 1
        else:
            return 0