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

if __name__ == "__main__":
    n = int(input("Introduce el tamaño del tablero cuadrado: "))
    casillas_libres = n * n
    jugador_activo = 0

    movimientos_jugador_1 = {}
    movimientos_jugador_2 = {}
    movimientos_jugadores = [movimientos_jugador_1, movimientos_jugador_2]

    mostrar_tablero(n, movimientos_jugadores)

    while casillas_libres > 0:
        entrada = input(f"JUGADOR {jugador_activo + 1} (x,y): ")
        try:
            x, y = map(int, entrada.split(','))
            x -= 1
            y -= 1
        except ValueError:
            print("Formato incorrecto. Usa x,y")
            continue

        movimientos_jugador_activo = movimientos_jugadores[jugador_activo]
        movimientos_otro_jugador = movimientos_jugadores[(jugador_activo + 1) % 2]

        if movimiento_valido(n, x, y, movimientos_otro_jugador):
            columnas = movimientos_jugador_activo.get(x, [])
            columnas.append(y)
            movimientos_jugador_activo[x] = columnas

            print("\033c", end="")  # limpiar pantalla en macOS/Linux
            mostrar_tablero(n, movimientos_jugadores)

            if jugada_ganadora(movimientos_jugador_activo, n):
                print(f"🎉 ENHORABUENA JUGADOR {jugador_activo + 1}, HAS GANADO")
                break

            jugador_activo = (jugador_activo + 1) % 2
            casillas_libres -= 1
        else:
            print("Movimiento inválido. Intenta de nuevo.")