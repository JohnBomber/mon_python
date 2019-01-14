import random
x = random.sample(range(1,20),15)
y = random.sample(range(1,20),15)
a = x + y
print(a)

def loop(x):
    y = []
    for i in x:
        if i not in y:
            y.append(i)
    return y

def loop2(x):
    y = []
    [y.append(i) for i in x if i not in y]
    return y

def mode_set(x):
    return list(set(x))
