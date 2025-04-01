from Punto import Punto
from Rectangulo import Rectangulo
def crear_puntos():
    print("Ingrese las coordenadas de los puntos:")
    x1, y1 = map(float, input("Punto A (x y): ").split())
    x2, y2 = map(float, input("Punto B (x y): ").split())
    x3, y3 = map(float, input("Punto C (x y): ").split())
    x4, y4 = map(float, input("Punto D (x y): ").split())
    A = Punto(x1, y1)
    B = Punto(x2, y2)
    C = Punto(x3, y3)
    D = Punto(x4, y4)
    return A, B, C, D

def imprimir_puntos(A, B, C, D):
    print("Punto A:", A)
    print("Punto B:", B)
    print("Punto C:", C)
    print("Punto D:", D)

def consultar_cuadrantes(A, C, D):
    print("Cuadrante de A:", A.cuadrante())
    print("Cuadrante de C:", C.cuadrante())
    print("Cuadrante de D:", D.cuadrante())

def consultar_vectores(A, B):
    print("Vector AB:", A.vector(B))
    print("Vector BA:", B.vector(A))

def consultar_distancias(A, B, D):
    print("Distancia de A a B:", A.distancia(B))
    print("Distancia de B a A:", B.distancia(A))

def determinar_punto_mas_lejos(A, B, C, D):
    distancia_A = A.distancia(D)
    distancia_B = B.distancia(D)
    distancia_C = C.distancia(D)
    mas_lejos = max(distancia_A, distancia_B, distancia_C)
    if mas_lejos == distancia_A:
        print("El punto más lejos del origen es A")
    elif mas_lejos == distancia_B:
        print("El punto más lejos del origen es B")
    else:
        print("El punto más lejos del origen es C")

def crear_rectangulo(A, B):
    return Rectangulo(A, B)

def consultar_rectangulo(rectangulo):
    print("Base del rectángulo:", rectangulo.base())
    print("Altura del rectángulo:", rectangulo.altura())
    print("Área del rectángulo:", rectangulo.area())
    
def lanzada():
    A, B, C, D = crear_puntos()
    imprimir_puntos(A, B, C, D)
    consultar_cuadrantes(A, C, D)
    consultar_vectores(A, B)
    consultar_distancias(A, B, D)
    determinar_punto_mas_lejos(A, B, C, D)
    rectangulo = crear_rectangulo(A, B)
    print("Base del rectángulo:", rectangulo.base())
    print("Altura del rectángulo:", rectangulo.altura())
    print("Área del rectángulo:", rectangulo.area())

