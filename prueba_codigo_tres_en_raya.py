import random

tablero_interno = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def mostrar_tablero(tablero_interno):
    print("    1   2   3")
    for n_de_fila, fila in enumerate(tablero_interno):
        print(f"{n_de_fila + 1}   {fila[0]} | {fila[1]} | {fila[2]}")
        if n_de_fila < 2:
            print("   ---+---+---")

def iniciar_juego():
    print("Bienvenido al Tres en Raya, un juego tradicional que nunca pasa de moda. ")
    print("Para ganar, tienes que consegir que tus fichas estén en tres casillas consecutivas, bien sea en vertical, horizontal o diagonal.")
    print("Vamos a ver de que pasta estás hecha ¡Que empiece el juego! pero antes, contesta a esta pregunta:")
    print("¿Cómo quieres jugar?")
    print("1. Contra la máquina")
    print("2. Contra otro jugador")

    while True:
        modo = input("Elige 1 o 2: ")
        if modo in ["1", "2"]:
            if modo == "1":
                print("Has elegido jugar contra mi. Perfecto, intenta ganarme a ver si puedes. Yo seré las O y tú las X. Empiezas tú, te dejo ventaja, a ver que sabes hacer.")
            else:
                print("Perfecto, seré una espectadora. La jugadora 1 será las X y la jugadora 2 será las O. Jugadora 1, es tu turno ¡Que empiece el espectáculo!")
            return modo
        else:
            print("Opción no válida. Intenta de nuevo.")

def pedir_jugada(tablero, turno):
    while True:
        try:
            fila = int(input("Elige la fila (1-3): ")) - 1
            columna = int(input("Elige la columna (1-3): ")) - 1
            if fila not in [0,1,2] or columna not in [0,1,2]:
                print("Fila o columna no válida. Deben ser 1, 2 o 3.")
                continue
            if tablero[fila][columna] != " ":
                print("La casilla que elegiste ya está ocupada. Elige otra.")
                continue
            tablero[fila][columna] = turno
            break
        except ValueError:
            print("Por favor, introduce un número válido.")

def hay_ganadora(tablero, turno):
    # Filas
    for fila in tablero:
        if all(casilla == turno for casilla in fila):
            return True
    # Columnas
    for col in range(3):
        if all(tablero[fila][col] == turno for fila in range(3)):
            return True
    # Diagonales
    if all(tablero[i][i] == turno for i in range(3)):
        return True
    if all(tablero[i][2 - i] == turno for i in range(3)):
        return True
    return False

def tablero_lleno(tablero):
    for fila in tablero:
        if " " in fila:
            return False
    return True

def turno_maquina_inteligente(tablero, turno, turno_maquina_num):
    jugadora_humana = "X" if turno == "O" else "O"

    # Primera jugada: aleatoria
    if turno_maquina_num == 1:
        vacias = [(f,c) for f in range(3) for c in range(3) if tablero[f][c] == " "]
        fila, col = random.choice(vacias)
        tablero[fila][col] = turno
        print(f"La máquina coloca {turno} en la fila {fila+1}, columna {col+1} (random)")
        return

    # Función interna: intentar ganar o bloquear
    def buscar_jugada(turno_objetivo):
        for f in range(3):
            for c in range(3):
                if tablero[f][c] == " ":
                    tablero[f][c] = turno_objetivo
                    if hay_ganadora(tablero, turno_objetivo):
                        tablero[f][c] = turno
                        print(f"La máquina coloca {turno} en la fila {f+1}, columna {c+1} (estratégico)")
                        return True
                    tablero[f][c] = " "
        return False

    # Intentar ganar
    if buscar_jugada(turno):
        return
    # Bloquear al humano
    if buscar_jugada(jugadora_humana):
        return
    # Si no hay nada, poner en la primera casilla vacía
    for f in range(3):
        for c in range(3):
            if tablero[f][c] == " ":
                tablero[f][c] = turno
                print(f"La máquina coloca {turno} en la fila {f+1}, columna {c+1}")
                return

def reiniciar_tablero(tablero):
    for f in range(3):
        for c in range(3):
            tablero[f][c] = " "

def jugar():
    modo = iniciar_juego()
    if modo == "1":
        jugadora1 = "X"  # humano
        jugadora2 = "O"  # máquina
    else:
        jugadora1 = "X"
        jugadora2 = "O"

    tablero = tablero_interno
    turno = jugadora1
    turno_maquina_num = 1

    mostrar_tablero(tablero)

    while True:
        print(f"\nTurno de la jugadora {turno}\n")

        if modo == "1" and turno == jugadora2:
            turno_maquina_inteligente(tablero, turno, turno_maquina_num)
            turno_maquina_num += 1
        else:
            pedir_jugada(tablero, turno)

        mostrar_tablero(tablero)

        if hay_ganadora(tablero, turno):
            print(f"\n¡Tenemos ganadora! Ganan las {turno} !\n")
            reiniciar_tablero(tablero)
            break

        if tablero_lleno(tablero):
            print("\n¡Empate! Que partida tan reñida ¿Jugamos otra?\n")
            reiniciar_tablero(tablero)
            break

        turno = jugadora2 if turno == jugadora1 else jugadora1

# Punto de entrada
if __name__ == "__main__":
    jugar()
