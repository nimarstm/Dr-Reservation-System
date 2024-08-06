import mysql.connector
person_list=[]
Id0=None
def Connection0():
    connection = mysql.connector.connect(
        host="localhost",  # یا آدرس سرور MySQL
        user="root",  # نام کاربری MySQL شما
        password="12345678",  # رمز عبور MySQL شما
        database="reservation_system"  # نام پایگاه داده‌ای که می‌خواهید به آن وصل شوید
    )
    return connection
