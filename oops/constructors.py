
class Student:

    # Non Parametrized Constructor
    # Constructor -non parametrized

    def __init__(self):
        print("This non parametrized constructor")

    def show(self, name):
        print("Hello ", name)


class Student2:

    # Constructor Parameterized
    def __init__(self, name):
        """

        :type name: string
        """
        print(" This is parametrized constructor")
        self.name = name

    def show(self):
        print("Hello ", self.name)


student = Student()
student.show("vinay")


student1 = Student2( "Vinayagam" )
student1.show()


