from array import array
from collections import deque
import math
Number1 = 10
Number2 = 20
print((Number1+Number2)*10)
text = "Hello world this is pythone"
# this is comment
print(len(text))
print(text[0])
print(text[0:5])
print(text[0:])
print(text[:5])
text2 = """ Hello
 World
 85
"""
print(text2)
text3 = "want to print \" "
text4 = "line 1 \n line 2"
print(text3+"\n" + text4)
first = "coding"
last = "is cool"
full = f"{first} {last} \n{80+5} is good number"
print(full)
text.strip()  # whitespace removeing from end and first of string
print(text.replace("Hello", "goodbye"))
print("Hello" in text)
print("Hello" not in text)
print(10**3)  # توان
print(round(2.9))  # gerd mikone
print(round(2.3))
print(abs(-25))  # gadr motlag
print(math.sin(0))
# x = input("Enter x ")
x = 0
# tabdil noe motgayer
int(x)
str(x)
bool(x)
float(x)
print(bool(x))
type(x)  # noew motgayer ro barmigardone
ord("m")  # namayesh adadi har harf ro barmigardone


tempreture = 40
if tempreture == 20:
    print("its 20 ")
    print("its nice tempreture")
elif tempreture < 20:
    print("its cold")
else:
    print("its hot")


age = 15

message = "Can enter" if age >= 18 else "Can not enter"
print(message)

# عملگر های منطقی
# and
# or
# not

# Between
# 10<age<18

for i in range(4):
    print(i)
# از یک شروع میکنه تا ده دوتا دوتا میره جلو
for i in range(1, 10, 2):
    print(i)

successfull = False
for i in range(3):
    print("attempt")
    if successfull == True:
        print("sent successfull")
        break
else:
    print("sent failed")

list2 = [1, 2, "Nima", 3]
print(list2)
print(list2[2])

for x in list2:
    print(x)


number = 100
while number > 0:
    print(number)
    number //= 2

# function ya hamoon methode


def printhi(name):
    print(f"hi {name}")


printhi("Nima")


def printhi2(name):
    return ("hi"+name)


print(printhi2("BABAK"))

printhi2(name="Nima")


# num1 bayad avl biad ejbare hast num2 exteyari hast age
# arguman begerre on ro lahaz mikone nagere 5 ro lahaz mikone
# hatman avl ejbari ha v baad exteyari ha garar migiran
def test(num1, num2=5):
    return (num1+num2)


# * tupple ejad meshe ((1,2,5))
# ** dictionary ejad mishe({'id':1,'age':20,'name':nima})
def test2(*numbers):
    total = 1
    for i in numbers:
        total *= i
    print(total)


test2(1, 2, 5, 2)
test2(20, 4, 1, 0, 8)


def test3(**user):
    print(user["id"])
    print(user["name"])


test3(id=1, age=20, name="nima")


# List

numbers = [1, 2, 3, "Nima"]
print(numbers)
print(numbers[0])
matrix = [[0, 1], [2, 3]]
combined = numbers+matrix
print(combined)
print(combined[0:3])
# 2ta 2 ta joda mikone entexab mikoneh
print(combined[::2])

# unpacking
num = [1, 2, 3, 4, 5, "Nima", "Armin"]
first, second, third, *others = num
# first,*others,last=num
print(first, second, third, others)


for i in num:
    print(i)

# in function yek 2taye barmigardone ex :(0,1),...
for i in enumerate(num):
    print(i)

for index, number in enumerate(num):
    print(index, number)
# ADD to list
num.append(6)  # akharesh ezafe mikone
num.insert(0, 0)  # be on xone ezafe mikone bagye ro shift mede jolo
print(num)
# Remove from list
num.pop()  # akharero hazf mikone
num.pop(2)  # in index ro pak mekone
num.remove(5)  # in adad ro az list hafz mikone (na index ro ozv ro hazf mikone)
del num[0]  # in index ro hazf mikone
del num[0:3]  # index 0 ta 2 ro hazf mikone

num.clear()  # hame onsor haro hazf mikone

# print(num.index("Nima"))  # index nima ro mige
num.count("Nima")  # tedad tekrar nima ro mige
num.sort(reverse=True)  # baraks sort mikone
num.sort()  # soert mikone

# ex payen mige chetori behesh begim bar che asasi sort kon
# way one
items2 = [
    ("item1", 100),
    ("item3", 80),
    ("item2", 130)
]


def items_sorted(item):
    return item[1]


items2.sort(key=items_sorted, reverse=True)
print(items2)

# way two
items2.sort(key=lambda item: item[1])
print(items2)

x = map(lambda item: item[1], items2)
for item in x:
    print(item)

# ya list comprihention
x = [item[1] for item in items2]

filtered = list(filter(lambda item: item[1] >= 100, items2))
print(filtered)
# ya
filtered = [item[1] for item in items2 if item[1] >= 100]


# zip 2 ya chand list ro nazer b nazer tupple mikone
list1 = [1, 10, 100]
list22 = [2, 20, 200]
print(list(zip(list1, list22, "ABC")))


# first in first out


queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
# az avl remove mikone
queue.popleft()
# yani age khali bood
if not queue:
    print("Empty")


# tupple
testTupple = (1, 2)
print(testTupple[0])
# concat ba + anjam meshe (1,2)+(3,4)
# tabdil list b tupple
listy = [1, 2, 3]
tuppletest = tuple(listy)
print(tuppletest)

# unpacking
x, y = testTupple
print(x, y)

m = 10
n = 20
# عوض کردن جای این دو
m, n = n, m
print(n)
print(m)

# araye


arayeTest = array("i", [1, 2, 3, 4, 5])
arayeTest.append(6)
print(arayeTest)
arayeTest.insert(0, 0)
print(arayeTest)
arayeTest[arayeTest.index(2)] = 20
print(arayeTest)


# set (مجموعه) عضو تکراری ندارد
arayez = [1, 1, 2, 3, 4, 3]
setTest = set(arayez)
setTest.add(7)
print(setTest.issubset({1}))
setTest2 = {1, 4, 3, 2}
print(setTest)
print(setTest2)
# اجتماع  و اشتراک دو محموعه
Ejtema2set = setTest | setTest2
print(Ejtema2set)
Eshterak2set = setTest2 & setTest
# اعضایی که یا در اولی هست یا در دومی
w = setTest ^ setTest2


# dictionary (کلید مقدار)
dicTest = {"x": 1, "y": "2", "m": 100}
dicTest2 = {0: "A", 1: "B", 2: "c", 3: 30}
dicTest3 = dict(x=1, y=2, m=100)
print(dicTest2.keys())
print(dicTest["x"])
# عوض کردن مقدار یک کلید
dicTest["x"] = 1000
# اضافه کردن یک مقدار و کلید
dicTest["v"] = 200
print(dicTest)
# آرکومان دوم واسه اینه که اگه اون کلید وجود نداشت اون رو برگردونه
print(dicTest.get("x", 000))
# حذف کلید و مقدا
del dicTest["m"]
# پیمایش روی کلید
for x in dicTest:
    print(x)
# پیمایش روی مقدار
for x in dicTest:
    print(dicTest[x])

# به صورت تاپل پیمایش میکنه
for x in dicTest.items():
    print(x)

# پیمایش و انپک
for x, y in dicTest.items():
    print(x, y)

# dictionary comprehention
valu = {x: x*2 for x in range(5)}
print(valu)

#generator
valu2=(x*2 for x in range(5))

#unpacking operator
print(*valu)
# دوتا ستاره برای دیکشنری

#exception

try:
    age=int(input("age:"))
except ValueError:
    print("you entered invalid number")
except ZeroDivisionError:
    print("age can not be zero")   
    
# هر دو اکسپشن رو میشه درون پارانتز در یک اگسپشن نوشت
finally:
    print("program last action")