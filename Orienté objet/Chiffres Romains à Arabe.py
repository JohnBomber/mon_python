class ChiffreRomain():
    romain1 = ["M","D","C","L","X","V","I"]
    arabe1 =  [1000,500,100,50,10,5,1]
    romain2 = ["CM","CD","XC","XL","IX","IV"]
    arabe2 = [900,400,90,40,9,4]
    def __init__(self):
        self.chiffre = input("Donner un chiffre Romain à convertir en Chiffre Arabe: ")

    def convertir(self):
        resultat = 0
        chiffre = self.chiffre
        romain1 = self.romain1
        romain2 = self.romain2
        arabe1 = self.arabe1
        arabe2 = self.arabe2
        c = len(chiffre)
        for ind,val in enumerate(romain2):
            a = 0
            b = 2
            while b < c:
                if val == chiffre[a:b]:
                    resultat += arabe2[ind]
                a += 1
                b += 1

        for double in romain2:
            chiffre = chiffre.split(double)
            chiffre = "".join(chiffre)

        for j in chiffre:
            for ind,val in enumerate(romain1):
                if j == val:
                    resultat += arabe1[ind]
        return resultat

print(ChiffreRomain().convertir())
