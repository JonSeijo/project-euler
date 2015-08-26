# Consecutive prime sum
# Problem 50

"""
The prime 41, can be written as
the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes
that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand
that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million,
can be written as the sum of the most consecutive primes?
"""


import math


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


def getPrimes(maxNumber):
    # See the five millon problems before that use this function
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
    """
    Jonathan Seijo

    Sorry for the explanation
    Just ask me :)
    """

    # 5000 is a guess, although it can give correct answer with less
    primes = getPrimes(5000)

    trying = 0
    primeAmount = 0
    maxPrimeAmount = 0
    answer = 0

    # Start considering the biggest primes
    for n in range(len(primes)-1, 1, -1):
        for m in range(1, n):
            # Take primes[1 : len(primes)]
            # Then primes[2 : len(primes)]
            # ...
            # Then primes[m : len(primes)]

            # Substract one to ending
            # Take primes[1 : len(primes) - 1]
            # Take primes[2 : len(primes) - 1]

            # ...
            # until ... primes[m : len(primes) - n = n]

            # Sum every considered prime
            trying = sum(primes[m:n])

            # See how many primes were added together
            primeAmount = n - m

            if trying < 1000000:
                if isPrime(trying):
                    # If sum is less than 1000000 and is prime
                    # See if more primes were used
                    if primeAmount > maxPrimeAmount:
                        maxPrimeAmount = primeAmount
                        answer = trying

                    break
            else:
                break

    print "primeAmount: " + str(maxPrimeAmount) + "  answer: " + str(answer)


if __name__ == "__main__":
    main()
