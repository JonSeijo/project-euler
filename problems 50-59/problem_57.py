# -*- coding: utf-8 -*-

# Square root convergents
# Problem 57

"""
It is possible to show that the square root of two
can be expressed as an infinite continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408,
but the eighth expansion, 1393/985, is the first example
where the number of digits in the numerator exceeds
the number of digits in the denominator.

In the first one-thousand expansions,
how many fractions contain a numerator with more digits than denominator?
"""


def crearSucesiones():
    """
    Jonathan Seijo

    Las fracciones que quiero analizar son:

    1+(1/2), 1+(2/5), 1+(5/12), 1+(12/29), 1+(29/70),..

    considero an/bn = (1/2), (2/5), (5/12), (12/29), (29/70), ..
    puedo definir esta sucesion por recurrencia como:

    a1 = 1
    b1 = 2

    an = b(n-1)
    bn = 2*b(n-1) + a(n-1)

    --> 'an' contiene al numerador en la posicion n
    --> 'bn' contiene al denominador en la posicion n
    """

    an = [1]
    bn = [2]

    for n in range(1, 1001):
        an.append(bn[n-1])
        bn.append(2*bn[n-1] + an[n-1])

    return an, bn


def main():
    # Creo las suceciones de numeradores y denominadores
    an, bn = crearSucesiones()

    answer = 0

    for n in range(0, 1000):
        # 1 + (an/bn) = (bn + an)/bn
        if len(str(bn[n] + an[n])) > len(str(bn[n])):
            answer += 1

    print "answer: " + str(answer)


if __name__ == "__main__":
    main()
