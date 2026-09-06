"""
Tarea Semana 12: Reserva de un asiento en una sala de cine.

El programa crea una matriz de 3 filas por 4 columnas, solicita la
ubicación de un asiento, registra la reserva y muestra la sala completa.
"""

# Matriz de 3 filas por 4 columnas. El valor 0 representa un asiento libre.
asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

print("=== RESERVA DE ASIENTO EN SALA DE CINE ===")

try:
    # Se solicitan los índices de la fila y la columna del asiento.
    fila = int(input("Ingrese la fila del asiento (0 a 2): "))
    columna = int(input("Ingrese la columna del asiento (0 a 3): "))

    # Se comprueba que los índices pertenezcan a la matriz.
    if 0 <= fila <= 2 and 0 <= columna <= 3:
        # El valor 1 indica que el asiento ha sido reservado.
        asientos[fila][columna] = 1

        print(f"\nAsiento de la fila {fila}, columna {columna}, reservado correctamente.")
        print("\nEstado de la sala:")
        print("    0 1 2 3")

        # Los dos bucles anidados recorren todas las filas y columnas.
        for i in range(3):
            print(f"{i} | ", end="")
            for j in range(4):
                print(asientos[i][j], end=" ")
            print()  # Salto de línea al terminar cada fila.
    else:
        print("Error: la fila o la columna está fuera del rango permitido.")

except ValueError:
    print("Error: debe ingresar números enteros para la fila y la columna.")
