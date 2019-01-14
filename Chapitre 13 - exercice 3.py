class Shape():
    def what_am_i(self):
        print("I am a shape")
        
class Rectangle(Shape):
    def __init__(self, c1, c2):
        self.longueur = c1
        self.largeur = c2
    def calculate_perimeter(self):
        return self.longueur * 2 + self.largeur *2

class Square(Shape):
    def __init__(self, c):
        self.coté = c
    def calculate_perimeter(self):
        return self.coté * 4

carré = Square(5)
rectangle = Rectangle(2,5)

carré.what_am_i()
rectangle.what_am_i()
