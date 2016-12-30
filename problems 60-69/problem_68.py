"""
Problem statement:
https://projecteuler.net/problem=68


IDEA DEL ALGORITMO:
(puede optimizarse bastante mas, pero esto lo resuelve en ~10segundos)

- Para cada permutacion de [1, 2, ... , 10] armo todos los grupos (total: 10!)

- Armo los grupos
pos: 0 1 2 3 4 5 6 7 8 9
Los grupos por pos son:
0 1 3   2 3 5   4 5 7   6 7 9   8 9 1

- Reviso si todos suman lo mismo

- Si todos suman lo mismo, armo una string donde concateno los grupos

    - Veo si el largo de la string es 16

        - Lo agrego a una lista de rtas

- Final = max(lista de respuestas)
"""

import itertools

def stringify(a):
    rta = ""
    for i in range(len(a)):
        rta += str(a[i])
    return rta

def main():
    answerStrings = []
    solutionGroups = []
    vs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for p in itertools.permutations(vs):
        groups = []
        # This will create an array of arrays,
        # Each internal array is a subgroup of the form described in algorithm's idea
        for i in xrange(0, 10, 2):
            groups.append([p[j] for j in [i, (i+1)%10, (i+3)%10]])

        # Get the sum of every subgroup and check if it is equal
        sums = [sum(groups[k]) for k in range(len(groups))]
        allSumsEqual = sums.count(sums[0]) == len(sums)

        if (allSumsEqual):
            solutionGroups.append(groups)

    # Now that I have every group that is solution, I create the strings for each solutionGroup and filter the way I need
    for g in solutionGroups:
        groupsStringed = ""

        # The groups must be ordered starting clockwise starting from the lowest one
        minIndex = g.index(min(g))
        for i in [(k+minIndex)%5 for k in range(5)]:
            groupsStringed += stringify(g[i])

        # Problem asks explicitly for those of lenght 16
        if (len(groupsStringed) == 16):
            answerStrings.append(groupsStringed)

    print "ans: " + max(answerStrings)

if __name__ == '__main__':
    main()
