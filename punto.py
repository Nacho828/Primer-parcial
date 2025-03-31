class punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return "I"
        elif self.x < 0 and self.y > 0:
            return "II"
        elif self.x < 0 and self.y < 0:
            return "III"
        elif self.x > 0 and self.y < 0:
            return "IV"
        elif self.x == 0 and self.y != 0:
            return "Eje Y"
        elif self.y == 0 and self.x != 0:
            return "Eje X"
        else:
            return "Origen"

    def vector(self, other):
        return (other.x - self.x, other.y - self.y)

    def distancia(self, other):
        return ((other.x - self.x)**2 + (other.y - self.y)**2)**0.5