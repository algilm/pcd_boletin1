fichas = ['o', 'x']

def mostrar_tablero(n, movimientos_jugadores):
    for i in range(n):
        for j in range(n):
            casilla_vacia = True
            for k in range(len(movimientos_jugadores)):
                movimientos_jugador = movimientos_jugadores[k]
                if i in movimientos_jugador:
                    if j in movimientos_jugador[i]:
                        print(fichas[k], end=' ')
                        casilla_vacia = False
            if casilla_vacia:
                print('_', end=' ')
        print()


if __name__ == "__main__":
    n = 3
    movimientos_jugador_1 = {}
    movimientos_jugador_2 = {}
    movimientos_jugadores = [movimientos_jugador_1, movimientos_jugador_2]
    mostrar_tablero(n, movimientos_jugadores)


def movimiento_valido(n, x, y, movimientos_otro_jugador):
    # fuera del tablero
    if x < 0 or y < 0 or x >= n or y >= n:
        return False

    # casilla ocupada por el otro jugador
    if x in movimientos_otro_jugador:
        if y in movimientos_otro_jugador[x]:
            return False

    return True


def jugada_ganadora(movimientos_jugador, n=3):
    # Comprueba si hay n fichas en alguna fila (versión simple del boletín)
    for fila, columnas in movimientos_jugador.items():
        if len(columnas) == n:
            return True
    return False