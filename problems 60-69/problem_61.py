# Problem 61
# Cyclical figurate numbers

"""
Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers
are all figurate (polygonal) numbers and
are generated by the following formulae:

Triangle        P3,n=n(n+1)/2       1, 3, 6, 10, 15, ...
Square      P4,n=n2         1, 4, 9, 16, 25, ...
Pentagonal      P5,n=n(3n-1)/2      1, 5, 12, 22, 35, ...
Hexagonal       P6,n=n(2n-1)        1, 6, 15, 28, 45, ...
Heptagonal      P7,n=n(5n-3)/2      1, 7, 18, 34, 55, ...
Octagonal       P8,n=n(3n-2)        1, 8, 21, 40, 65, ...

The ordered set of three 4-digit numbers:
8128, 2882, 8281, has three interesting properties.

    The set is cyclic, in that the last two digits of each number
    is the first two digits of the next number
    (including the last number with the first).

    Each polygonal type: triangle (P3,127=8128),
    square (P4,91=8281), and pentagonal (P5,44=2882),
    is represented by a different number in the set.

    This is the only set of 4-digit numbers with this property.

Find the sum of the only ordered set of six cyclic 4-digit numbers
for which each polygonal type:
triangle, square, pentagonal, hexagonal, heptagonal, and octagonal,
is represented by a different number in the set.
"""


def getNthTriangle(n):
    return n*(n+1)/2


def getNthSquare(n):
    return n*n


def getNthPentagonal(n):
    return n*(3*n-1)/2


def getNthHexagonal(n):
    return n*(2*n-1)


def getNthHeptagonal(n):
    return n*(5*n-3)/2


def getNthOctagonal(n):
    return n*(3*n-2)


def getNumberList(getFigure):
    t = 0
    n = 1
    figures = []

    while t < 10000:
        t = getFigure(n)

        if t >= 1000:
            figures.append(t)

        n += 1

    return figures


def getTwoDigitsLeft(n):
    return str(n)[0:2]


def getTwoDigitsRight(n):
    return str(n)[2:4]


def esCiclico(conjunto, pRight, p1):
    if len(conjunto) == 0:
        if pRight == getTwoDigitsLeft(p1):
            return True
        else:
            return False

    p = 0
    flag = False
    for c in conjunto:
        if pRight == getTwoDigitsLeft(c):
            p = c
            flag = True
            break

    if flag:
        pRight = getTwoDigitsRight(p)
        conjunto.remove(p)
        return esCiclico(conjunto, pRight, p1)
    else:
        return False


def algoritmoPrincipal():
    triangles = getNumberList(getNthTriangle)
    squares = getNumberList(getNthSquare)
    pentagons = getNumberList(getNthPentagonal)
    hexagons = getNumberList(getNthHexagonal)
    heptagons = getNumberList(getNthHeptagonal)
    octagons = getNumberList(getNthOctagonal)

    # Horrible, sry
    for p1 in triangles:

        print "Estoy en triangulo: " + str(p1)

        for p2 in squares:
            if p2 == p1:
                continue

            print "Estoy en cuadrado: " + str(p2)

            for p3 in pentagons:
                if p3 == p2:
                    continue

                for p4 in hexagons:
                    if p4 == p3:
                        continue

                    for p5 in heptagons:
                        if p5 == p4:
                            continue

                        for p6 in octagons:
                            if p6 == p5:
                                continue

                            conjunto = [p2, p3, p4, p5, p6]
                            pRight = getTwoDigitsRight(p1)

                            if esCiclico(conjunto, pRight, p1):
                                print conjunto
                                print "Ans: " + str(sum(conjunto))
                                return


def main():
    # Hago esto para poder usar un return en el ciclo for de mas adentro.
    # Da miedo.
    algoritmoPrincipal()


if __name__ == "__main__":
    main()