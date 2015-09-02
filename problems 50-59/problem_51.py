# Prime digit replacements
# Problem 51

"""
By replacing the 1st digit of the 2-digit number *3,
it turns out that six of the nine possible values:
13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the
same digit, this 5-digit number is the first example
having seven primes among the ten generated numbers,
yielding the family: 56003, 56113, 56333, 56443, 56663,
56773, and 56993. Consequently 56003, being the first
member of this family, is the smallest prime with this
property.

Find the smallest prime which, by replacing part of the
number (not necessarily adjacent digits) with the same
digit, is part of an eight prime value family.
"""


import math


def getPrimes(maxNumber):
    primes = [2]
    number = 3
    while number < maxNumber:
        for div in primes:
            if div >= int(math.sqrt(number)) + 1:
                isPrime = True
                break
            if number % div == 0:
                isPrime = False
                break

        if isPrime:
            primes.append(number)
        number += 2

    return primes


def isPrime(number):
    # Divisible by 2, not prime
    if number % 2 == 0:
        return False

    div = 3

    # If divisible by something, not prime
    while div < int(math.sqrt(number)) + 1:
        if number % div == 0:
            return False
        # Increase by 2, we already checked even numbers
        div += 2

    return True


def getBinaryPermutations(digits):
    binaryPermutations = []
    currentBinary = '0' * digits

    n = 1
    while currentBinary != '1'*digits:
        currentBinary = "{0:b}".format(n)

        currentBinary = '0'*(digits - len(currentBinary)) + currentBinary
        binaryPermutations.append(currentBinary)

        n += 1

    return binaryPermutations

def main():
    # primes = getPrimes(100000)

    print getBinaryPermutations(4)



if __name__ == "__main__":
    main()