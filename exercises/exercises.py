"""names = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary"]
print(names[1])
print(names[3])
print(names[-2])
print(names[1:3])
print(names[2:])
print(names[:3])
print (names)"""
from _pyrepl.commands import repaint

"""names.append("Matti")
print(names)
names.remove("Pekka")
print(names)
names.insert(2, "Teppo")
print(names)

names2 = ["allu","niini"]
names2.extend(names)
print(names2)
olga = names.index("Olga")
print(olga)
#print(hello)
if "Matti" in names:
    print("Matti was found")
else:
    print("Matti was not found")

names.sort()
print(names)
names.sort(reverse=True)
print(names)

#empty list
names = []
name = input("add a name to the list: ")
while name != "":
    names.append(name)
    name = input("add another name to the list: ")
print(names)

name = input("give me your name ")
for c in names:
    print(c)
 for n in range(1, 6):
     print(n)

for n in range(1, 20, 2):
    print(n)

#my list [1,2,3,4,5]
# my tuple (w,e,r,t,y)
# my set {re,ty,uui,iuy,iiy}
# my dictionary {"a" : 5 , "b" : 6 }"""

"""
class Car:
    def __init__(self,brand, color,mileage = 0 ,fuel = 100):
        self.brand = brand
        self.color = color
        self.mileage = mileage
        self.fuel = fuel

    def drive(self,distance):
        fuel_needed = distance * 0.5
        if fuel_needed >= self.fuel:
            print("You do not have enough fuel.")
        else:
            self.fuel -= fuel_needed
            self.mileage = self.mileage + distance
            print(f"this car is {self.brand} and the color is  {self.color} and"
              f" mileage is {self.mileage} and the fuel is  {self.fuel} ")

    def repaint(self,new_color):
        self.color = new_color
        print(f"this car is {self.brand} and the new color is {self.color} ")




car1 = Car("Toyota", "red",0)
car2 = Car("Audi", "blue",0)

car1.drive(10)
car2.drive(20)"""
"""car1.repaint("blue")"""


"""class Dog:
    def __init__(self,name,birth_year, sound="woof woof"):
        self.name = name
        self.birth_year = birth_year
        self.sound = sound
    def bark(self, times):
        for i in range(times):
            print(self.name+"barks"+self.sound)
        return


class Hotel:
    def __init__(self):
        self.dogs = []

    def dog_checkin(self, dog):
        self.dogs.append(dog)
        print (dog.name + "dog checkin")
        return

    def dog_checkout(self, dog):
        self.dogs.remove(dog)
        print (dog.name + "dog checkout")
        return

    def greet_dogs(self):
        for dog in self.dogs:
            dog.bark(2)


dog1 = Dog("Dolly", 2022)
dog2 = Dog("Royalty", 2020)
dog3 = Dog("Melvin", 2023)

hotel = Hotel()
hotel.dog_checkin(dog1)
hotel.dog_checkin(dog2)
hotel.dog_checkin(dog3)
hotel.greet_dogs()
hotel.dog_checkout(dog2)
hotel.greet_dogs()"""


"""class Student:
    def __init__(self,name,last_name,student_ID):
        self.name = name
        self.last_name = last_name
        self.student_ID = student_ID

class Teacher:
    def __init__(self):
        self.students = []
    def add_student(self,student):
        self.students.append(student)
        return
    def remove_student(self,student):
        self.students.remove(student)
        return
    def attendance(self):
        for i in self.students:
            print(i.name,i.last_name,i.student_ID)
        return

student1 = Student("noob", "noobiloinen", 123456)
student2 = Student("James", "Jameson", 147852)
student3 = Student("lily", "lilyiamson", 789654)
teacher= Teacher()
teacher.add_student(student1)
teacher.add_student(student2)
teacher.attendance()"""


class Publication:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(self.name)
class Book(Publication):
    def __init__(self, name, page_count, author):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_info(self):
        super().print_info()
        print(f"Author: {self.author} and the page number is {self.page_count}")


class Magazine(Publication):
    def __init__(self, name , chief_editor):
        self.chief_editor = chief_editor
        super().__init__(name)

    def print_info(self):
        super().print_info()
        print(f"chief editor: {self.chief_editor}")

#main
num = []

x1 = Book("suomi mestari", 300, "yenni")
x2 = Magazine( "Parabola function","dear Timo")
num.append(x1)
num.append(x2)
for i in num:
    i.print_info()
