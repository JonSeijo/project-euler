# Problem 79
# Passcode derivation

"""
A common security method used for online banking is to ask the user
for three random characters from a passcode.
For example, if the passcode was 531278,
they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, p079_keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order,
analyse the file so as to determine the shortest possible secret passcode of unknown length.
"""

"""
The idea is the following:

If we have the number ABC, then A comes before B before C.
We can represent it like this: A -> B -> C.

If we do the same thing for every number,
the result will be a directed graph where the digits are the nodes.
To find an order for the elements we do a topological sort,
but when picking a new element do it in lexicographical order.
(This was implemented using an Indegree sort)
"""

grafo = [[False for _ in range(10)] for _ in range(10)]
indegre = [0 for _ in range(10)]

with open("p079_keylog.txt") as f:
    for line in f:
        a = int(line[0])
        b = int(line[1])
        c = int(line[2])

        # No quiero duplicados
        if not grafo[a][b]:
            grafo[a][b] = True
            indegre[b] += 1

        if not grafo[b][c]:
            grafo[b][c] = True
            indegre[c] += 1

# Construyo lista de nodos con indegree 0 que no son aislados
S = [v for v in range(10) if (indegre[v] == 0 and any(grafo[v]))]
L = []

while len(S) != 0:
    S.sort() # Quiero el menor S
    v = S.pop(0)

    L.append(v)

    for wi in range(10):
        if (grafo[v][wi]):
            grafo[v][wi] = False
            indegre[wi] -= 1

            if indegre[wi] == 0:
                S.append(wi)

print(L)
