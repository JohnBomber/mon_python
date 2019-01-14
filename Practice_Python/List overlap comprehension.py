import random

a = random.sample(range(1,100), 30)
b = random.sample(range(1,100), 30)

print(a)
print(b)

c = []
c = [j for i in a for j in b if j == i if j not in c]

print(c)


d = set(a)
print(d)
