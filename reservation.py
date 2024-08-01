from tkinter import *


def LoginCheck(username, password):
    if username == "Nima" and password == "13841394":
        wellcom_label.config(text="log in successfull",foreground="green")
        username_label.pack_forget()
        username_entry.pack_forget()
        password_label.pack_forget()
        password_entry.pack_forget()
        login_button.pack_forget()
    else:
        wellcom_label.config(text="log in failed",foreground="red")
def Signup(username,password,phone_number):
    #arguman ha b database ezafe meshan
    print(" ")
    
def loginButtonCommand():
    LoginCheck(username_entry.get(), password_entry.get())


def loginpage():
    wellcom_label.config(text="Log in page" , foreground="orange")
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
    wellcom_label.config(text="sign up page" , foreground="orange")
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
login_show_button = Button(Window, text="Log in page", command=loginpage)
signup_show_button=Button(Window,text="Creat an account",command=signuppage)
login_show_button.pack()
signup_show_button.pack()
username_label = Label(Window, text="Username:")
username_entry = Entry(Window)
password_label = Label(Window, text="Password")
password_entry = Entry(Window)
phonenumber_label=Label(Window,text="Phone Number")
phonenumber_entry=Entry(Window)
login_button = Button(Window, text="Login", command=loginButtonCommand)
signup_button=Button(Window,text="sign Up")
Window.mainloop()
