# este archivo contiene el flujo del juego y llama a las funciones desde funciones.py

from funciones import (
    crear_tablero, colocar_barcos, imprimir_tablero, verificar_ganador, 
    turno_jugador, turno_computadora
)


def jugar():
    print("\n ¡Bienvenido a Hundir la Flota! ")
    print(" Instrucciones: Ingresa las coordenadas para disparar (ejemplo: fila 3, columna 5).")
    print(" ¡Intenta hundir todos los barcos del rival antes de quedarte sin intentos!")

    # Crear tableros
    tablero_jugador = crear_tablero()
    tablero_jugador_mostrar = crear_tablero()
    tablero_computadora = crear_tablero()
    tablero_computadora_mostrar = crear_tablero()

    # Colocar barcos
    colocar_barcos(tablero_jugador)
    colocar_barcos(tablero_computadora)

    intentos = 20
    disparos_realizados = set()

    while intentos > 0:
        # Mostrar tableros
        imprimir_tablero("Tu tablero", tablero_jugador)
        imprimir_tablero("Tablero Computadora", tablero_computadora_mostrar)

        # Turno del jugador
        turno_jugador(tablero_computadora, tablero_computadora_mostrar)

        # Comprobar si el jugador ha ganado
        if verificar_ganador(tablero_computadora):
            print("\n ¡Felicidades! Hundiste todos los barcos de la computadora.")
            break

        # Turno de la Computadora
        turno_computadora(tablero_jugador, tablero_jugador_mostrar, disparos_realizados)

        # Comprobar si la Computadora ha ganado
        if verificar_ganador(tablero_jugador):
            print("\n La computadora ha ganado. ¡Sigue intentándolo!")
            break

        intentos -= 1

    if intentos == 0:
        print("\n Se acabaron los intentos. ")

    print("\n Tablero final:")
    imprimir_tablero("Tu tablero", tablero_jugador)
    imprimir_tablero("Tablero computadora", tablero_computadora)


jugar()