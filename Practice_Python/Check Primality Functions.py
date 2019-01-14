while input("press q to quit ") != "q":
    number = input("choose an integer:" )
    try:
        number = int(number)
    except:
        print("please type an integer")
        break

    def prime(number):
        for i in range(2,number):
            if number % i == 0 and i != number:
                return "not prime number"
            

    print(prime(number))


