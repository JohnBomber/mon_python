class Square:
    square_liste = []
    def __init__(self, coté):
        self.coté = coté
        self.square_liste.append(self.coté)
    def __repr__(self):
        return "{} by {} by {} by {}".format(self.coté,self.coté,self.coté,self.coté)

c1 = Square(5)
c2 = Square(10)

print(Square.square_liste)
print(c1)
print(c2)
