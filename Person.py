from config import *
from datetime import date
import config


class Person:
    def __init__(self, username, phone_number, password):
        self.username = username
        self.password = password
        self.phone_number = phone_number
# Extracts user reserve history from data base and return that as a list

    def ReservedListShow(self):
        connection = Connection0()
        cursor = connection.cursor()
        sql = "SELECT ID, drName, Date, Time FROM reserve_info WHERE userID = %s"
        val = (config.Id0,)
        cursor.execute(sql, val)
        reserve_list = cursor.fetchall()
        return reserve_list
# searchs for reserve id and delete that row from date base

    def ReserveRemove(self, reserveID):
        connection = Connection0()
        cursor = connection.cursor()
        sql = "Delete From reserve_info Where ID=%s"
        val = (reserveID,)
        cursor.execute(sql, val)
        connection.commit()
        if cursor.rowcount > 0:
            print("successfully rmoved")
            return 1
        else:
            print("failed remove")
            return 0
# changes and update the field (username ,password or phonenumber) at data base
# polymorphism used

    def ChangeField(self, field_name: str, new_value: str) -> int:
        connection = Connection0()
        cursor = connection.cursor()
        sql = f"UPDATE userinfo SET {field_name}=%s WHERE ID=%s"
        val = (new_value, config.Id0)
        cursor.execute(sql, val)
        connection.commit()

        print(f"{field_name} changed")
        if cursor.rowcount > 0:
            print("successfully changes")
            return 1
        else:
            print("failed change")
            return 0
# sends field(username) and new username to update at data base

    def ChangeUsername(self, newusername):
        return self.ChangeField("Username", newusername)
# sends field(phonenumber) and new phone number to update at data base

    def ChangePhoneNumber(self, newphonenumber):
        return self.ChangeField("PhoneNumber", newphonenumber)
# sends field(password) and new password to update at data base

    def ChangePassword(self, newpassword):
        return self.ChangeField("Password", newpassword)
# extracts dr list filtered by choosen expert and returns list

    def ShowDoctorName(self, category):
        current_date = date.today()
        connection = Connection0()
        cursor = connection.cursor()
        sql = "Select * From drinfo Where Expert=%s and Date>=%s and Capacity>0 "
        val = (category, str(current_date))
        cursor.execute(sql, val)
        drlist = [row[1] for row in cursor.fetchall()]
        print(drlist)
        return drlist
# extracts dr date list filtered by dr name and returns list

    def ShowDoctorDate(self, category, drname):
        current_date = date.today()
        connection = Connection0()
        cursor = connection.cursor()
        sql = "Select * From drinfo Where Expert=%s and Date>=%s and Capacity>0 and Name=%s "
        val = (category, str(current_date), drname)
        cursor.execute(sql, val)
        drdate = [row[3] for row in cursor.fetchall()]
        return drdate
# extracts dr time list filtered by date and dr name and free capacity and return list

    def ShowDoctorTime(self, category, drname, drdate):
        current_date = date.today()
        connection = Connection0()
        cursor = connection.cursor()
        sql = "Select * From drinfo Where Expert=%s and Date>=%s and Capacity>0 and Name=%s and Date=%s"
        val = (category, str(current_date), drname, drdate)
        cursor.execute(sql, val)
        drtime = [row[4] for row in cursor.fetchall()]
        return drtime
# Choosen reserve day and time capacity became full and not reserveable any more

    def SubmitReserve(self, category, drname, drdate, drtime):
        connection = Connection0()
        cursor = connection.cursor()
        sql = "UPDATE drinfo SET Capacity=%s WHERE Expert=%s and Name=%s and Date=%s and Time=%s"
        val = (0, category, drname, drdate, drtime)
        cursor.execute(sql, val)
        connection.commit()
        print("capacity changed")
        if cursor.rowcount > 0:
            print("successfully submited")
            return 1

        else:
            print("failed submit")
            return 0
# Insert new reserve to reserve_info data base

    def AddtoReserveInfo(self, drname, drdate, drtime):
        connection = Connection0()
        cursor = connection.cursor()
        insert_query = "INSERT INTO reserve_info (drName, userID, Date, Time) VALUES (%s, %s, %s,%s)"
        values = (drname, config.Id0, drdate, drtime)
        cursor.execute(insert_query, values)
        connection.commit()
        print("reserve inseted to reserve info")
