class Shoe:
    def __init__(self, brand, size, color):
        self.brand = brand
        self.size = size
        self.color = color

    def __str__(self):
        return f"{self.brand} shoes, Size {self.size}, Color {self.color}"
