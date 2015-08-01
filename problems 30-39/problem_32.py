# Pandigital products
# Problem 32

"""
We shall say that an n-digit number is pandigital if
it makes use of all the digits 1 to n exactly once;
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity,
39 * 186 = 7254, containing multiplicand, multiplier,
and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so
be sure to only include it once in your sum.
"""


def repeatsDigits(number):
    digits = []
    for d in str(number):
        if d in digits:
            return True
        digits.append(d)

    return False


def main():
    pandigitals = []

    for n in range(1, 100000):
        if repeatsDigits(n):
            continue
        for m in range(n, 100000):
            if repeatsDigits(m):
                continue

            allDigits = str(n) + str(m) + str(m*n)

            if len(allDigits) > 9:
                break
            if len(allDigits) == 9:
                if '0' not in allDigits:
                    if not repeatsDigits(allDigits):
                        pandigitals.append(n*m)

    print "answer"
    print sum(set(pandigitals))

if __name__ == "__main__":
    main()
