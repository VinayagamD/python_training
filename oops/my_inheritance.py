class Animal:

    def eat(self):
        print("Eating.......")


class Dog(Animal):
    def bark(self):
        print("Barking....")


d = Dog()
d.eat()
d.bark()


# Multilevel Inheritance
class BabyDog(Dog):
    def weep(self):
        print("Weeping")



bd = BabyDog()
bd.eat()
bd.bark()
bd.weep()