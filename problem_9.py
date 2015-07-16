# Special Pythagorean triplet
# Problem 9

"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def main():
    answer = 0

    for a in range(1, 1000):
        if answer != 0: break #Stop looping if there is an answer

        for b in range(a, 1000):
            if answer != 0: break

            for c in range(b, 1000):
                #It is faster to check the sum first
                if a+b+c == 1000:
                    if a**2 + b**2 == c**2:
                        answer = a*b*c
                        break

    print answer


if __name__ == "__main__":
    main()
