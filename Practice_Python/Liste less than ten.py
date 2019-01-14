a = [1,1,2,3,5,8,13,21,34,55,89]
b = []
for i in a:
    if i < 5:
        print(i)
    else:
        continue
x = input("give me a number ")
try:
    x = int(x)
    for i in a:
        if i < x:
            b.append(i)
    print(b)
except:
    print("type a number")

