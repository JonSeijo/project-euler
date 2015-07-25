# Non-abundant sums
# Problem 23

"""
A perfect number is a number for which the sum of its proper divisors
is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be
1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors
is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum
of two abundant numbers is 24.

By mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis
even though it is known that the greatest number that cannot be expressed as
the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot
be written as the sum of two abundant numbers.
"""

import math


def getProperDivisors(number):
    """Returns a list with all divisors of the number except itself"""
    divisors = [1]
    for n in range(2, int(math.sqrt(number)+1)):
        if number % n == 0:
            divisors.append(n)
            # In case its a perfect square, I dont want repeated values
            if number/n != n:
                divisors.append(number/n)

    return divisors


def getAbundantNumbers(maxNumber):
    abundantNumbers = []
    for n in range(1, maxNumber):
        if sum(getProperDivisors(n)) > n:
            abundantNumbers.append(n)

    return abundantNumbers


def main():
    """
    IT TAKES SEVERAL MINUTES TO GIVE THE ANSWER.
    At least 90 percent of the time is spent when
    searching for n not in abundantNumbersSum
    """
    abundantNumbers = getAbundantNumbers(28123)

    abundantNumbersSum = []
    print "finding sums"
    for i in abundantNumbers:
        for j in abundantNumbers:
            abundantNumbersSum.append(i+j)

    answer = 0

    print "searching not in abundant numbers"

    for n in range(1, 28123):
        if n not in abundantNumbersSum:
            answer += n

    print answer

if __name__ == "__main__":
    main()
