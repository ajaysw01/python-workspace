import os

# creatign new file
#  x - create returns error if file exitsts
# a - append 
# w - write

# f = open("demo.txt","x")

# delete file
# import os module 
# os.remove("demo.txt")

# checking if file exists then deleteing 
if os.path.exists("demo.txt"):
    os.remove("demo.txt")
else : 
    print("file doesn't exitist")


# deleting folder
os.rmdir("myfolder") #only empty folders can be removed
