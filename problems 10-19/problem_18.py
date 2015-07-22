# Problem 18
# Maximum path sum 1

"""
By starting at the top of the triangle below
and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle
"""


"""
Idea:
index de si mismo y el siguiente en la proxima linea
son los dos adyacentes
"""

def main():
    triangleStr = []
    triangleInt = []

    with open("problem_18_triangle") as f:
        lines = f.read().splitlines()

    for fila in lines:
        triangleStr.append(fila.split())

    for i in range(len(triangleStr)):
        triangleInt.append([] for x in range(i))

    for y in range(len(triangleStr)):
        for x in range(len(triangleStr[y])):
            currentNumber = int(triangleStr[y][x])
            print currentNumber







if __name__ == "__main__":
    main()
