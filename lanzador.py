from punto import Punto
from Rectangulo import Rectangulo  # Ensure the file is named 'rectangulo.py' with the correct case

def recorrer_puntos(puntos):
    for punto in puntos:
        print(f"Punto: {punto}, Cuadrante: {punto.cuadrante()}")

def recorrer_vectores(puntos):
    for i in range(len(puntos)):
        for j in range(i + 1, len(puntos)):
            print(f"Vector de {puntos[i]} a {puntos[j]}: {puntos[i].vector(puntos[j])}")

def recorrer_distancias(puntos, origen):
    for punto in puntos:
        print(f"Distancia de {punto} al origen {origen}: {punto.distancia(origen)}")

def recorrer_rectangulos(rectangulos):
    for rectangulo in rectangulos:
        print(f"Rectángulo con base {rectangulo.base()} y altura {rectangulo.altura()}, Área: {rectangulo.area()}")

# Lógica principal
def crear_puntos():
    A = Punto(0, 0)
    B = Punto(1, 2)
    C = Punto(3, 4)
    D = Punto(-1, -3)
    return A, B, C, D

def crear_rectangulo(p1, p2):
    return Rectangulo(p1, p2)

A, B, C, D = crear_puntos()
puntos = [A, B, C, D]
recorrer_puntos(puntos)
recorrer_vectores(puntos)
recorrer_distancias(puntos, D)

rectangulo = crear_rectangulo(A, B)
rectangulos = [rectangulo]
recorrer_rectangulos(rectangulos)
