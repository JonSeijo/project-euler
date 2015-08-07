# Pandigital multiples
# Problem 38

"""
Take the number 192 and multiply it by each of 1, 2, and 3:

    192 * 1 = 192
    192 * 2 = 384
    192 * 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576.
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying
by 1, 2, 3, 4, and 5, giving the pandigital, 918273645,
which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed
as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""


def isPandigital(number, maxDigits):
    num = str(number)
    if len(num) != maxDigits:
        return False

    if '0' in num:
        return False

    for digit in range(1, maxDigits+1):
        if str(digit) not in num:
            return False

    return True


def main():

    maxConcatenated = 0

    # Limit is biggest 5 digit number
    for number in range(1, 100000):
        concaten = ""
        n = 1
        while len(concaten) < 9:
            concaten += str(number * n)
            n += 1

        if isPandigital(concaten, 9):
            if concaten > maxConcatenated:
                maxConcatenated = concaten

    print "answer: " + str(maxConcatenated)


if __name__ == "__main__":
    main()
