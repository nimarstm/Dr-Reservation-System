from Login import Login
from Signup import Signup
from rich.console import Console
from rich.table import Table
from InquirerPy import prompt
import config
from InquirerPy.base.control import Choice
from InquirerPy import inquirer


console = Console()


def my_reserve_page():
    person = config.person_list[0]
    reserve_list = person.ReservedListShow()
    items = []
    for a, b, c, d in reserve_list:
        items.append(f"Reservation Code : ~{a}~ Doctor Name : {
            b} Date : {c} Time : {d}")
    items.append("back")
    reserve_preview = [
        {
            "type": "list",
            "name": "action",
            "message": "! by selecting them you can cancel them",
            "choices": items,
        }
    ]
    reserve_preview_answer = prompt(reserve_preview)
    print(reserve_preview_answer["action"])
    if reserve_preview_answer["action"] == "back":
        firstpage()
    else:
        selected_items_list = reserve_preview_answer["action"].split("~")
        result = person.ReserveRemove(selected_items_list[1])
        if result == 1:
            console.print("[bold green]sucsessfull Canceled.[/bold green]")

        else:
            console.print("[bold red]Action  failed failed.[/bold red]")
        firstpage()


def setting_page():
    person = config.person_list[0]
    menu_bar = [
        {
            "type": "list",
            "name": "action",
            "message": "You can change your info",
            "choices": ["Username", "Phone Number", "Password", "back"],
        }
    ]
    menu_bar_answer = prompt(menu_bar)
    if menu_bar_answer["action"] == "Phone Number":
        new_phone_number = [
            {
                "type": "input",
                "name": "phonenumber",
                "message": "Enter your new phone Number: or enter 0 to go back",
            },
        ]
        new_phone_number_answers = prompt(new_phone_number)
        if new_phone_number_answers["phonenumber"] != "0":
            result = person.ChangePhoneNumber(
                new_phone_number_answers["phonenumber"])
            if result == 1:
                console.print(
                    "[bold green]PhoneNumber sucsessfully Changed.[/bold green]")
            else:
                console.print("[bold red]Change failed.[/bold red]")
    elif menu_bar_answer["action"] == "Username":
        new_username = [
            {
                "type": "input",
                "name": "username",
                "message": "Enter your new username: or enter 0 to go back",
            },
        ]
        new_username_answers = prompt(new_username)
        if new_username_answers["username"] != "0":
            result = person.ChangeUsername(new_username_answers["username"])
            if result == 1:
                console.print(
                    "[bold green]username sucsessfully Changed.[/bold green]")
            else:
                console.print("[bold red]Change failed.[/bold red]")

    elif menu_bar_answer["action"] == "Password":
        new_password = [
            {
                "type": "password",
                "name": "password",
                "message": "Enter your new password:",
            },
        ]
        new_password_answers = prompt(new_password)
        if new_password_answers["password"] != "0":
            result = person.ChangePassword(new_password_answers["password"])
            if result == 1:
                console.print(
                    "[bold green]password sucsessfully Changed.[/bold green]")
            else:
                console.print("[bold red]Change failed.[/bold red]")

    firstpage()


def Create_New_Reserve_Page():
    person = config.person_list[0]
    questions = [
        {
            "type": "list",
            "name": "selection",
            "message": "Choose Doctor Expert",
            "choices": ["Dermotologist", "Cardiologist", "General Practitioner", "Gynecologist", "Neurologist", "back"],
        }]
    answers = prompt(questions)
    category = answers["selection"]
    if category == "back":
        firstpage()
    else:
        drname_list = person.ShowDoctorName(category)
        drname_set = list(set(drname_list))
        drname_set.append("back")

        questions = [
            {
                "type": "list",
                "name": "selection",
                "message": "Choose Date you want",
                "choices": drname_set
            }]
        answers = prompt(questions)
        drname = answers["selection"]
        if drname == "back":
            Create_New_Reserve_Page()
        else:
            drdate_list = person.ShowDoctorDate(category, drname)
            drdate_set = list(set(drdate_list))
            drdate_set.append("back")
            questions2 = [
                {
                    "type": "list",
                    "name": "selection",
                    "message": "Choose Doctor Date",
                    "choices": drdate_set
                }]
            answers = prompt(questions2)
            drdate = answers["selection"]
            if drdate == "back":
                Create_New_Reserve_Page()
            else:
                drtime_list = person.ShowDoctorTime(category, drname, drdate)
                drtime_set = list(set(drtime_list))
                drtime_set.append("back")
                questions3 = [
                    {
                        "type": "list",
                        "name": "selection",
                        "message": "Choose Time you want",
                        "choices": drtime_set
                    }]
                answers = prompt(questions3)
                drtime = answers["selection"]
                if drtime == "back":
                    Create_New_Reserve_Page()
                else:
                    reserve_info = f"{category},{drname},{drdate},{
                        drtime}\n Confirm reserve info to submit:"
                    questions4 = [
                        {
                            "type": "list",
                            "name": "selection",
                            "message": reserve_info,
                            "choices": ["Confirm", "Cancel"]
                        }]
                    answers = prompt(questions4)
                    result = answers["selection"]
                    if result == "Confirm":
                        person.SubmitReserve(category, drname, drdate, drtime)
                        person.AddtoReserveInfo(drname, drdate, drtime)
                        console.print(
                            "[bold green]reserve sucsessfully submited.[/bold green]")
                    else:
                        console.print("[bold red]reserve canceled.[/bold red]")
            firstpage()


def firstpage():
    menu_bar = [
        {
            "type": "list",
            "name": "action",
            "message": "What do you want to do?",
            "choices": ["Show your Reserve History", "Create New Reserve", "Setting", "quite"],
        }
    ]
    menu_bar_answer = prompt(menu_bar)
    if menu_bar_answer["action"] == "Show your Reserve History":
        my_reserve_page()
    if menu_bar_answer["action"] == "Setting":
        setting_page()
    if menu_bar_answer["action"] == "Create New Reserve":
        Create_New_Reserve_Page()

# gets login info from user and process result


def login_page():
    login_questions = [
        {
            "type": "input",
            "name": "username",
            "message": "Enter your username:",
        },
        {
            "type": "password",
            "name": "password",
            "message": "Enter your password:",
        },
    ]
    login_answers = prompt(login_questions)
    login = Login(login_answers["username"], login_answers["password"])
    if login.checkinfo() == 0:
        console.print("[bold red]Log in failed.[/bold red]")
    elif login.checkinfo() == 1:

        console.print("[bold green]sucsessfull log in.[/bold green]")
        firstpage()
    else:
        console.print("[bold red]account not found[/bold red]")

#  gets info from users to register them


def signup_page():
    signup_questions = [
        {
            "type": "input",
            "name": "username",
            "message": "Choose a username:",
        },
        {
            "type": "input",
            "name": "phonenumber",
            "message": "enter a phone Number:",
        },
        {
            "type": "password",
            "name": "password",
            "message": "Choose a password:",
        },
        {
            "type": "password",
            "name": "confirm_password",
            "message": "Confirm your password:",
        },
    ]
    signup_answers = prompt(signup_questions)

    # Password match check
    if signup_answers["password"] != signup_answers["confirm_password"]:
        console.print(
            "[bold red]Passwords do not match! Please try again.[/bold red]")
        login_and_signup_selection()
    else:
        signup = Signup(
            signup_answers["username"], signup_answers["phonenumber"], signup_answers["password"])
        if signup.DuplicateUsernameCheck() == 1:
            if signup.insert() == 1:
                console.print(
                    "[bold green]sucsessfull sign up please log in again.[/bold green]")
                login_page()
            else:
                console.print("[bold red]sign up failed.[/bold red]")
                login_and_signup_selection()
        else:
            console.print("[bold red]this username exist.[/bold red]")
            signup_page()


# Gets the user's choice between the login page and the signup page


def login_and_signup_selection():
    main_menu = [
        {
            "type": "list",
            "name": "action",
            "message": "What do you want to do?",
            "choices": ["Login", "Signup", "quite"],
        }
    ]


# دریافت انتخاب کاربر
    menu_answer = prompt(main_menu)

    if menu_answer["action"] == "Login":
        login_page()

    else:
        signup_page()


# program starts from here
login_and_signup_selection()


# def result_check(result, section):
#     if result == 0:
#         console.print(f"[bold red]{section} failed.[/bold red]")
#     elif result == -1:
#         console.print("[bold red] not found[/bold red]")
#     else:
