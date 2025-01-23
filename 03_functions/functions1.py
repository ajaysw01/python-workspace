
# function declaration
def my_function():
    print("Hello world from myfunciton")

# function invocation
my_function()

# functions with params
def add(num1, num2, num3):
    print(num1+num2+num3)

#passing arguments to add()
# no of params == no of arguments else TypeError
add(1,23,3)
# add(1,23,3,5) TypeError


# Arbitary arguments : *args
# If the number of arguments is unknown, add a * before the parameter name:
def arbi_func(*ciities):
    print("RajRajeshwar city : " + ciities[1])

arbi_func("ngp","akola","hyd")