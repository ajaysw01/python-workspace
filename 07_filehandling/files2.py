
# writing to existing files
# a - append 
# w - write

f = open("ajay1.txt","a")
print(f.write("It has more content"))
f.close()

# open and reading after appedn

f = open("ajay1.txt","r")
print(f.read())


# overwrtiing the file 
f = open("ajay.txt", "w")
f.write("Overwritign existing content")
f.close()

f = open("ajay.txt","r")
print(f.read())