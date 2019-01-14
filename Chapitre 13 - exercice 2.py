class Square():
    def __init__(self, c):
        self.coté = c
    def calculate_perimeter(self):
        return self.coté * 4
    def change_size(self, nombre):
        self.coté += nombre

carré = Square(100)

print(carré.coté)
carré.calculate_perimeter

carré.change_size(200)

print(carré.coté)
carré.calculate_perimeter

