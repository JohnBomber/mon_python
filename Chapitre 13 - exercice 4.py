class Horse():
    def __init__(self, nom):
        self.nom = nom

class Rider():
    def __init__(self, nom, cheval):
        self.nom = nom
        self.cheval = cheval

jolly = Horse("Jolly Jumper")
patrick = Rider("Patoche le beau", jolly)

print(patrick.nom)
print(patrick.cheval)
print(patrick.cheval.nom)
