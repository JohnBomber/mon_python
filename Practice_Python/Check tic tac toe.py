liste_liste = [[1, 2, 1], [2, 2, 1], [2, 1, 1]]

def check_tic_tac_toe(liste_liste):
    liste0 = liste_liste[0]
    liste1 = liste_liste[1]
    liste2 = liste_liste[2]
    x = "No winner"

    #horizontal
    for i in range(0,3):
        liste = liste_liste[i]
        if liste[0] == liste[1] == liste[2] and liste[0] != 0:
            x = "Player " + str(liste[0]) + " has  won horizontally on line " + str(i)

    #vertical
    for j in range(0,3):
        if liste0[j] == liste1[j] == liste2[j] and liste0[j] != 0:
            x = "Player " + str(liste0[j]) + " has  won vertically on column " + str(j)

    #diagonale gauche à droite
    if liste0[0] == liste1[1] == liste2[2] and liste0[0] != 0:
        x  = "Player " + str(liste0[0]) + " has  won diagonally from top left to bottom right"

    #diagonale droite à gauche
    if liste0[2] == liste1[1] == liste2[0] and liste0[2] != 0:
        x = "Player " + str(liste0[2]) + " has  won diagonally from top right to bottom left"

    return(x)

# méthode utilisant intelligemment set = pas de doublon ==> vérifier si un seul élément différent de 0
"""
def checkGrid(grid):
	# rows
	for x in range(0,3):
		row = set([grid[x][0],grid[x][1],grid[x][2]])
		if len(row) == 1 and grid[x][0] != 0:
			return grid[x][0]

	# columns
	for x in range(0,3):
		column = set([grid[0][x],grid[1][x],grid[2][x]])
		if len(column) == 1 and grid[0][x] != 0:
			return grid[0][x]

	# diagonals
	diag1 = set([grid[0][0],grid[1][1],grid[2][2]])
	diag2 = set([grid[0][2],grid[1][1],grid[2][0]])
	if len(diag1) == 1 or len(diag2) == 1 and grid[1][1] != 0:
		return grid[1][1]

	return 0

winner_is_2 = [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]
winner_is_1 = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

also_no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]

print(checkGrid(also_no_winner))
"""
