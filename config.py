import mysql.connector
# variabels and functions that used in all classes
person_list = []
Id0 = None


def Connection0():
    connection = mysql.connector.connect(
        host="localhost",  # یا آدرس سرور MySQL
        user="root",  # نام کاربری MySQL شما
        password="12345678",  # رمز عبور MySQL شما
        database="reservation_system"  # نام پایگاه داده‌ای که می‌خواهید به آن وصل شوید
    )
    return connection


def DatabaseTestRemove():
    connection = Connection0()
    cursor = connection.cursor()
    sql = "Delete From userinfo Where Username=%s"
    val = ("Test",)
    cursor.execute(sql, val)
    connection.commit()


def TestReserveAdd():
    connection = Connection0()
    cursor = connection.cursor()
    insert_query = "INSERT INTO reserve_info (ID, userID) VALUES (%s, %s)"
    values = (0, "Test")
    cursor.execute(insert_query, values)
    connection.commit()
