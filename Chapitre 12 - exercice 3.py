class Triangle():
    def __init__(self, b, h):
        self.base = b
        self.hauteur = h
    def area(self):
        print(self.base * self.hauteur **2)

triangle1 = Triangle(3,5)
Triangle.area(triangle1)
