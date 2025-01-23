

# while loop
num = 12345
rev = 0
while num != 0:
    last = num % 10
    rev = (rev * 10) + last
    num = num // 10

print(rev)

x = 1
while x < 10 :
    print(x)
    if(x ==5):
        break
    x +=1


