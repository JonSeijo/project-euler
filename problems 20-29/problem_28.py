# Number spiral diagonals
# Problem 28

"""
Starting with the number 1 and moving to the right in a clockwise direction
a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
formed in the same way?
"""


def main():
    """
    Jonathan Seijo

    The logic goes by this:
    the numbers on the diagonals that need to be sumed are
    1 + 3 + 5 + 7 + 9 + 13 + 17 + 21 + 25 + 31 + 37 + 43 + 49 ....
    The numbers grow in a pattern,
    +2 +2 +2 +2 +4 +4 +4 +4 +6 +6 +6 +6 +8 +8 +8 +8 ....
    And that steps are how many numbers are in the "inside row" minus 1

    7 8 9
    6 1 2
    5 4 3

    1 + 3 + 5 + 7 +9
    (3, 5, 7 ,9) are in the row that has 3 numbers, minus 1, the step is 2

    This can be applied to n amount of rows, you can check doing bigger tables
    That "step" is consistent, always is 2 bigger every 4 numbers.

    Sorry for the bad explanation. I hope it's clearer reading the code.
    """
    rows = 1001
    step = 2
    diagonals = 1

    stepCount = 0
    n = 1

    # The step is in relationship with how many numbers are in that row
    # If the step is greater, it surpssed the desired rows
    while step <= rows:
        n += step
        diagonals += n

        # Every 4 numbers, the step grows by 2
        stepCount += 1
        if stepCount == 4:
            step += 2
            stepCount = 0

    print diagonals


if __name__ == "__main__":
    main()
