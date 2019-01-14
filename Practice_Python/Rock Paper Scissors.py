continuer = "yes"
import random

while continuer != "no":
    Player1 = input("Rock, Paper, Scissors ?")
    RPS = ("Rock", "Paper", "Scissors")
    Player2 = RPS[random.randint(0,2)]
    if Player1 not in RPS:
        print("Wrong answer")
        continuer = input("Play again ?")
    elif Player2 == Player1:
        print("draw")
        continuer = input("Play again ?")
    elif Player2 == "Scissors" and Player1 == "Paper":
        print("Player 2 wins")
        continuer = input("Play again ?")
    elif Player2 == "Rock" and Player1 == "Scissors":
        print("Player 2 wins")
        continuer = input("Play again ?")
    elif Player2 == "Paper" and Player1 == "Rock":
        print("Player 2 wins")
        continuer = input("Play again ?")
    else:
        print("Player 1 wins")
        continuer = input("Play again ?")
print(Player2)
