def pendu():
    word = input("choississez un mot pour vous amuser comme des fous !! ")
    print("\n"*20)
    print("\n"*20)
    print("\n"*20)
    print("\n"*20)
    print("\n"*20)
    word = word.lower()
    wrong = 0
    stages = ["",
                 "__________        ",
                 "|                 ",
                 "|        |        ",
                 "|        0        ",
                 "|       /|\       ",
                 "|       / \       ",
                 "|_____       _____",
                  ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Bienvenue dans le jeu du pendu !")
    print("c'est un mot de " + str(len(word)) + " lettres")
    print(" ".join(board))

    while wrong < len(stages)-1 :
        print("\n")
        guess = input("Quelle lettre ? ")
        if guess in rletters:
            print("Tout a fait, bien joué !")
            position = rletters.index(guess)
            board[position] = guess
            rletters[position] = "$"
            print(" ".join(board))
        else:
            print("Non non non!")
            wrong += 1
            print("\n".join(stages[0:wrong+1]))
            print(" ".join(board))
        if "__" not in board:
            print("Bravo vous avez gagné")
            print("Le mot était bel et bien: " + word)
            print("\n".join(stages[0:wrong+1]))
            win = True
            break

    if not win:
	    print("Vous avez perdu!")
