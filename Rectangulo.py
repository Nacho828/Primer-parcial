from Punto import Punto
class Rectangulo:
    def __init__(self, p1=Punto(), p2=Punto()):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f"Rectangulo: {self.p1}, {self.p2}"

    def area(self):
        base = abs(self.p1.x - self.p2.x)
        altura = abs(self.p1.y - self.p2.y)
        return base * altura
    
    def altura(self):
        return abs(self.p1.y - self.p2.y)
    
    def perimetro(self):
        base = abs(self.p1.x - self.p2.x)
        altura = abs(self.p1.y - self.p2.y)      
                                                
