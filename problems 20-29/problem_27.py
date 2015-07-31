# Quadratic primes
# Problem 27

"""
Euler discovered the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes
for the consecutive values n = 0 to 39.
However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41,
and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

The incredible formula  n^2 - 79n + 1601 was discovered,
which produces 80 primes for the consecutive values n = 0 to 79.
The product of the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:

    n^2 + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b,
for the quadratic expression that produces the maximum number of primes
for consecutive values of n, starting with n = 0.
"""


from math import sqrt


def isPrime(number):
    if number < 2:
        return False

    if number == 2:
        return True

    if number % 2 == 0:
        return False

    # Every number divisible by two is already out, so step by 2
    for n in range(3, int(sqrt(number))+1, 2):
        if number % n == 0:
            return False

    return True


def main():
    maxPrimes = 0
    productAB = 1
    # The absolute value of 'a' must be <1000. So 'a' could be negative
    for a in range(-1000, 1000):
        for b in range(-1000, 1000):
            n = 0
            primes = 0
            givesPrimes = True

            while givesPrimes:
                # Quadratic formula
                p = n*n + a*n + b
                if isPrime(p):
                    primes += 1
                else:
                    # If does not give more primes, stop loop
                    givesPrimes = False
                    if primes > maxPrimes:
                        maxPrimes = primes
                        productAB = a * b
                n += 1

    print maxPrimes
    print "a * b = " + str(productAB)


if __name__ == "__main__":
    main()
