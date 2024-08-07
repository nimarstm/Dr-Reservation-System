from Person import Person
import config
from config import *


class Login:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        print(username, password)
# Checks and extract user info for log in

    def checkinfo(self):
        connection = Connection0()
        cursor = connection.cursor()
        sql = "SELECT * FROM userinfo WHERE Username = %s"
        val = (self.username,)
        cursor.execute(sql, val)
        row = cursor.fetchone()
        if row:
            config.Id0 = row[0]
            print("ID:", row[0])
            print("Name:", row[1])
            print("phonenumber:", row[2])
            print("password:", row[3])
            if row[3] == self.password:
                person = Person(self.username, row[3], self.password)
                config.person_list.insert(0, person)
                person.ReservedListShow()
                return 1
            else:
                return 0
        else:
            print("No record found with the specified ID.")
            cursor.close()
            return -1
