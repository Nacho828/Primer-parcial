from lanzador import crear_puntos, imprimir_puntos, consultar_vectores, consultar_distancias, crear_rectangulo

if __name__ == "__main__":
    A, B, C, D, O = crear_puntos()
    imprimir_puntos(A, B, C, D)
    consultar_vectores(A, B)
    consultar_distancias(A, B, C, O)
    crear_rectangulo(A, B)