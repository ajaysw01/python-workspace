# class declaration
class Demo : 
    x = 5

# object creation
obj = Demo()
# print(obj.x)


# he __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created
class Person : 
    def __init__(self,name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"
    
    def myfunc(self):
        print("Hello my name is "+self.name)

p1 = Person("Ajay",25)
# print(p1.name,p1.age)
# without str
# print(p1)  #<__main__.Person object at 0x0000019521496BA0>

# The __str__() function controls what should be returned when the class object is represented as a string.

# with str
# print(p1)
p1.myfunc()

# modifying object progper
p1.age = 3242
print(p1)

# deleteing object properties
# del p1.age
# print(p1)

# delete object
# del p1
