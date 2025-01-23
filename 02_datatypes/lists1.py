# declaring a list
# items are ordered, changeable, allow duplicate values,diff datatypes

myList = ["aj","sj","ak","aj","pj"]
print((myList))
# lenght
print(len(myList))

# accessing list elements
dtList = ["apple","banana",True,12, 32.3, "Nacho"]
print(type(dtList[3]))

# negative index
print(dtList[-2])

# range
print(dtList[2: 5])

# change items
dtList[2]="cherry"
print(dtList)

# without replacing & inserting at specific index
dtList.insert(2,"mango")
print(dtList)

# to add at the end
dtList.append("Bhailog")
print(dtList)


# append another list
localList = ["papaya","peru","grapes"]
dtList.extend(localList)
print(dtList)
print(localList)

# appending tuple,set, dict
mytuple = ("kiwi","orange")
dtList.extend(mytuple)
print(dtList)


# remove itme & if more than one then first occurance
dtList.remove("kiwi")
print(dtList)

# for specified index & index not specified removes last item
dtList.pop(1)
print(dtList)

# del keyword
del dtList[1]
print(dtList)
print("\n")

# delete completedly
# del dtList
# print(dtList) ---> NameErro

# clearing the content
# dtList.clear()
# print(dtList)
# print("\n")

# List constructor
thislist = list(("hyd","akola","ngp","pune"))
print(thislist)
print(type(thislist))

if "akola" in thislist:
    print("Akola is present")

