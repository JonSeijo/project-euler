# 10001st prime
# Problem 7

"""
By listing the first six prime numbers: 
2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""


def findPrime(numOfPrimes):
    primes = [2]
    n = 1

    while len(primes) != numOfPrimes:
        # If n is even, WON'T be prime
        # So I only check odd numbers doing n+=2 (3, 5, 7, 9, ..)
        n += 2
        isPrime = True
        for prime in primes:
            if n % prime == 0:
                isPrime = False
                break  # If n isn't prime, don't bother with more divisions

        if(isPrime):
            primes.append(n)

    return primes[numOfPrimes-1]


def main():
    answer = findPrime(10001)
    print answer

if __name__ == "__main__":
    main()
