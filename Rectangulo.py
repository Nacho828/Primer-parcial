from Punto import Punto
class Rectangulo:
    def __init__(self, p1=None, p2=None):
        self.p1 = p1 if p1 else Punto(0, 0)
        self.p2 = p2 if p2 else Punto(0, 0)
        self.p2 = p2
        if not isinstance(p1, Punto) or not isinstance(p2, Punto):
            raise TypeError("p1 and p2 must be instances of Punto")
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
                                                
