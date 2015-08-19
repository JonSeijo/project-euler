# Goldbach's other conjecture
# Problem 46

"""
It was proposed by Christian Goldbach that every odd
composite number can be written as
the sum of a prime and twice a square.

9 = 7 + 2*1^2
15 = 7 + 2*2^2
21 = 3 + 2*3^2
25 = 7 + 2*3^2
27 = 19 + 2*2^2
33 = 31 + 2*1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot
be written as the sum of a prime and twice a square?
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


def main():
    """ Solves in about 20 seconds """

    # Pregenerate a list of primes until 10000 (guess)
    primes = getPrimes(10000)
    answer = 0
    number = 7
    isComposite = False

    while answer == 0:
        # Add 2 each time because it cant be divisible by 2
        number += 2

        # Check if number is composite
        for div in primes:
            # If is divisible, is composite
            if number % div == 0:
                isComposite = True
                break
            # If divisor is greater than the sqrt, then the number is prime
            if div >= int(math.sqrt(number)) + 1:
                isComposite = False
                break

        if isComposite:
            canBeWritten = False
            # Check for each prime until is greater than number
            for prime in primes:
                if prime > number:
                    break

                # Tries with       primes[0] + 2*i^2
                # Then tries with  primes[0] + 2*(i+1)^2
                # Then tries with  primes[0] + 2*(i+2)^2
                # ... until is greater than number or canBeWritten
                for single in range(1, int(number/2)):
                    newNumber = prime + 2 * single*single
                    if newNumber > number:
                        break
                    if newNumber == number:
                        canBeWritten = True
                        break

            if not canBeWritten:
                answer = number

    print "answer: " + str(answer)



if __name__ == "__main__":
    main()
