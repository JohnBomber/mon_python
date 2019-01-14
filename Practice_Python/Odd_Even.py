num = input("Type a number ")
check = input("Type a number (not 0) ")
try:
    num = int(num)
    check = int(check)
    x = check / num
    x= float(x)
    print(x)
    if x % 4 == 0:
        print("multiple of 4")
    elif x % 2 == 0:
        print("even number")
    else:
        print("odd number")
except:
    print("type a number")


