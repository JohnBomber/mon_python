x = int(input("un nombre 1 "))
y = int(input("un nombre 2 "))
z = int(input("un nombre 3 "))


if z > y and z > x:
    print("le plus grand est " + str(z))
elif y > x and y > z:
    print("le plus grand est " + str(y))
else:
    print("le plus grand est " + str(x))
    


    
