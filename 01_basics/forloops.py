
#range & pass
# for x in range(2,6):
#     print(x)

# incrementing 
for x in range(2, 100, 4):
    if x == 18 : break
    print(x)
else:
        print("finished") #not executed coz of break

# String
for i in "banana":
    print(i)

# List break & continue
fruits = ["apple","kiwi","guava","grapes"]
for fruit in fruits:
    if fruit == "kiwi":
        break
    print(fruit)


# Nested Loop
adj = ["red","sour","tasty","green"]

for x in adj : 
    for y in fruits:
        print(x,y)
