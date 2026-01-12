import tkinter as tk
import random

# Crear ventana
ventana = tk.Tk()
ventana.title("Tres en Raya")

tablero = [[" "]*3 for _ in range(3)]
botones = [[None]*3 for _ in range(3)]
turno = "X"  # jugador empieza

def reiniciar():
    global tablero, turno
    tablero = [[" "]*3 for _ in range(3)]
    for f in range(3):
        for c in range(3):
            botones[f][c]["text"] = " "
    turno = "X"

def comprobar_ganador():
    # Filas y columnas
    for i in range(3):
        if all(tablero[i][j]==turno for j in range(3)) or all(tablero[j][i]==turno for j in range(3)):
            return True
    # Diagonales
    if all(tablero[i][i]==turno for i in range(3)) or all(tablero[i][2-i]==turno for i in range(3)):
        return True
    return False

def pulsar(fila, col):
    global turno
    if tablero[fila][col] != " ":
        return
    tablero[fila][col] = turno
    botones[fila][col]["text"] = turno
    
    if comprobar_ganador():
        tk.messagebox.showinfo("¡Ganador!", f"¡Gana {turno}!")
        reiniciar()
        return
    elif all(tablero[f][c] != " " for f in range(3) for c in range(3)):
        tk.messagebox.showinfo("Empate", "¡Empate!")
        reiniciar()
        return

    turno = "O" if turno=="X" else "X"
    if turno=="O":
        # Jugada aleatoria máquina
        vacias = [(f,c) for f in range(3) for c in range(3) if tablero[f][c]==" "]
        if vacias:
            f,c = random.choice(vacias)
            pulsar(f,c)

# Crear botones
for f in range(3):
    for c in range(3):
        botones[f][c] = tk.Button(ventana, text=" ", width=6, height=3,
                                  command=lambda f=f, c=c: pulsar(f,c))
        botones[f][c].grid(row=f, column=c)

ventana.mainloop()

