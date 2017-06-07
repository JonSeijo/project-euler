# Problem 77
# Prime summations

"""
It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five thousand different ways?
"""

import math

def auxEsPrimo(n):
    if (n == 0 or n == 1):
        return False

    if (n == 2):
        return True

    if (n == 3):
        return True

    for i in range(2, int(math.sqrt(n)) + 2):
        if (n % i == 0):
            return False
    return True


def listaPrima(xs):
    for x in xs:
        if not primo[x]:
            return False
    return True

def hasAOne(xs):
    for x in xs:
        if x == 1:
            return True
    return False


visitado = {}
objetivo = 1
primo = [auxEsPrimo(p) for p in range(101)]
formasPrimas = 0

"""
Uses the same generating function of problem 76,
but I added a check to see if the entire list is prime.

Optimization: if there is a 1 (not prime) in the list,
then every list generated from this list wont be prime, because "1" will always be there

Answer is given ~2 minutes
"""

def dfs(A):
    global formasPrimas
    global objetivo

    visitado[str(A)] = True

    if (hasAOne(A)):
        return

    if (listaPrima(A)):
        formasPrimas += 1

    if (formasPrimas > 5000):
        return

    for i in range(len(A)):
        if A[i] == 1:
            continue

        for j in range(1, int(A[i]/2) + 1):
            V = A[:i] + [j] + [A[i] - j] + A[i+1:]
            V.sort()

            if str(V) not in visitado:
                dfs(V)

while True:
    formasPrimas = 0
    objetivo += 1
    visitado = {}

    print("checking n: " + str(objetivo))

    for x in range(1, objetivo//2 + 1):
        dfs([x, objetivo - x])

    # for k,v in visitado.items():
    #     print(k)

    if (formasPrimas >= 5000):
        print("rta: " + str(objetivo))
        break
