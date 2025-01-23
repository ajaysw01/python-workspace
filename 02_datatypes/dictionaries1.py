# Dictionary : key -value pairs, undordered, mutable

mydict = {"name" : "ajya", "age" : 25, "city" : "akola"}
print(mydict)

mydict["email"] = "ajay@mail.com"
print(mydict)


# delete
del mydict["email"]
print(mydict)


for key,value in mydict.items() : 
    print(key,value)

# copy
mydict_cpy = mydict.copy()
print(mydict_cpy)

# update
merge_dict = mydict_cpy.update(mydict)


# 
dict1 = {3:9, 5:36,9:8}
mytuple = (89,90)
dd = {mytuple:15}
print(dd)