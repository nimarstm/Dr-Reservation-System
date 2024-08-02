import mysql.connector 

# ایجاد اتصال به پایگاه داده
connection = mysql.connector.connect(
    host="localhost",  # یا آدرس سرور MySQL
    user="root",  # نام کاربری MySQL شما
    password="12345678",  # رمز عبور MySQL شما
    database="reservation_system"  # نام پایگاه داده‌ای که می‌خواهید به آن وصل شوید
)
cursor=connection.cursor()
# ایجاد یک شیء cursor
sql = "SELECT * FROM userinfo WHERE USername = %s"
val = ("Nima",)

# اجرای کوئری
cursor.execute(sql, val)

# دریافت نتیجه
row = cursor.fetchone()

# بررسی و نمایش نتیجه
if row:
    print("ID:", row[0])
    print("Name:", row[1])
    print("phonenumber:", row[2])
    print("password:", row[3])
else:
    print("No record found with the specified ID.")
# بستن cursor
cursor.close()

# بستن اتصال به پایگاه داده
connection.close()
