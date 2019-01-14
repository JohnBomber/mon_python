x = input("Give a number ")
try:
    x = int(x)
except:
    print("this field only accepts numbers")
a = list()

for i in range(1,100):
    if i % 5 == 0:
        a.append(i)

print(a)
