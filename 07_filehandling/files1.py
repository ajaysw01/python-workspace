
# file reading 
f = open("ajay.txt","r")
# print(f.read())

# reading only specified characters
# print(f.read(5))

# reading one line
# print(f.readline())
# print(f.readline())

# reading whole file using loops

for i in f : 
    print(i)


# good practice to close the file
f.close()