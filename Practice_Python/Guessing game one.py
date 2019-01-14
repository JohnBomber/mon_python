import random

c = "yes"

while c != "q":
    a = random.randint(1,9)
    b = 0
    i = 0

    while b != a:
        b = input("give a number: ")
        b = int(b)
        if b == a:
            print("good job")
        elif b < a:
            print("More")
        else:
            print("Less")
        i += 1

    print("number of tries " + str(i))
    c = input("press q to quit")
