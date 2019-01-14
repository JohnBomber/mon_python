game = [[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]

count = 0
joueur = 2

#vérifier victoire
def check_tic_tac_toe(game):
    game0 = game[0]
    game1 = game[1]
    game2 = game[2]
    x = "Draw game"

    #horizontal
    for i in range(0,3):
        liste = game[i]
        if liste[0] == liste[1] == liste[2] and liste[0] != 0:
            x = "Player " + str(liste[0]) + " has  won horizontally on line " + str(i+1)

    #vertical
    for j in range(0,3):
        if game0[j] == game1[j] == game2[j] and game0[j] != 0:
            x = "Player " + str(game0[j]) + " has  won vertically on column " + str(j+1)

    #diagonale gauche à droite
    if game0[0] == game1[1] == game2[2] and game0[0] != 0:
        x  = "Player " + str(game0[0]) + " has  won diagonally from top left to bottom right"

    #diagonale droite à gauche
    if game0[2] == game1[1] == game2[0] and game0[2] != 0:
        x = "Player " + str(game0[2]) + " has  won diagonally from top right to bottom left"

    return(x)

#Remplacer les 0,1,2 en x,o,vide
def visuel(game):
    game_visuel = [["a", "b", "c"],
            ["d", "e", "f"],
            ["g", "h", "i"]]

    for ligne, liste in enumerate(game):
        for indexe, valeur in enumerate(liste):
            if valeur == 1:
                game_visuel[ligne][indexe] = "x"
            elif valeur == 2:
                game_visuel[ligne][indexe] = "o"
            else:
                game_visuel[ligne][indexe] = "_"

    print(" _ _ _")
    for ligne, liste in enumerate(game_visuel):
        x = "|".join(game_visuel[ligne])
        print("|" + x + "|")


while count <= 9:
    visuel(game)
    count += 1
    if joueur == 2:
        joueur = 1
    else:
        joueur = 2
    b = input("Player " + str(joueur) + " it is your turn to play, please indicate using row,column coordinates: ")
    row = int(b[0]) - 1
    column = int(b[2]) - 1

    if game[row][column] == 0:
        game[row][column] = joueur
    else:
        count -= 1
        print("spot already taken, try again player " + str(joueur))
        if joueur == 2:
            joueur = 1
        else:
            joueur = 2


    if check_tic_tac_toe(game) != "Draw game":
        visuel(game)        
        print(check_tic_tac_toe(game))
        break

    
