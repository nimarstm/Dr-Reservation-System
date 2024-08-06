from tkinter import *
from tkinter import font
from tkinter import ttk
from datetime import date
import mysql.connector
current_date = date.today()
Id0 = " "
row0 = []
person_list = []


def Connection0():
    connection = mysql.connector.connect(
        host="localhost",  # یا آدرس سرور MySQL
        user="root",  # نام کاربری MySQL شما
        password="12345678",  # رمز عبور MySQL شما
        database="reservation_system"  # نام پایگاه داده‌ای که می‌خواهید به آن وصل شوید
    )
    return connection


class Person():
    def __init__(self, username, phone_number, password):
        self.username = username
        self.password = password
        self.phone_number = phone_number

    def ReservedListShow(self):
        connection = Connection0()
        cursor = connection.cursor()
        sql = "SELECT ID, drName, Date, Time FROM reserve_info WHERE userID = %s"
        val = (Id0,)
        cursor.execute(sql, val)
        global row0
        row0 = cursor.fetchall()
        print(row0)

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

    def Changeinfo(self, newusername, newphonenumber, newpassword):
        connection = Connection0()
        cursor = connection.cursor()
        if newusername:
            sql = "UPDATE userinfo SET Username=%s WHERE ID=%s"
            val = (newusername, Id0)
            cursor.execute(sql, val)
            connection.commit()
            print("username changed")
        if newphonenumber:
            sql = "UPDATE userinfo SET PhoneNumber=%s WHERE ID=%s"
            val = (newphonenumber, Id0)
            cursor.execute(sql, val)
            connection.commit()
            print("phonenumber changed")
        if newpassword:
            sql = "UPDATE userinfo SET Password=%s WHERE ID=%s"
            val = (newpassword, Id0)
            cursor.execute(sql, val)
            connection.commit()
            print("password changed")
        if cursor.rowcount > 0:
            print("successfully changes")
            return 1
        else:
            print("failed change")
            return 0

    def ShowDoctorList(self, category):
        connection = Connection0()
        cursor = connection.cursor()
        sql = "Select * From drinfo Where Expert=%s and Date>=%s "
        val = (category, current_date)
        cursor.execute(sql, val)
        drlist = cursor.fetchmany(2)
        dr_dict={}
        print(drlist)


class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def checkinfo(self):
        connection = Connection0()
        cursor = connection.cursor()
        sql = "SELECT * FROM userinfo WHERE Username = %s"
        val = (self.username,)
        cursor.execute(sql, val)
        row = cursor.fetchone()
        if row:
            global Id0
            Id0 = row[0]
            print("ID:", row[0])
            print("Name:", row[1])
            print("phonenumber:", row[2])
            print("password:", row[3])
            if row[3] == self.password:
                person = Person(self.username, row[3], self.password)
                global person_list
                person_list.insert(0, person)
                person.ReservedListShow()
                return 1
            else:
                return 0
        else:
            print("No record found with the specified ID.")
            cursor.close()
            return -1


class Signup():
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


def LoginCheck(username, password):
    login = Login(username, password)
    if login.checkinfo() == 1:
        wellcom_label.config(
            text="log in successfull \n WellCome", foreground="green")
        signup_show_button.pack_forget()
        username_label.pack_forget()
        username_entry.pack_forget()
        password_label.pack_forget()
        password_entry.pack_forget()
        login_button.pack_forget()
        Window.config(menu=menubar)
    elif login.checkinfo() == 0:
        wellcom_label.config(text="log in failed", foreground="red")
    else:
        wellcom_label.config(
            text="user not found \n create an account", foreground="pink")


def SignupCheck(username, phone_number, password):
    # arguman ha b database ezafe meshan
    signup = Signup(username, phone_number, password)
    if signup.insert() == 1:
        wellcom_label.config(text="sign up seccessfull please log in ")
        username_label.pack_forget()
        username_entry.pack_forget()
        username_entry.pack_forget()
        password_label.pack_forget()
        password_entry.pack_forget()
        phonenumber_label.pack_forget()
        phonenumber_entry.pack_forget()
        signup_button.pack_forget()
    else:
        wellcom_label.config(text="Fill the information correctly")


def loginButtonCommand():
    LoginCheck(username_entry.get(), password_entry.get())


def signupButtonCommand():
    SignupCheck(username_entry.get(),
                phonenumber_entry.get(), password_entry.get())


def MyReserveMenuCommand():
    setting_pannel.pack_forget()
    wellcom_label.config(text="Your reserves history", foreground="black")
    myreserve_list_box.delete(0, END)
    myreserve_pannel.pack(fill="both", expand=True)
    reservedelete_button.pack(side="bottom")
    myreserve_pannel.add(myreserve_list_box)
    for a, b, c, d in row0:
        myreserve_list_box.insert(END, f"Reservation Code : ~{a}~ Doctor Name : {
                                  b} Date : {c} Time : {d} \n")


def SettingMenuCommand():
    myreserve_pannel.pack_forget()
    wellcom_label.config(text="You Can Change your information")
    setting_pannel.pack(fill="none", expand=True)
    setting_pannel.add(setting_username_label)
    setting_pannel.add(setting_username_entry)
    setting_pannel.add(setting_phonenumber_label)
    setting_pannel.add(setting_phonenumber_entry)
    setting_pannel.add(setting_password_label)
    setting_pannel.add(setting_password_entry)
    setting_pannel.add(setting_changeinfo_button)


def reserve_remove_command():
    selected_indices = myreserve_list_box.curselection()  # دریافت ایندکس‌های انتخاب شده
    # دریافت آیتم‌های انتخاب شده
    if len(selected_indices) == 1:
        selected_items = [myreserve_list_box.get(i) for i in selected_indices]
        print("Selected items:", selected_items)
        selected_items_list = selected_items[0].split("~")
        person = person_list[0]
        result = person.ReserveRemove(selected_items_list[1])
        if result == 1:
            myreserve_list_box.delete(selected_indices[0])
        else:
            print("deleting operation failed")
    else:
        print("please select to delete")


def change_info_command():
    person = person_list[0]
    result = person.Changeinfo(setting_username_entry.get(
    ), setting_phonenumber_entry.get(), setting_password_entry.get())
    if result == 1:
        print("change info was successfull")
    else:
        print("change info failed")


def Reserve_Menu_Command(category):
    person = person_list[0]
    person.ShowDoctorList(category)
    reserve_pannel.pack(fill="none", expand=True)
    items = ["Option 1", "Option 2", "Option 3", "Option 4"]
    doctor_selection_ComboBox['values'] = items
    doctor_selection_ComboBox.pack()



def loginpage():
    wellcom_label.config(text="Log in page", foreground="orange")
    login_show_button.pack_forget()
    signup_button.pack_forget()
    signup_show_button.pack()
    username_label.pack()
    username_entry.pack()
    password_label.pack()
    password_entry.pack()
    login_button.pack()


def signuppage():
    login_show_button.pack()
    signup_show_button.pack_forget()
    wellcom_label.config(text="sign up page", foreground="orange")
    username_label.pack()
    username_entry.pack()
    password_label.pack()
    password_entry.pack()
    phonenumber_label.pack()
    phonenumber_entry.pack()
    signup_button.pack()
    login_button.pack_forget()


Window = Tk()
Window.title("Reservtion System")
Window.geometry("800x600")
Window.resizable(width=False, height=False)

wellcom_label = Label(
    Window, text="Wellcome to reservation System", foreground="blue", font=(20))
wellcom_label.pack()
login_show_button = Button(Window, text="Log in page",
                           command=loginpage, anchor="e")
signup_show_button = Button(
    Window, text="Creat an account", command=signuppage, anchor="center")
login_show_button.pack()
signup_show_button.pack()
username_label = Label(Window, text="Username:")
username_entry = Entry(Window)
password_label = Label(Window, text="Password")
password_entry = Entry(Window)
phonenumber_label = Label(Window, text="Phone Number")
phonenumber_entry = Entry(Window)
login_button = Button(Window, text="Login", command=loginButtonCommand)
signup_button = Button(Window, text="sign Up", command=signupButtonCommand)
menubar = Menu(Window)
reservemenu = Menu(menubar, tearoff=0)
reservemenu.add_command(label="1.Dermatologist",
                        command=lambda: Reserve_Menu_Command("Dermotologist"))
reservemenu.add_command(label="2.Cardiologist",
                        command=lambda: Reserve_Menu_Command("Cardiologist"))
reservemenu.add_command(label="3.General practitioner",
                        command=lambda: Reserve_Menu_Command("General Practitioner"))
reservemenu.add_command(label="4.Gynecologist",
                        command=lambda: Reserve_Menu_Command("Gynecologist"))
reservemenu.add_command(label="5.Neurologist",
                        command=lambda: Reserve_Menu_Command("Neurologist"))
menubar.add_cascade(label="Reserve", menu=reservemenu)
menubar.add_command(label="My Reservs", command=MyReserveMenuCommand)
menubar.add_command(label="Setting", command=SettingMenuCommand)
menubar.add_command(label="Support")
menubar.add_command(label="Help")
menubar.add_command(label="quit", command=Window.quit)
custom_font = font.Font(family="Helvetica", size=16)
myreserve_pannel = PanedWindow(Window, bd=50, bg="grey")
myreserve_list_box = Listbox(myreserve_pannel, font=custom_font)
reservedelete_button = Button(
    myreserve_pannel, text="Delete Reserve", font=20, command=reserve_remove_command)
setting_pannel = PanedWindow(Window, bd=50, bg="black")
setting_username_label = Label(
    setting_pannel, text="New Username", background="white")
setting_username_entry = Entry(setting_pannel)
setting_phonenumber_label = Label(
    setting_pannel, text="New Phonenumber", background="white")
setting_phonenumber_entry = Entry(setting_pannel)
setting_password_label = Label(
    setting_pannel, text="New Password", background="white")
setting_password_entry = Entry(setting_pannel)
setting_changeinfo_button = Button(
    setting_pannel, text="Change info", font=16, background="red", command=change_info_command)
reserve_pannel = PanedWindow(Window, bd=50, bg="black")
doctor_selection_ComboBox=ttk.Combobox(reserve_pannel)

Window.mainloop()
