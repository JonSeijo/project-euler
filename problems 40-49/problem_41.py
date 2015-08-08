# Pandigital prime
# Problem 41

"""
We shall say that an n-digit number is pandigital if
it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""


import math


def isPandigital(number, maxDigits):
    """
    Reusing from problem 38
    """
    num = str(number)
    if len(num) != maxDigits:
        return False

    if '0' in num:
        return False

    for digit in range(1, maxDigits+1):
            if str(digit) not in num:
                return False

    return True


def isPrime(number):
    if number == 2 or number == 3:
        return True

    if number % 2 == 0:
        return False

    for d in range(3, int(math.sqrt(number)) + 1, 2):
        if number % d == 0:
            return False

    return True


def main():
    """
    All pandigitals of 9 digits are divisible by 3:
    1+2+3+4+5+6+7+8+9 -> 45

    All pandigitals of 8 digits are divisible by 3:
    1+2+3+4+5+6+7+8 -> 36

    So the biggest primes pandigitals should be of 7 digits
    """
    answer = 0
    number = 7654321
    # Start with thee biggest pandigital of 7 digits
    # End with the smaller pandigital of 7 digits
    while number >= 1234567:
        if isPandigital(number, 7):
            if isPrime(number):
                # I'm starting from the biggest
                # So the first I find is the answer
                answer = number
                break

        # I substract 2 each time, it cant be an even number
        number -= 2

    print "answer: " + str(answer)


if __name__ == "__main__":
    main()
