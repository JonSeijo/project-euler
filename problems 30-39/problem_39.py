# Integer right triangles
# Problem 39

"""
If p is the perimeter of a right angle triangle with integral
length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
"""


def main():
    """
    THIS NEEDS HEAVY OPTIMIZATION
    IT TAKES ALMOST 500 SECONDS TO SOLVE
    """
    maxSolutions = 0
    maxP = 0
    for p in range(10, 1001):
        print p

        solutions = 0

        # the hyponetunuse must not be too big or too small, arbitrary numbers
        for hyp in range(p/4, p/2):
            solutionFound = False
            # The sides can NOT be bigger than the hypotenuse
            for side1 in range(10, hyp):
                if solutionFound:
                    break

                for side2 in range(10, hyp):
                    if side1 + side2 + hyp == p:
                        # it MUST satisfy pythagoren theorem
                        if hyp**2 == side1**2 + side2**2:
                            solutions += 1
                            solutionFound = True
                            break

        if solutions > maxSolutions:
            maxSolutions = solutions
            maxP = p

    print "p: " + str(maxP) + "     solutions: " + str(maxSolutions)


if __name__ == "__main__":
    main()
