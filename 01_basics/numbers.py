import random
# There are three numeric types in Python:
# int
x = 2
print(type(x))

# float
x = 2.234
print(type(x))

#float can be scientic nos
s = 12e3
print(type(s))

# complex
#cant covert complex no in another type
z = 1j 
print(type(z))



#random number
print(random.randrange(1,100))



#boolean
isEmpty = True
isPresent = False

# bool() function to evaluate value

print(bool("i am great"))

# Most Values are True
# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones
# False : empty values, such as (), [], {}, "", the number 0, and the value None


#isinstance(a,dt) 
x = 200
print(isinstance(x, float))
