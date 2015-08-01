# Coin sums
# Problem 31

# -*- coding: utf-8 -*-

"""
In England the currency is made up of pound, f,
and pence, p, and there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, f1 (100p) and f2 (200p).

It is possible to make f2 in the following way:

    1*f1 + 1*50p + 2*20p + 1*5p + 1*2p + 3*1p

How many different ways can f2 be made using any number of coins?
"""


def main():
    # The 200p coin only, is a vallid combination
    combinations = 1

    # 1p coin
    for a in range(0, 201, 1):
        print "a: " + str(a)

        # 2p coin
        for b in range(0, 201, 2):
            # If current combination is bigger than 200,
            # then don't bother checking greater ones
            if a + b > 200:
                break

            # 5p coin
            for c in range(0, 201, 5):
                if a + b + c > 200:
                    break

                # 10p coin
                for d in range(0, 201, 10):
                    if a + b + c + d > 200:
                        break

                    # 20p coin
                    for e in range(0, 201, 20):
                        if a + b + c + d + e > 200:
                            break

                        # 50p coin
                        for f in range(0, 201, 50):
                            if a + b + c + d + e + f > 200:
                                break

                            # 100p coin
                            for g in range(0, 201, 100):
                                if a + b + c + d + e + f + g == 200:
                                    combinations += 1
                                    break

    print "combinations: " + str(combinations)

if __name__ == "__main__":
    main()
