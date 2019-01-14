import random
cows = 0

print("Welcome to the Cows and Bulls Game!")

def numbers():
    return random.randint(0,9)

def toguess():
    x1 = str(numbers())
    x2 = str(numbers())
    x3 = str(numbers())
    x4 = str(numbers())
    return [x1,x2,x3,x4]
    
def compare_numbers(number, user_guess):
    cowbull = [0,0] #cow then bulls
    try:
        for i in range(len(number)):
            if number[i] == user_guess[i]:
                cowbull[1]+=1
            else:
                cowbull[0]+=1
    except:
        print("Type a 4 digit number !!")
    return cowbull

count = 0

if __name__ == "__main__":
    playing = True
    count = 0
    number = toguess()

    print("Let's play a game of Cowbull!") #explanation
    print("I will generate a number, and you have to guess the numbers one digit at a time.")
    print("For every number in the wrong place, you get a cow. For every one in the right place, you get a bull.")
    print("The game ends when you get 4 bulls!")
    print("Type exit at any prompt to exit.")    

        
    while playing:
        count += 1
        user_guess = input("Enter a 4 digit number:\n")
        if user_guess == "exit":
            break
        cowbullcount = compare_numbers(number,user_guess)
        if cowbullcount[0] > 1 and cowbullcount[1]>1:
            print(str(cowbullcount[0]) + " cows, " + str(cowbullcount[1]) + " bulls")
        elif cowbullcount[0] > 1 and cowbullcount[1] <= 1:
            print(str(cowbullcount[0]) + " cows, " + str(cowbullcount[1]) + " bull")
        elif cowbullcount[0] <= 1 and cowbullcount[1] > 1:
            print(str(cowbullcount[0]) + " cow, " + str(cowbullcount[1]) + " bulls")
        else:
            print(str(cowbullcount[0]) + " cow, " + str(cowbullcount[1]) + " bull")

        if cowbullcount[1] == 4:
            playing = False
            print("Good job, in " + str(count) + " tries!")

