# Factorial digit sum
# Problem 20

"""
n! means n * (n - 1) * ... * 3 * 2 * 1

For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800,
and the sum of the digits in the number 10!
is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

from math import factorial


def main():
    answer = 0
    for c in str(factorial(100)):
        answer += int(c)

    print answer

if __name__ == "__main__":
    main()
