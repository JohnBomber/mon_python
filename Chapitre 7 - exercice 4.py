liste = [12,36,24,58,97,84,65,15,98]
while True:
    x = input("guess a number or press q to quit")
    if x == "q":
        break
    try:
        x = int(x)
    except ValueError:
        print("Please type a number")
        continue
    if x in liste:
        print("you guessed correctly ")
    else:
        print("Wrong! Try again!")
    
