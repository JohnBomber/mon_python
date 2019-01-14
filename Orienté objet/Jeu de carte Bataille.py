from random import shuffle
# permet de mélanger aléatoirement une liste

# class Cartes qui détermine la valeur et la couleur d'une carte. Leur ordre dans les listes correspond à leur puissance.
# le print a été redéfini afin qu'il donne la valeur de la carte.
class Cartes():
    # les valeurs et couleurs sont triées par ordre de puissance dans les listes
    valeurs = [None,None,"2","3","4","5","6","7","8","9","10","valet","dame","roi","as"]
    couleurs = ["Pique", "Coeur", "Carreau", "Trèfle"]
    def __init__(self,v,c):
        #v et c sont des integer
        self.valeur = v
        self.couleur = c

    def __repr__(self):
        #v et c permettent de ressortir en string la carte obtenue
        return self.valeurs[self.valeur] + " de " + self.couleurs[self.couleur]
    
    def __lt__(self, c2):
        # remplacer la magic method "<" pour tester les valeurs des integer v & c pour déterminer si < ==> True N'est pas utilisé dans la class Game()
        if self.valeur < c2.valeur:
            return True
        # cas de 2 valeurs identiques, teste la couleur
        elif self.valeur == c2.valeur:
            if self.couleur < c2.couleur:
                return True
            else:
                return False
        else:
            return False

    def __gt__(self,c2):
        # remplacer la magic method ">" pour tester les valeurs des integer v & c pour déterminer si < ==> True
        if self.valeur > c2.valeur:
            return True
        # cas de 2 valeurs identiques, teste la couleur
        elif self.valeur == c2.valeur:
            if self.couleur > c2.couleur:
                return True
            else:
                return False
        else:
            return False
        
            

# Créer un jeu de 52 cartes et le mélanger aléatoirement avec shuffle
class Deck():
    def __init__(self):
        self.cartes = []
        # créer un jeu de 52 cartes complet à l'aide de la classe Cartes et le mélanger à l'aide de la méthode shuffle du module random
        for i in range(2,15):
            for j in range(4):
                self.cartes.append(Cartes(i,j))
        shuffle(self.cartes)

    # permet de récupérer la dernière carte du paquet et de la supprimer de la liste
    def rm_carte(self):
        if len(self.cartes) == 0:
            return
        return self.cartes.pop()

# récupérer le nom d'un joueur et créer une variable pour compter son nombre de victoire + une variable permettant de stocker la carte tirée (via Deck().rm_carte)
class Player():
    def __init__(self, nom):
        self.win = 0
        self.carte = None
        self.nom = nom

class Game():
    # Créer un paquet de carte et input le nom des 2 joueurs (intégrés en variable j1 et j2) dans la class Player
    def __init__(self):
        self.deck = Deck()
        nom1 = input("Nom du joueur 1: ")
        nom2 = input("Nom du joueur 2: ")
        self.j1 = Player(nom1)
        self.j2 = Player(nom2)

    # méthode pour print le nom du gagnant (gagnant = nom d'un des 2 joueurs)
    def wins(self, gagnant):
        g = "{} a gagné ce tour\n"
        g = g.format(gagnant)
        print(g)

    # méthode pour print les pioches
    def pioche(self, j1n, j1c, j2n, j2c):
        p = "{} a pioché un {} et {} a pioché un {}"
        p = p.format(j1n,j1c,j2n,j2c)
        print(p)

    # méthode pour déterminer le gagnant en reprenant j1 et j2 qui correspondent à Player(nom1) et Player(nom2)
    def gagnant(self,j1,j2):
        if j1.win > j2.win:
            return j1.nom
        elif j1.win < j2.win:
            return j2.nom
        else:
            return "Match nul"
        

    def jouer(self):
        # cartes est la liste de cartes créée via la class Deck
        cartes = self.deck.cartes
        print("Que la Bataille commence !")
        # tant qu'il y a au moins 2 cartes dans le paquet
        while len(cartes) >= 2:
            prompt = input("Appuyer sur q pour quitter, ou n'importe quelle touche pour continuer: ")
            if prompt == "q":
                break
            # j1c appelle la classe Deck() et sa méthode rm_carte qui passe par la classe Carte() qui va obtenir les valeurs v et c des cartes
            else:
                j1c = self.deck.rm_carte()
                j2c = self.deck.rm_carte()
                j1n = self.j1.nom
                j2n = self.j2.nom
                self.pioche(j1n,j1c,j2n,j2c)
                # va comparer les valeurs v et c obtenues via j1c et j2c dans le magic méthode __gt__ de Cartes()
                if j1c > j2c:
                    self.j1.win += 1
                    self.wins(self.j1.nom)
                else:
                    self.j2.win += 1
                    self.wins(self.j2.nom)
                    
        win = self.gagnant(self.j1, self.j2)
        print("Bataille terminée. {} a gagné ! \n Score final: {} {} contre {} {}".format(win,j1n, self.j1.win, j2n, self.j2.win))

go = Game().jouer()
