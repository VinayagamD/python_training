class MyClass:

    """
    This is VinayLogics
    """
    a = 50

    def func(self):
        print("Hello Vinaylogics")


print(MyClass.a)

print(MyClass.__doc__)

myClass = MyClass()

print(myClass.func())


class Student:
    def __init__(self, rollno, name):
        self.rollno = rollno
        self.name = name

    def display_student(self):
        print("roll no: ", self.rollno, ", name: ", self.name)


emp1 = Student(121, "Ajeet")
emp2 = Student(122, "Sonoo")
emp1.display_student()
emp2.display_student()