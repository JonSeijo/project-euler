# Problem 58
# Spiral primes

"""

Starting with 1 and spiralling anticlockwise in the following way,
a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along
the bottom right diagonal,
but what is more interesting is that 8 out of the 13 numbers
lying along both diagonals are prime; that is, a ratio of 8/13 = 62%.

If one complete new layer is wrapped around the spiral above,
a square spiral with side length 9 will be formed.
If this process is continued, what is the side length
of the square spiral for which the ratio of primes
along both diagonals first falls below 10%?
"""

import math


def esPrimo(number):
    """
    Podria hacerse mas eficiente,
    pueden verse en las mil veces
    que hice esta funcion en los problemas anteriores.
    Fiaca.
    """

    if number == 2 or number == 3:
        return True

    if number % 2 == 0:
        return False

    for n in range(3, int(math.sqrt(number))+1, 2):
        if number % n == 0:
            return False

    return True


def main():
    """
    37 36 35 34 33 32 31
    38 17 16 15 14 13 30
    39 18  5  4  3 12 29
    40 19  6  1  2 11 28
    41 20  7  8  9 10 27
    42 21 22 23 24 25 26
    43 44 45 46 47 48 49

    Voy a encerrar con parentesis los numeros que estan en la diagonal

    2 (3) 4 (5) 6 (7) 8 (9)   diagonal cada 2
    10 11 12 (13) 14 15 16 (17) 18 19 20 (21) 22 23 24 (25)   diagonal cada 4
    26 27 28 29 30 (31) 32 33 34 35 36 (37) .... diagonal cada 6

    cada cuatro numeros en la diagonal, la distancia entre ellos
    (el espaciado) aumenta en 2

    contando solo los numeros en la diagonal,
    veo cuantos son primos,
    y por cada vuelta (4 diagonales)
    veo si la proporcion es menor a 10% = 0.10

    """
    contador = 0
    espaciado = 2
    nActual = 1
    nDiagonales = 1  # Contando el 1 central
    nPrimos = 0
    answer = 0

    while answer == 0:
        contador += 1
        nActual += espaciado
        nDiagonales += 1  # numeros totales que estan en la diagonal

        if esPrimo(nActual):
            nPrimos += 1.   # Necesito punto flotante para la division

        if contador == 4:
            if nPrimos/nDiagonales < 0.10:
                answer = espaciado + 1
                break

            contador = 0
            espaciado += 2

    print "answer: " + str(answer)


if __name__ == "__main__":
    main()
