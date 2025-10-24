class Student:
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
teacher.attendance()