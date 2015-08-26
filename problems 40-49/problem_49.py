# Prime permutations
# Problem 49

"""
The arithmetic sequence, 1487, 4817, 8147,
in which each of the terms increases by 3330,
is unusual in two ways: (i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of
three 1-, 2-, or 3-digit primes, exhibiting this property,
but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating
the three terms in this sequence?
"""


import math


def isPrime(number):
    # Divisible by 2, not prime
    if number % 2 == 0:
        return False

    div = 3

    # If divisible by something, not prime
    while div < int(math.sqrt(number)) + 1:
        if number % div == 0:
            return False
        # Increase by 2, we already checked even numbers
        div += 2

    return True


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

    answer = ''
    number = 1001

    while answer == '' and number < 10000:

        if isPrime(number):
            print number

            # If the number is prime, loop through an amount to increase
            for increase in range(100, 5000):

                # If next two in sequence are primes
                if isPrime(number + increase) and isPrime(number + increase*2):

                    # Check if both numbers are permutations of the first
                    if isPermutation(number, number+increase):
                        if isPermutation(number, number+increase*2):

                            # Then we found the answer
                            answer += str(number)
                            answer += str(number+increase)
                            answer += str(number+increase*2)
                            break

        # Even numbers are not prime
        number += 2

        # 1487 is the example given
        if number == 1487:
            number += 2

    print "answer: " + answer


if __name__ == "__main__":
    main()
