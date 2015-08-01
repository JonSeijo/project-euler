# Digit fifth powers
# Problem 30

"""
Find the sum of all the numbers that can be written as
the sum of fifth powers of their digits.
"""


def main():
    """
    I don't know when to stop checking numbers,
    So I guessed 7 digit numbers would suffice.
    Sorry for that.
    """
    number = 11
    totalSum = 0

    while True:
        numberSum = 0
        for c in str(number):
            numberSum += int(c)**5
        if numberSum == number:
            totalSum += number
        number += 1
        if len(str(number)) == 7:
            break

    print totalSum


if __name__ == "__main__":
    main()
