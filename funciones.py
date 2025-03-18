# este archivo tendra todas las funciones usadas en el juegoç

import random

tamaño_tablero = 10

# Crear tableros vacíos
def crear_tablero():
    return [[" " for _ in range(tamaño_tablero)] for _ in range(tamaño_tablero)]

# Definir los barcos con un diccionario
barcos = {
    'tiburón': 4,
    'orca2': 3,
    'orca1': 3,
    'delfínrosa3': 2,
    'delfínrosa2': 2,
    'delfínrosa1': 2,
    'piraña4': 1,
    'piraña3': 1,
    'piraña2': 1,
    'piraña1': 1
}

# Verificamos si una pocision es valida para colocar un barco

def posicion_valida(tablero, fila, columna, tamaño, direccion):
    cambios = {
        "arriba": (-1, 0),
        "abajo": (1, 0),
        "izquierda": (0, -1),
        "derecha": (0, 1)
    }
    cambio_fila, cambio_columna = cambios[direccion]

    for i in range(tamaño):
        nueva_fila = fila + (i * cambio_fila)
        nueva_columna = columna + (i * cambio_columna)

        if not (0 <= nueva_fila < tamaño_tablero and 0 <= nueva_columna < tamaño_tablero):
            return False
        if tablero[nueva_fila][nueva_columna] != " ":
            return False

    return True


# Colocar barcos en el tablero de manera aleatoria 
def colocar_barcos(tablero):
    for nombre, tamaño in barcos.items():
        colocado = False
        while not colocado:
            fila, columna = random.randint(0, tamaño_tablero-1), random.randint(0, tamaño_tablero-1)
            direccion = random.choice(["arriba", "abajo", "izquierda", "derecha"])
            if posicion_valida(tablero, fila, columna, tamaño, direccion):
                for i in range(tamaño):
                    if direccion == "arriba":
                        tablero[fila - i][columna] = "B"
                    elif direccion == "abajo":
                        tablero[fila + i][columna] = "B"
                    elif direccion == "izquierda":
                        tablero[fila][columna - i] = "B"
                    elif direccion == "derecha":
                        tablero[fila][columna + i] = "B"
                colocado = True


# para ver el tablero en un formato mas claro

def imprimir_tablero(nombre, tablero):
    print(f"\n{nombre.upper()}:")
    print("   " + " ".join(str(i) for i in range(tamaño_tablero)))
    print("  " + "---" * tamaño_tablero)
    for i, fila in enumerate(tablero):
        print(f"{i} |" + "|".join(fila) + "|")
    print("  " + "---" * tamaño_tablero)


# para verificar si quedan barcos en el tablero

def verificar_ganador(tablero):
    for fila in tablero:
        if "B" in fila: #Verifica si hay al menos una casilla con "B" en esa fila
            return False #Si encuentra "B", retorna False, indica que todavía hay barcos y el juego no ha terminado.
    return True


# permite al jugador atacar en su turno de ataque
def turno_jugador(tablero_computadora, tablero_computadora_mostrar):
    while True:
        try:
            fila = int(input("Introduce fila (0-9): "))
            columna = int(input("Introduce columna (0-9): "))

            if not (0 <= fila < tamaño_tablero and 0 <= columna < tamaño_tablero):
                print(" Coordenadas fuera de rango. Intenta de nuevo.")
                continue

            if tablero_computadora_mostrar[fila][columna] in ["X", "O"]:
                print(" Ya atacaste esta posición. Intenta de nuevo.")
                continue

            if tablero_computadora[fila][columna] == "B":
                print(" ¡Impacto! Hundiste parte de un barco enemigo.")
                tablero_computadora_mostrar[fila][columna] = "X"
                tablero_computadora[fila][columna] = "X"
            else:
                print("Agua.")
                tablero_computadora_mostrar[fila][columna] = "O"
            break  # Termina el turno

        except ValueError:
            print(" Entrada no válida. Ingresa números.")

# Simula el turno de la computadora al atacar las pocisiones del jugador
def turno_computadora(tablero_jugador, tablero_jugador_mostrar, disparos_realizados):
    while True:
        fila, columna = random.randint(0, tamaño_tablero-1), random.randint(0, tamaño_tablero-1)

        if (fila, columna) in disparos_realizados:
            continue  # Evita repetir disparos en la misma posición

        disparos_realizados.add((fila, columna))
        print(f"\n La computadora atacó la posición ({fila}, {columna})")

        if tablero_jugador[fila][columna] == "B":
            print("¡Te han dado!")
            tablero_jugador[fila][columna] = "X"
            tablero_jugador_mostrar[fila][columna] = "X"
        else:
            print(" La computadora falló.")
            tablero_jugador_mostrar[fila][columna] = "O"
        break  # Termina el turno
       