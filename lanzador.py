
# Métodos heredados de Punto

from punto import Punto
from Rectangulo import Rectangulo


def mover(self, dx, dy):
    self.x += dx
    self.y += dy

def distancia(self, otro_punto):
    return ((self.x - otro_punto.x) ** 2 + (self.y - otro_punto.y) ** 2) ** 0.5

# Métodos heredados de Rectangulo
def area(self):
    return self.ancho * self.alto

def perimetro(self):
    return 2 * (self.ancho + self.alto)

def mover(self, dx, dy):
    self.esquina_inferior_izquierda.mover(dx, dy)

def contiene(self, punto):
    x1 = self.esquina_inferior_izquierda.x
    y1 = self.esquina_inferior_izquierda.y
    x2 = x1 + self.ancho
    y2 = y1 + self.alto
    return x1 <= punto.x <= x2 and y1 <= punto.y <= y2

