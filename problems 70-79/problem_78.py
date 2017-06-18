# Problem 78
# Coin partitions

"""
Let p(n) represent the number of different ways in which n coins can be separated into piles.
For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.

OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O
Find the least value of n for which p(n) is divisible by one million.
"""

"""
Solucion usando la formula recursiva con numeros pentagonales
"""

def g(clock):
    if clock == len(G):
        k = 0
        if clock % 2 == 0:
            k = -1 * (clock // 2)
        else:
            k = (clock // 2) + 1

        gk = (k*(3*k - 1))//2
        G.append(gk)

    return G[clock]

n = 0
P = [1]
G = [1]

while True:
    P.append(0)
    n += 1
    clock = 1

    while True:
        gk = g(clock)
        if gk > n:
            break

        q = clock
        if clock % 2 == 1:
            q += 1

        if (q // 2) % 4 == 1 or (q // 2) % 4 == 3:
            P[n] += P[n - gk] % 1000000
        else:
            P[n] -= P[n - gk] % 1000000

        clock += 1

    if n % 5000 == 0:
        print("n: " + str(n) + "  p(n): " + str(P[n]))

    if P[n]  % 1000000 == 0 and n > 1:
        print("rta: " + str(n))
        break
