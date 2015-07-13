# Smallest multiple
# Problem
# https://projecteuler.net/problem=5

"""
2520 is the smallest number that can be
divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number t
hat is evenly divisible by all of the numbers from 1 to 20?
"""

"""
BRUTE FORCE
tomar n
n % 1 == 0?
n % 2 == 0?
n % 3 == 0?
..

NO --> probar n+1
SI --> answer = n 


NOTE:
No hay necesidad de probar todos los numeros del 1 al 20
divisible por 2 => divisible por 2,4,6,8,10..
divisible por 3 => divisible por 3,6,9,12,15..
divisible por 5 => divisible por 5,10,15..

===> Debe ser divisible por los primos menores a 20
"""


def main():
    greaterDivisor = 20
    answerFound = False
    number = 1

    while not answerFound:
        answerFound = True
        number += 2
        print number

        for d in range(2, greaterDivisor+1):
            if number % d != 0:
                answerFound = False

    print number

if __name__ == "__main__":
    main()
