
# list comprehension --> gives shorter syntax when 
# we wan to create a new list based on exiting list

# syntax : newlist = [expression for item in iterable if condition == True]


# create new list fruits containing "a"
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# using for loop
# for x in fruits : 
#     if "a" in x : 
#         newlist.append(x)

# using list comprehension
# newlist = [x for x in fruits if "a" in x ]
# print(newlist)

# range
# newlist = [x for x in range(10) if x%2==0]
# print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
