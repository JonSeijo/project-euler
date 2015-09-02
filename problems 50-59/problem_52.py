# Permuted multiples
# Problem 52

"""
It can be seen that the number, 125874, and its double, 251748,
contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x,
and 6x, contain the same digits.
"""


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
    """
    Using permutation function of problem 49
    """
    number = 0
    answer = 0
    answerFlag = False

    while answer == 0:
        number += 1
        answerFlag = True
        for x in range(2, 7):
            if not isPermutation(number, number*x):
                answerFlag = False
                break

        if answerFlag:
            answer = number

    print "answer: " + str(answer)



if __name__ == "__main__":
    main()
