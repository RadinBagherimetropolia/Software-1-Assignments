"""student = {"Bob":{"math":4 , "science":1},
           "Alice":{"math":2 , "science":4},
           "Ana":{"math":5 , "science":5},
           "Joshua" :{"math":4 , "science":4}
           }

def  add_student(students,name,subject,):
    students[name] = subject
    return




add_student(student,"matti", {"math" :42 })


student["Alice"]["History"]=92

student["Bob"]["math"]=82
add_student(student, "Charlie", {"biology":85})
student["Charlie"]["chemistry"]=50
del student["Alice"]["math"]
for i in student:
    print(i, student[i])


print(student)"""


"""class Dog:
    created = 0
    def __init__(self,name,birth_year, sound = ("woof")):
      self.name = name
      self.birth_year = birth_year
      self.sound = sound
      Dog.created += 1


    def bark(self, time):
        for i in range(time):
            print(self.sound)
        return


dog1 = Dog("tina",1990, "rre")


dog2 = Dog("bob",1123)

print(Dog.created)"""

class Employee:
    total = 0
    def __init__(self, name, lastname):
        Employee.total += 1
        self.number = Employee.total
        self.name = name
        self.lastname = lastname

    def print_info(self):
        print(f"Employee number {self.number}:{self.name} {self.lastname}")

#subclasses inherited from the base class
class HourlyPaid(Employee):
    def __init__(self, name, lastname, hourly_pay):
        self.hourly_pay = hourly_pay
        super().__init__(name, lastname)

    def print_info(self):
        super().print_info()
        print(f"Hourly pay: {self.hourly_pay}$")

class MonthlyPaid(Employee):
    def __init__(self, name, lastname, monthly_pay):
        super().__init__(name, lastname)
        self.monthly_pay = monthly_pay

    def print_info(self):
        super().print_info()
        print(f"Monthly pay: {self.monthly_pay}$")






#main program
employee = []
emp1 = Employee("viivi", "virta")
emp2 = Employee("Ahmed", "Habib")
emp3 = HourlyPaid("pekka", "puro", 14.50)
emp4 = MonthlyPaid("Heidi", "lulu", 145)
employee.append(emp1)
employee.append(emp2)
employee.append(emp3)
employee.append(emp4)
for i in employee:
    i.print_info()
