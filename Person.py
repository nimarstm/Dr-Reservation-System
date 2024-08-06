from config import *
from datetime import date
import config


class Person:
    def __init__(self, username, phone_number, password):
        self.username = username
        self.password = password
        self.phone_number = phone_number
        print(Id0, "fuckkkk")

    def ReservedListShow(self):
        connection = Connection0()
        cursor = connection.cursor()
        sql = "SELECT ID, drName, Date, Time FROM reserve_info WHERE userID = %s"
        val = (config.Id0,)
        cursor.execute(sql, val)
        reserve_list = cursor.fetchall()
        return reserve_list

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

    def ChangeUsername(self, newusername):
        connection = Connection0()
        cursor = connection.cursor()
        sql = "UPDATE userinfo SET Username=%s WHERE ID=%s"
        val = (newusername, config.Id0)
        cursor.execute(sql, val)
        connection.commit()
        print("username changed")
        if cursor.rowcount > 0:
            print("successfully changes")
            return 1
        else:
            print("failed change")
            return 0

    def ChangePhoneNumber(self, newphonenumber):
        connection = Connection0()
        cursor = connection.cursor()
        sql = "UPDATE userinfo SET PhoneNumber=%s WHERE ID=%s"
        val = (newphonenumber, config.Id0)
        cursor.execute(sql, val)
        connection.commit()
        print("phonenumber changed")
        if cursor.rowcount > 0:
            print("successfully changes")
            return 1
        else:
            print("failed change")
            return 0

    def ChangePassword(self, newpassword):
        connection = Connection0()
        cursor = connection.cursor()
        sql = "UPDATE userinfo SET Password=%s WHERE ID=%s"
        val = (newpassword, config.Id0)
        cursor.execute(sql, val)
        connection.commit()
        print("password changed")
        if cursor.rowcount > 0:
            print("successfully changes")
            return 1
        else:
            print("failed change")
            return 0

    # def Changeinfo(self, newusername, newphonenumber, newpassword):
    #     connection = Connection0()
    #     cursor = connection.cursor()
    #     if newusername:
    #         sql = "UPDATE userinfo SET Username=%s WHERE ID=%s"
    #         val = (newusername, config.Id0)
    #         cursor.execute(sql, val)
    #         connection.commit()
    #         print("username changed")
    #     if newphonenumber:
    #         sql = "UPDATE userinfo SET PhoneNumber=%s WHERE ID=%s"
    #         val = (newphonenumber, config.Id0)
    #         cursor.execute(sql, val)
    #         connection.commit()
    #         print("phonenumber changed")
    #     if newpassword:
    #         sql = "UPDATE userinfo SET Password=%s WHERE ID=%s"
    #         val = (newpassword, config.Id0)
    #         cursor.execute(sql, val)
    #         connection.commit()
    #         print("password changed")
    #     if cursor.rowcount > 0:
    #         print("successfully changes")
    #         return 1
    #     else:
    #         print("failed change")
    #         return 0

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

    def ShowDoctorDate(self, category, drname):
        current_date = date.today()
        connection = Connection0()
        cursor = connection.cursor()
        sql = "Select * From drinfo Where Expert=%s and Date>=%s and Capacity>0 and Name=%s "
        val = (category, str(current_date), drname)
        cursor.execute(sql, val)
        drdate = [row[3] for row in cursor.fetchall()]
        return drdate

    def ShowDoctorTime(self, category, drname, drdate):
        current_date = date.today()
        connection = Connection0()
        cursor = connection.cursor()
        sql = "Select * From drinfo Where Expert=%s and Date>=%s and Capacity>0 and Name=%s and Date=%s"
        val = (category, str(current_date), drname, drdate)
        cursor.execute(sql, val)
        drtime = [row[4] for row in cursor.fetchall()]
        return drtime

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

    def AddtoReserveInfo(self, drname, drdate, drtime):
        connection = Connection0()
        cursor = connection.cursor()
        insert_query = "INSERT INTO reserve_info (drName, userID, Date, Time) VALUES (%s, %s, %s,%s)"
        values = (drname, config.Id0, drdate, drtime)
        cursor.execute(insert_query, values)
        connection.commit()
        print("reserve inseted to reserve info")
