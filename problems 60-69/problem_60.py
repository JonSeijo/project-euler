# Problem 60
# Prime pair sets

"""
The primes 3, 7, 109, and 673, are quite remarkable.
By taking any two primes and concatenating them in any order
the result will always be prime. For example, taking 7 and 109,
both 7109 and 1097 are prime. The sum of these four primes, 792,
represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any
two primes concatenate to produce another prime.
"""

import math

# Genero primos hasta el integer maxPrime
def generatePrimes(maxPrime):
    primes = [2]

    for i in range(3, maxPrime):
        for p in primes:
            if i % p == 0:
                break
            if p > math.sqrt(i):
                primes.append(i)
                break

    return primes


# Chequea si un numero es primo o no
def isPrime(n):
    for p in primes:
        if n % p == 0:
            return False
        if p > math.sqrt(n):
            return True


# Concatenar izquierda
def glueToLeft(n, m):
    return int(str(n) + str(m))

# Concatenar derecha
def glueToRight(n, m):
    return int(str(m) + str(n))

"""
# 1 000 000 tardo media hora y nada
# 200 000  da 1 resultado no correcto  [3, 37, 67, 5923, 194119]
# Baje el limite a 20 000 y consegui la respuesta [13, 5197, 5701, 6733, 8389]

# Con el limite en 10 000, sigue funcionando,
# pero era imposible de saber de antemano 
"""
#Genera lista de primos hasta el numero n
primes = generatePrimes(10000)


def recursion(candidates, last):
    for p in primes:
        if p <= last:
            continue

        flag = True

        for cand in candidates:
            if (not isPrime(glueToLeft(p, cand)) or
                    not isPrime(glueToRight(p, cand))):
                flag = False
                break

        if flag:
            candidates.append(p)
            if len(candidates) == 5:
                print candidates
                print "sum: " + str(sum(candidates))
            else:
                recursion(candidates[:-1], p)

    return


def main():
    for p in primes:
        candidates = [p]
        recursion(candidates, p)


if __name__ == "__main__":
    main()
