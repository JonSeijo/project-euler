# Problem 6
# Sum square difference

"""
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""


def main():
    sumSquare = 0
    squareSum = 0
    answer = 0

    for n in range(101):
        sumSquare += pow(n, 2)
        squareSum += n

    squareSum = pow(squareSum, 2)

    answer = squareSum - sumSquare

    print answer

if __name__ == "__main__":
    main()

