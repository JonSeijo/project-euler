# Problem 81
# Path sum: two ways

"""
Find the minimal path sum, in problem_81.txt,
a 31K text file containing a 80 by 80 matrix,
from the top left to the bottom right by only moving right and down.
"""

matriz = []

with open("problem_81.txt") as fi:
    for line in fi:
        matriz.append([int(x) for x in line.split(',')])


DP = [[-1 for _ in range(80)] for _ in range(80)]
DP[0][0] = matriz[0][0]

def f(x, y):
    if (DP[x][y] != -1):
        return DP[x][y]

    elif (x == 0):
        DP[x][y] = matriz[x][y] + f(x, y-1)

    elif (y == 0):
        DP[x][y] = matriz[x][y] + f(x-1, y)

    else:
        DP[x][y] = matriz[x][y] + min(f(x-1, y), f(x, y-1))

    return DP[x][y]


print(f(79, 79))