# 10001st prime
# Problem 7

"""
By listing the first six prime numbers: 
2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

"""
plan 
busqueda de primos como en problema 3?

primes = [2]
while(primes.size != 10001):
    
    tomo n,
    lo divido por la lista de primos
    si nunca fue divisible,
    es primo, lo agrego a la lista de primos
    tomo n+1
    ...
    hasta que la lista de primos tenga 100001 elementos

"""

def getPrimeList(index):

    return primes


def findPrime(index):
    primes = [2]
    n = 1

    while len(primes) != index:
        # If n is even, WON'T be prime
        # So I only check odd numbers doing n+=2 (3, 5, 7, 9, ..)
        # This way I only check half thee numbers
        n += 2
        isPrime = True
        for prime in primes:
            if n % prime == 0:
                isPrime = False
                break

        if(isPrime):
            primes.append(n)

    return primes[index-1]


def main():
    answer = findPrime(10001)
    print answer

if __name__ == "__main__":
    main()
