# Problem 80
# Square root digital expansion

"""
It is well known that if the square root of a natural number
is not an integer, then it is irrational.
The decimal expansion of such square roots
is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880...,
and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers,
find the total of the digital sums of
the first one hundred decimal digits for all the irrational square roots.
"""

import decimal
decimal.getcontext().prec = 110


# No es entera
suma_decimales = 0
for x in range(2, 101):
    raiz = decimal.Decimal(x).sqrt()

    if (raiz == int(raiz)):
        continue

    raiz = str(raiz)

    for i in range(101):
        if (raiz[i] != '.'):
            suma_decimales += int(raiz[i])

print(suma_decimales)