from Login import Login
from Signup import Signup
from rich.console import Console
from rich.table import Table
from InquirerPy import prompt
import config
from InquirerPy.base.control import Choice
from InquirerPy import inquirer


console = Console()
login_stutus = False


def my_reserve_page():
    person = config.person_list[0]
    reserve_list = person.ReservedListShow()
    print(reserve_list)
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
    if (reserve_preview_answer["action"] == "back"):
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
                "message": "Enter your new phone Number:",
            },
        ]
        new_phone_number_answers = prompt(new_phone_number)
        person.ChangePhoneNumber(new_phone_number_answers["phonenumber"])
        console.print(
            "[bold green]PhoneNumber sucsessfully Changed.[/bold green]")
    elif menu_bar_answer["action"] == "Username":
        new_username = [
            {
                "type": "input",
                "name": "username",
                "message": "Enter your new username:",
            },
        ]
        new_username_answers = prompt(new_username)
        person.ChangeUsername(new_username_answers["username"])
        console.print(
            "[bold green]username sucsessfully Changed.[/bold green]")
    elif menu_bar_answer["action"] == "Password":
        new_password = [
            {
                "type": "password",
                "name": "password",
                "message": "Enter your new password:",
            },
        ]
        new_password_answers = prompt(new_password)
        person.ChangePassword(new_password_answers["password"])
        console.print(
            "[bold green]password sucsessfully Changed.[/bold green]")
    firstpage()


def firstpage():
    menu_bar = [
        {
            "type": "list",
            "name": "action",
            "message": "What do you want to do?",
            "choices": ["Show your Reserve History", "Create new Reserve", "Setting", "quite"],
        }
    ]
    menu_bar_answer = prompt(menu_bar)
    if menu_bar_answer["action"] == "Show your Reserve History":
        my_reserve_page()
    if menu_bar_answer["action"] == "Setting":
        setting_page()


main_menu = [
    {
        "type": "list",
        "name": "action",
        "message": "What do you want to do?",
        "choices": ["Login", "Signup"],
    }
]

# دریافت انتخاب کاربر
menu_answer = prompt(main_menu)

if menu_answer["action"] == "Login":
    # سوالات برای لاگین
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
    result = Login(login_answers["username"], login_answers["password"])
    if result.checkinfo() == 0:
        console.print("[bold red]Log in failed.[/bold red]")
    elif result.checkinfo() == 1:

        console.print("[bold green]sucsessfull log in.[/bold green]")
        login_stutus = True
        firstpage()
    else:
        console.print("[bold red]account not found[/bold red]")


elif menu_answer["action"] == "Signup":
    # سوالات برای ساین‌اپ
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

    # بررسی تطابق رمز عبور
    if signup_answers["password"] != signup_answers["confirm_password"]:
        console.print(
            "[bold red]Passwords do not match! Please try again.[/bold red]")
    else:
        result = Signup(
            signup_answers["username"], signup_answers["phonenumber"], signup_answers["password"])
        if result.insert() == 1:
            console.print(
                "[bold green]sucsessfull sign up please log in again.[/bold green]")
        else:
            console.print("[bold red]sign up failed.[/bold red]")

    # نمایش پاسخ‌ها برای بررسی

    #     questions = [
    #         {
    #             "type": "checkbox",
    #             "name": "remove_items",
    #             "message": "Select items to cancel: or go back",
    #             "choices": items,
    #         }
    #     ]
    #     answers = prompt(questions)
    #     print(f"Answers received: {answers}")
    #     if "remove_items" in answers:
    #         # دریافت آیتم‌های انتخاب‌شده
    #         selected_items = answers["remove_items"]
    #         for item in selected_items:
    #             items.remove(item)
    #         table = Table(title="Final Items")
    #         table.add_column("Item", style="cyan")
    #         for item in items:
    #             table.add_row(item)
    # console.print(table)
