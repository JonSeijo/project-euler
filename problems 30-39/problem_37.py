# Truncatable primes
# Problem 37

"""
The number 3797 has an interesting property.
Being prime itself, it is possible to continuously remove digits
from left to right, and remain prime at each stage: 3797, 797, 97, and 7.
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both
truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""


import math


def isTruncablePrime(number, primes):
    isTruncable = True
    digitAmount = len(str(number))

    for cut in range(1, digitAmount):
        if (int(str(number)[cut:digitAmount]) not in primes) or (
          int(str(number)[0:digitAmount-cut]) not in primes):

            isTruncable = False
            break

    return isTruncable


def main():
    """
    Jonathan Seijo

    I reused the code from problem 35,
    sorry for the mess!

    Here I generate a list of prime numbers,
    AS I'M GENERATING,
    I take the new prime number, truncate it (from left and right)
    and see if the truncated number is in the prime list.

    The truncated number will have less digits than the original number,
    so if it is prime, it MUST be on the prime list

    When I found 11 truncable primes, It stop
    Solves in around 18 seconds
    """

    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    truncableAmount = 0
    number = 20
    answer = 0

    while truncableAmount < 11:
        # Prime generator start
        number += 1
        isPrime = True
        for d in primes:
            if d > int(math.sqrt(number)) + 1:
                break

            if number % d == 0:
                isPrime = False
                break

        # If the number is prime, add it to the list
        # see if it is a truncable prime

        if isPrime:
            primes.append(number)

            if isTruncablePrime(number, primes):
                truncableAmount += 1
                print number
                answer += number

    print "answer: " + str(answer)


if __name__ == "__main__":
    main()
