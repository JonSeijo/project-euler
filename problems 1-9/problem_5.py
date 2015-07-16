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
