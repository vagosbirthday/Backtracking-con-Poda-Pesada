def es_seguro(tablero, fila, columna, N):
    # Comprobar esta columna hacia arriba
    for i in range(fila):
        if tablero[i][columna] == 1:
            return False

    # Comprobar diagonal superior izquierda
    for i, j in zip(range(fila, -1, -1), range(columna, -1, -1)):
        if tablero[i][j] == 1:
            return False

    # Comprobar diagonal superior derecha
    for i, j in zip(range(fila, -1, -1), range(columna, N)):
        if tablero[i][j] == 1:
            return False

    return True


def resolver_n_reinas(tablero, fila, N):
    """
    Usa backtracking para resolver el problema N-Queens desde una fila específica.
    """
    if fila >= N:
        return True  # Todas las reinas han sido colocadas correctamente

    for columna in range(N):
        if es_seguro(tablero, fila, columna, N):
            # Colocar la reina en esta posición
            tablero[fila][columna] = 1

            # Intentar colocar el resto de las reinas
            if resolver_n_reinas(tablero, fila + 1, N):
                return True

            # Backtracking: quitar la reina si no conduce a una solución
            tablero[fila][columna] = 0

    return False


def mostrar_tablero(tablero, N):
    """
    Muestra el tablero resultante con ceros y unos.
    """
    for fila in tablero:
        print("{", "  ".join(map(str, fila)), "}")


def main():
    print("Problema N-Queens usando Backtracking.")
    print("Puedes elegir un tablero de tamaño 4x4 u 8x8.")
    N = int(input("Ingrese el tamaño del tablero (4 u 8): "))
    
    if N not in [4, 8]:
        print("Solo se permiten tamaños de tablero 4 o 8. Por favor, intente de nuevo.")
        return

    # Crear un tablero NxN inicializado con ceros
    tablero = [[0 for _ in range(N)] for _ in range(N)]

    # Resolver el problema
    if resolver_n_reinas(tablero, 0, N):
        print(f"Solución para un tablero de {N}x{N}:")
        mostrar_tablero(tablero, N)
    else:
        print(f"No se encontró una solución para un tablero de {N}x{N}.")

main()
