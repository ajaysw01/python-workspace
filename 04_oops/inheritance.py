# Inheritance
class Person : 
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printName(self):
        print(self.firstname, self.lastname)
        

p1 = Person("ajay", "patiL")
p1.printName()

class Student(Person):
# The child's __init__() function overrides the inheritance of the parent's __init__() function.
    def __init__(self, fname,lname,age) : 
        super().__init__(fname, lname)
        self.age = age

    def welcome(self):
        print("Welcome ", self.firstname, self.lastname, "you age is ",self.age)

x = Student("Mike", "Olsen", 2019)
x.welcome()