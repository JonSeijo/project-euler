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

# Used in problem 52
def isPermutation(number1, number2):
    # Not permutation if not the same size
    if len(str(number1)) != len(str(number2)):
        return False

    # Every digit in number1 must be in number2
    for c1 in str(number1):
        if c1 not in str(number2):
            return False

    # Every digit in number2 must be in number1
    for c2 in str(number2):
        if c2 not in str(number1):
            return False

    return True


def main():
    # Ejemplo cumple
    print isPermutation(345**3, 384**3) and isPermutation(345**3, 405**3)

    

if __name__ == "__main__":
    main()