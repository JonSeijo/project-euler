# Cubic permutations
#Problem 62

"""
The cube, 41063625 (345^3), can be permuted to produce two other cubes:
56623104 (384^3) and 66430125 (405^3).
In fact, 41063625 is the smallest cube which has exactly
three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations
of its digits are cube.
"""

def isPermutation(number1, number2):
    # Not permutation if not the same size
    if len(str(number1)) != len(str(number2)):
        return False

    for c1 in str(number1):
        if cuenta(c1, str(number1)) != cuenta(c1, str(number2)):
            return False

    return True


# How many x are in xs (both strings)
def cuenta(x, xs):
    n = 0
    for s in xs:
        if x == s:
            n += 1

    return n

def main():
    validCubes = []

    #maxBound arbitrario
    maxBound = 10000
    for c in range(maxBound):
        currentCube = c
        validCubes = [c]
        i = c + 1

        while i < maxBound:
            if len(str(i**3)) > len(str(currentCube**3)):
                break
            if isPermutation(currentCube**3, i**3):
                validCubes.append(i)
            i += 1

        if len(validCubes) == 5:
            print "cubos: "
            print validCubes
            print [x**3 for x in validCubes]
            print "solucion: " + str(currentCube**3)
            break 


if __name__ == "__main__":
    main()