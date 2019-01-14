a = [1,1,2,3,5,8,13,21,34,55,89,6,9]
b = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,19,54,55,56]
c = []

for i in a:
    for j in b:
        if j == i:
            if j not in c:
                c.append(j)
print(c)
