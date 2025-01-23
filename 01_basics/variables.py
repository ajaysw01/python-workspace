# int
x = 23
print(type(x))

# float 
y = 23.8328
print(type(y))

# double
z = -2.323423143412243241342134213412432141234
print(type(z))

# str
name = "ajay "
last = 'Wankhade'

print(name+last)

# concatination
fullName = name + last
print(fullName)


# Many values to multiple variables
# No of var should match no of values
x, y, z = "Ajay", "sjs", "Nacho"
print(x,y,z)


# unpack collection
fruits = ["apple", "banana","cherry"]
a, b, c = fruits

print(a, b, c)

#Global Variables 
# Variables that are created outside of a funciton 
x = "lets nacho"

def myfun():
    print("Sare bolo " + x)
myfun()  # Sare bolo lets nacho

def myfunc():
    x = 'nahega'
    print("Koi bhi nhi " + x)
myfunc()  # Koi bhi nhi nahega

def myfunct():
    global xx
    xx = "nacho nacho"
myfunct()
print(xx)  # nacho nacho
