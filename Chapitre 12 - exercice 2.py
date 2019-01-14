import math

class Circle():
    def __init__(self, r):
        self.rayon = r
    def area(self):
        print((self.rayon ** 2) * math.pi)

cercle1 = Circle(5)
Circle.area(cercle1)
