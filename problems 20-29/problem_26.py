# Reciprocal cycles
# Problem 26

"""
A unit fraction contains 1 in the numerator.
The decimal representation of the unit fractions with
denominators 2 to 10 are given:

    1/2 =   0.5
    1/3 =   0.(3)
    1/4 =   0.25
    1/5 =   0.2
    1/6 =   0.1(6)
    1/7 =   0.(142857)
    1/8 =   0.125
    1/9 =   0.(1)
    1/10    =   0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest
recurring cycle in its decimal fraction part.
"""


def main():
    """
    Jonathan Seijo

    With this algoorithm I don't care about the result,
    I'm only interested in the remainders.
    It goes like solving a division by hand.

    10/7 -> remainder is 3
    next division to do is
    30/7 -> remainder is 2
    20/7 -> remainder is 6
    60/7 -> remainder is 4
    ....
    repeat until the remainder starts repeating again

    when starts repeating, it counts how many decimals are between them,
    and that is the amount of digits in the recurring cycle.
    """
    maxRecurring = 1
    maxDivisor = 1

    for d in range(2, 1000):
        decimals = []
        # Start with 1. I'm testing 1/d.
        remainder = 1
        recurringCycle = 0

        while recurringCycle == 0:
            # Always add a 0 at the end to continue the division
            remainder *= 10

            # If this remainder is in the decimals list,
            # then they eill start repeating,
            # so count how long is the recurring cycle
            if remainder in decimals:
                recurringCycle = len(decimals) - decimals.index(remainder)
            # If not on the list, add it and continue with next decimal
            else:
                decimals.append(remainder)
                remainder %= d

        # See if there is a new max
        if recurringCycle > maxRecurring:
            maxRecurring = recurringCycle
            maxDivisor = d

    print str(maxDivisor) + " " + str(maxRecurring)

if __name__ == "__main__":
    main()
