# Summation of primes
# Problem 10

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import math


def findPrimes(maxPrime):
    """Returns a list of primes until maxPrime (included)"""

    primes = [2]
    n = 1

    while n < maxPrime-1:
        # If n is even, WON'T be prime
        # So I only check odd numbers doing n+=2 (3, 5, 7, 9, ..)
        n += 2
        isPrime = True
        for prime in primes:
            # eg n=100 wont be divisible by any prime greater than 10
            if prime <= math.sqrt(n):
                if n % prime == 0:
                    isPrime = False
                    break  # If n isn't prime, don't bother with more divisions
            else:
                isPrime = True
                break

        if(isPrime):
            primes.append(n)

    return primes


def main():
    answer = 0
    primes = findPrimes(2000000)

    for p in primes:
        answer += p

    print answer


if __name__ == "__main__":
    main()
