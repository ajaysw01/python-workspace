# Sets : 
# unordeered, mutable, no duplications

myset = {1,2,3,1,2}
print(myset)

set1 = set("hello")
print(set1)


# empty = {}
empty = set()
print(type(empty))

myset.add(5)
print(myset)

for i in myset : 
    print(i)


# union and intersection

odds = {1,3,5,7,9}
evens ={2,4,6,8,10}
primes = {2,3,5,7,11}

u = odds.union(evens)
print(u)

i = odds.intersection(primes)
print(i)


# differnce
d = evens.difference(evens)
print(d)


print(primes.issubset(evens))
print(primes.issubset(odds))
print(primes.isdisjoint(evens))