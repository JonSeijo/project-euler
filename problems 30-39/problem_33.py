# Digit cancelling fractions
# Problem 33

"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician
in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which
is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less
than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
"""


def badCancelDigit(num, digit):
    # They'll always be 2 digit numbers
    if str(num).count(str(digit)) == 2:
        return num/10
    if num % 10 != 0:
        return int(str(num).replace(str(digit), ""))
    else:
        return num


def main():
    finalNumerator = 1
    finalDenominator = 1

    # Both denominator andd numerator mus have 2 digits
    for denominator in range(12, 100):
        # The numerator is smaller than denominator
        # Because the fraction must be less than 1
        for numerator in range(11, denominator):
            for digit in range(1, 10):
                # See if there is the same digits in numerator and denominator
                if (str(digit) in str(numerator)) and (
                  str(digit) in str(denominator)):

                    # If there is the same digits, perform the bad cancelling
                    newNum = badCancelDigit(numerator, digit)*1.
                    newDen = badCancelDigit(denominator, digit)

                    # are original fraction and the bad cancelled one equals?
                    if (newNum / newDen) == (numerator*1. / denominator):
                        print str(numerator) + "/" + str(denominator) + " = " +str(int(newNum)) + "/" + str(newDen)
                        # I need to find the products of these fractions
                        finalNumerator *= newNum
                        finalDenominator *= newDen

    print "\nfinal: " + str(int(finalNumerator)) + "/" + str(finalDenominator)
    # This gives 8/800, wich simplified gives 1/100
    # So the final answer is 100

if __name__ == "__main__":
    main()
