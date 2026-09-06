# Reserva de un asiento en sala de cine

## Datos del estudiante

- **Nombre:** Diego Martín Guashpa Bonilla
- **Asignatura:** Fundamentos de Programación
- **Semana:** 12
- **Unidad:** Unidad 3. Arreglos N-Dimensionales

## Objetivo

Desarrollar un programa en Python que represente una sala de cine mediante una matriz de 3 filas por 4 columnas, permita reservar un asiento por sus índices y muestre el estado completo de la sala utilizando bucles anidados.

## Funcionamiento

El programa:

1. Crea la matriz `asientos` con todos sus valores en `0`.
2. Solicita una fila entre `0` y `2`.
3. Solicita una columna entre `0` y `3`.
4. Cambia a `1` el asiento seleccionado.
5. Recorre la matriz con dos bucles anidados y muestra la sala en forma de tabla.
6. Valida que los índices sean correctos y que se ingresen números enteros.

## Requisitos

- Python 3 instalado.

## Ejecución

Abra una terminal en la carpeta del proyecto y ejecute:

```bash
python reserva_cine.py
```

En algunos equipos con Windows puede utilizar:

```bash
py reserva_cine.py
```

## Ejemplo

Si se ingresa la fila `1` y la columna `2`, el resultado será:

```text
Estado de la sala:
    0 1 2 3
0 | 0 0 0 0
1 | 0 0 1 0
2 | 0 0 0 0
```

El valor `1` identifica el asiento reservado y los valores `0` corresponden a asientos libres.
