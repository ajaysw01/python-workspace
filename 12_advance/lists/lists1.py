# Lists : 
#  ordred, mutable, allows duplicate elements

myList = ["banana", "chdrry", "apple"]
print(myList)

# item = myList[-1]
# print(item)

# # iterating 
# for x in myList : 
#     print(x)

if "banana" in myList : 
    print("yes")
else : 
    print("no")

myList.append("lemon")
myList.insert(1, "grapes")
print(myList)
item = myList.pop()
print(item)


# sorting 
new_list = sorted(myList)
print(myList)
print(new_list)

# new list with multiple times
ls = [0]*5
print(ls)

# slicing

arr = [1,2,34,5,6,78,8,10]
a = arr[1:6]
print(a)
b = arr[::2]
print(b)

# list comphresion 
a1 = [1,2,3,4,5,6]
b1 = [i*i for i in a ]
print(b1)