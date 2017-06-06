# Problem 76
# Counting summations

"""
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
"""

objetivo = 15
visitado = {}

print("Formas de escribir el nro " + str(objetivo) + ": ")

def dfs(A):
    visitado[str(A)] = True

    if (len(visitado) % 10000 == 0):
        print(len(visitado))

    for i in range(len(A)):
        if A[i] == 1:
            continue

        for j in range(1, int(A[i]/2) + 1):
            V = A[:i] + [j] + [A[i] - j] + A[i+1:]
            V.sort()

            if str(V) not in visitado:
                dfs(V)

for x in range(1, objetivo//2 + 1):
    print("x: " + str(x))
    dfs([x, objetivo - x])


for k,v in visitado.items():
    print(k)

print("rta: " + str(len(visitado)))


"""
The recursive formula above is a beautiful one that generates every combination.
It works great, it is correct, it's just slow

Problem was solved using the DP formula bellow,
https://en.wikipedia.org/wiki/Partition_(number_theory)#Restricted_part_size_or_number_of_parts
(Number partitioning for reference)

def p(k, n):
    if (k == 0 and n == 0):
        return 1

    if (n <= 0 or k <= 0):
        return 0

    if (DP[k][n] != -1):
        return DP[k][n]

    DP[k][n] = p(k, n-k) + p(k-1, n-1)
    return DP[k][n]


DP = [[-1 for _ in range(101)] for _ in range(101)]
objetivo = 100
rta = 0

for x in range(1, objetivo):
    rta += p(x, objetivo)

print("rta: " + str(rta))
"""