# Champernowne's constant
# Problem 40

"""
An irrational decimal fraction is created by concatenating
the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part,
find the value of the following expression.

d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000
"""


def main():
    concaten = ""
    number = 0

    # Create a string with all the numbers
    # Stop when I wont need more positions (+1000000)
    while len(concaten) <= 1000000:
        concaten += str(number)
        number += 1

    answer = 1
    digit = 1
    # The digits I need goes: 1, 10, 100, 1000, 10000 ...
    # It is multiplied by ten every time
    # I get that digit position (a single number) from the string
    while digit <= 1000000:
        answer *= int(concaten[digit])
        digit *= 10

    print "answer: " + str(answer)


if __name__ == "__main__":
    main()
