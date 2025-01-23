# Sorting lists
# sort() -> sorts capital letters first
thislist = ["orange", "mango", "kiwi", "Pineapple", "banana"]
thislist.sort()
print(thislist)

nums = [23,324,2,34,1,34,23,234,5323]
nums.sort()
print(nums)
print("\n")

# descending
nums.sort(reverse= True)
print(nums)
print("\n")


# Customizing sorting function
def sortFunc(n):
    return abs(n-100)

nums.sort(key=sortFunc)
print(nums)
print("\n")


# case insensitive sort
thislist.sort(key=str.lower)
print(thislist)
print("\n")


# reverse the list
thislist.reverse()
print(thislist)
print("\n")

# copy list copy()
myList = thislist.copy()
print(myList)
print("\n")

# list()
list1 = list(myList)
print(list1)
print("\n")

# by slice operator :
myList2 = list1[:]
print(myList2)
print("\n")

# joining two lists
# + operator 

ls = ['a','b','c']
ls1 = [1,2,3]
# print(ls + ls1)

# using append
# for i in ls1 : 
#     ls.append(i)    
# print(ls)

# extend
ls.extend(ls1)
print(ls)

