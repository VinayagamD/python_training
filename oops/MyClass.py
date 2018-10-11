class MyClass:
    a = 50

    def func(self):
        print("Hello Vinay")

print(MyClass.a)
MyClass.func(MyClass.__doc__)

ob = MyClass()
ob.func()

class Student:
    def __init__(self, rollno, name):
        self.rollno = rollno
        self.name = name

    def display_student(self):
        print("Roll no : ", self.rollno, " ; Name : ", self.name)


emp1 = Student(121, "Vinay")
emp2 = Student(122, "Ganesh")

emp1.display_student()
emp2.display_student()
