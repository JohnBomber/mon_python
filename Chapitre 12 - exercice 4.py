class Hexagon():
    def __init__(self,c):
        self.cote = c
    def calculate_perimeter(self):
        print(self.cote * 6)

hexagon1 = Hexagon(6)
Hexagon.calculate_perimeter(hexagon1)
