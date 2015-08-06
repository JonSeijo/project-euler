# Circular primes
# Problem 35

"""
The number, 197, is called a circular prime because all
rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100:
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

import math


def getPrimes(limit):
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    for number in range(20, limit):
        isPrime = True

        for d in primes:
            if d > int(math.sqrt(number)) + 1:
                break

            if number % d == 0:
                isPrime = False
                break

        if isPrime:
            primes.append(number)

    return primes


def getNextRotation(numberInt):
    """
    Returns a string because of the problems with the digit '0'
    If returns an int, zeroes at begginig and end dissapear,
    and I can't get next rotation with missing digits
    """
    numberStr = str(numberInt)
    return numberStr[1::] + numberStr[0]


def main():
    circularCount = 0
    primes = getPrimes(1000000)

    # check every prime number
    for number in primes:
        isCircular = True
        originalNumber = number
        n = getNextRotation(number)

        # if is 1 digit long, or is a double (for example 11), it is circular
        # I know it is prime, I'm only checking in the prime numbers list
        if int(n) == originalNumber:
            circularCount += 1
            continue

        # loop until the cycle completes
        while(int(n) != originalNumber):
            if int(n) not in primes:
                isCircular = False
                break
            n = getNextRotation(n)

        if isCircular:
            circularCount += 1
            print n

    print "circular amount: " + str(circularCount)


if __name__ == "__main__":
    main()
