# Amicable numbers
# Problem 21

"""
Let d(n) be defined as the sum of proper divisors of n
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are
1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""


def d(number):
    divisors = []
    for n in range(1, number/2 + 1):
        if number % n == 0:
            divisors.append(n)

    return sum(divisors)


def main():
    amicables = []
    for a in range(1, 10001):
        b = d(a)
        if d(b) == a:
            if b != a:
                # B will be appended when it is its turn in the loop
                amicables.append(a)

    print sum(amicables)

if __name__ == "__main__":
    main()
