from tkinter import *
import mysql.connector

Id0 = " "


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
        sql = "SELECT * FROM reserve_info WHERE userID = %s"
        val = (Id0,)
        cursor.execute(sql, val)
        row = cursor.fetchall()
        print(row)


class Login():
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
reservemenu.add_command(label="1.Dermatologist")
reservemenu.add_command(label="2.Cardiologist")
reservemenu.add_command(label="3.General practitioner")
reservemenu.add_command(label="4.Gynecologist")
reservemenu.add_command(label="5.Neurologist")
menubar.add_cascade(label="Reserve", menu=reservemenu)
menubar.add_command(label="My Reservs")
menubar.add_command(label="Setting")
menubar.add_command(label="Support")
menubar.add_command(label="Help")
menubar.add_command(label="quit", command=Window.quit)
Window.mainloop()
