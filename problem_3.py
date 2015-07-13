# Problem3
# Largest prime factor
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

NUMBER = 600851475143

def getPrimeFactors(number):
    """Get a list with all prime factors of the number given"""

    # primeList will contain all prime numbers
    primeList = [2]
    primeFactors = []

    while number > 1:
        needNewPrime = True
        for n in primeList:
            if number % n == 0:
                number = number / n
                primeFactors.append(n)
                needNewPrime = False

        # Get the next prime number to
        if needNewPrime:
            primeList.append(getNextPrime(primeList))

    return primeFactors


def getNextPrime(primeList):
    nextPrimeFound = False
    lastNumber = primeList[-1]

    while(not nextPrimeFound):
        isPrime = True
        lastNumber += 1
        for p in primeList:
            if lastNumber % p == 0:
                isPrime = False
                
        if(isPrime): nextPrimeFound = True

    return lastNumber


def main():
    print getPrimeFactors(NUMBER)

if __name__ == "__main__":
    main()
