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


def isPrime(n):
    for p in primes:
        if n % p == 0:
            return False
        if p > math.sqrt(n):
            return True


def glueToLeft(n, m):
    return int(str(n) + str(m))

def glueToRight(n, m):
    return int(str(m) + str(n))

"""
# 1 000 000 tardo media hora y nada
# 200 000  da 1 resultado no correcto  [3, 37, 67, 5923, 194119]
# Baje el limite a 20 000 y consegui la respuesta [13, 5197, 5701, 6733, 8389]

# Con el limite en 10 000, sigue funcionando,
# pero era imposible de saber de antemano 
"""
#Genero lista de primos hasta el numero n
primes = generatePrimes(10000)


def main():

    for p1 in primes:
        if p1 == 2:
            continue

        print "candidato: " + str(p1)
        candidates1 = [p1]
        for p2 in primes:
            if p2 <= p1:
                continue

            flag2 = True
            for cand in candidates1:
                if not isPrime(glueToLeft(p2, cand)):
                    flag2 = False
                    break

                if not isPrime(glueToRight(p2, cand)):
                    flag2 = False
                    break

            if flag2:
                candidates2 = [p1, p2]

                for p3 in primes:
                    if p3 <= p2:
                        continue

                    flag3 = True
                    for cand in candidates2:
                        if not isPrime(glueToLeft(p3, cand)):
                            flag3 = False
                            break

                        if not isPrime(glueToRight(p3, cand)):
                            flag3 = False
                            break

                    if flag3:
                        candidates3 = [p1, p2, p3]

                        for p4 in primes:
                            if p4 <= p3:
                                continue

                            flag4 = True
                            for cand in candidates3:
                                if not isPrime(glueToLeft(p4, cand)):
                                    flag4 = False
                                    break

                                if not isPrime(glueToRight(p4, cand)):
                                    flag4 = False
                                    break

                            if flag4:
                                #print "candidato p4: " + str(p4)
                                #print candidates3
                                candidates4 = [p1, p2, p3, p4]

                                print candidates4

                                for p5 in primes:
                                    if p5 <= p4:
                                        continue

                                    flag5 = True
                                    for cand in candidates4:
                                        if not isPrime(glueToLeft(p5, cand)):
                                            flag5 = False
                                            break

                                        if not isPrime(glueToRight(p5, cand)):
                                            flag5 = False
                                            break

                                    if flag5:
                                        candidates5 = [p1, p2, p3, p4, p5]
                                        print candidates5
                                        print "\n\n\n\n\n"
                                        print "sum:" + str(sum(candidates5))

                                        print "\n\n\n\n\n"




if __name__ == "__main__":
    main()
