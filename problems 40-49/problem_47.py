# Distinct primes factors
# Problem 47

"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 * 7
15 = 3 * 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2*2 * 7 * 23
645 = 3 * 5 * 43
646 = 2 * 17 * 19.

Find the first four consecutive integers to have
four distinct prime factors. What is the first of these numbers?
"""


import math


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


def getPrimeFactors(number, primes):
    factors = []
    n = number
    while n != 1:
        # The prime factors are primes
        for div in primes:
            # If n is divisible by a prime, then its a prime factor
            # Break the loop and check n = n/div until 1
            if n % div == 0:
                n /= div
                factors.append(div)
                break
            # If I dont find divisors, then n is prime
            if div > int(math.sqrt(n)) + 1:
                factors.append(n)
                n /= n
                break

    return factors


def main():
    primes = getPrimes(10000)
    number = 20
    counter = 0
    answer = 0

    while answer == 0:
        # set() removes duplicates
        factors = set(getPrimeFactors(number, primes))

        # If there are 4 factors, start a counter
        if len(factors) == 4:
            counter += 1
            # If 4 consecutive numbers have 4 factors
            # The answer was the first one: 3 numbers before
            if counter == 4:
                answer = number - 3
                break

        # Reset counter if not 4 factors
        else:
            counter = 0

        number += 1

    print "answer: " + str(answer)


if __name__ == "__main__":
    main()
