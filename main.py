from lanzador import crear_puntos, imprimir_puntos, consultar_vectores, consultar_distancias, crear_rectangulo
from lanzador import consultar_cuadrantes
from lanzador import determinar_punto_mas_lejos

def main():
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
    print("Perímetro del rectángulo:", rectangulo.perimetro())


if __name__ == "__main__":
    main()
