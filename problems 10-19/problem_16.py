# Power digit sum
# Problem 16

"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""


def main():
    """Very easy in python. 
    In other languages the magnitude of the number would be a big problem.
    For now, I won't bother in solving the problem in another language"""

    digitsSum = 0
    digits = str(2**1000)
    for d in digits:
        digitsSum += int(d)

    print digitsSum

if __name__ == "__main__":
    main()
