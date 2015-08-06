# Digit factorials
# Problem 34

"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to
the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""


def factorial(number):
    if number == 0:
        return 1

    result = 1
    for n in range(1, number+1):
        result *= n
    return result


def main():
    answerSum = 0

    # Upper bound was calculated by trial and error
    for number in range(10, 50000):

        factorialDigitSum = 0
        for digit in str(number):
            factorialDigitSum += factorial(int(digit))

        if factorialDigitSum == number:
            answerSum += number

    print answerSum


if __name__ == "__main__":
    main()
