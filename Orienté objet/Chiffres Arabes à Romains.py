class ChiffreRomain():
    romain = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    arabe =  [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    def __init__(self):
        self.chiffre = int(input("Donner un nombre entier à convertir en Chiffre Romain: "))

    def convertir(self):
        resultat = []
        chiffre = self.chiffre
        i = 0
        while i < len(self.romain):
            a = chiffre // self.arabe[i]
            resultat.append(self.romain[i] * a)
            chiffre = chiffre - self.arabe[i] * a
            i += 1
        return "".join(resultat)

print(ChiffreRomain().convertir())
