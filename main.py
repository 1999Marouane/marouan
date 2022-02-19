import datetime


class Student:
    no_of_students = 10
    todayName = datetime.date.today()

    def __init__(self, name, age, courses):
        self.name = name
        self.age = age
        self.courses = courses
        Student.no_of_students += 1

    def X(self):
        return "Name :", self.name, "Age :", self.age,"Counter",self.no_of_students,self.todayName


student_1 = Student("islam", 30, ['css', 'html'])
student_22 = Student("islam", 30, ['css', 'html'])
student_11 = Student("islam", 30, ['css', 'html'])
student_2 = Student("islam", 30, ['css', 'html'])
print(student_2.X())

