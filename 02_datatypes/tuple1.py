import sys
import timeit

# Tuple 
# ordeered, unchangeable and allow duplicate values.
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print("\n")


# even though it is unchangeable there are some workarounds
x = list(thistuple)
x[1]="guava"
thistuple = tuple(x)
print(thistuple)
print("\n")

oneItemTuple = ("ajaya",) #have to place one extra comma 
print(type(oneItemTuple))
print("\n")


# Tuple constructor 
mytuple = tuple(("aj","sj","dj"))
print(mytuple)
print("\n")

# slicing

a = (1,2,3,4,5,6,7,8,9)
a1, *a2, a3 = a
print(a1)
print(a2)
print(a3)
print(a[::2])


# unpacking 
tp = "max",28, "boston"
name, age, city = tp
print(name)
print("\n")


# memory comparison
l1 = [0,1,2,3,"Ajay",True]
t1 = (0,1,2,3,"Ajay",True)
print(sys.getsizeof(l1))
print(sys.getsizeof(t1))

# time Comparison
print(timeit.timeit(stmt="[0,1,2,3,4,5,6,7,8,9]", number = 1000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5,6,7,8,9)", number = 1000000))

# conclusion : tuples are more efficient
