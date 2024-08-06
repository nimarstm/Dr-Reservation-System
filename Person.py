from config import *
from datetime import date
import config
current_date = date.today()


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
        if newpassword:
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

    def ShowDoctorList(self, category):
        connection = Connection0()
        cursor = connection.cursor()
        sql = "Select * From drinfo Where Expert=%s and Date>=%s "
        val = (category, current_date)
        cursor.execute(sql, val)
        drlist = cursor.fetchmany(2)
        dr_dict = {}
        print(drlist)
