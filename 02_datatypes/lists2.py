# Looping through a list
thislist = ["apple", "banana", "cherry"]
for item in thislist : 
    print(item)

print("\n")
# through index no by range & len
flowers = ["lily","rose","mogra","lotus"]
for i in    range(len(flowers)):
    print(flowers[i])

print("\n")

city = ["akola", "hyd","ngp"]
i = 0 
while i < len(city) : 
    print(city[i])
    i+=1

print("\n")
[print(x) for x in city]