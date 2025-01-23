import mymodule as mm
import platform

# custom modules
mm.greeting("ajay")

a = mm.person["age"]
print(a)

# built in modules
x = platform.system
print(x)

y = dir(platform)
print(y)