def fibonacci():
    a = input("How many occurences do you want ? ")
    a = int(a)
    c = [1,1]
    for i in range(1,a-1):
        c.append(c[i] + c[i-1])
    return c
print(fibonacci())
