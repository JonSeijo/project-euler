#Odd period square roots
#Problem 64

"""
Exactly four continued fractions for sqrt(n), for N <= 13, have an odd period.
How many continued fractions for sqrt(n), N <= 10000, have an odd period?
"""

from math import *

def valorIgual(u, k):

    vale = True

    for i in range(0, k):
        uact = int(u[i]*10)
        ufin = int(u[k+i]*10)

       # print str(uact) + "   " + str(ufin)

        if (uact != ufin):
            vale = False
            break

    return vale

#'a' is a list of values
def hasPeriod(a, u):
    t2 = (len(a)+1)/2
    has = False
    period = 0

    if a[0:t2] == a[t2:t2*2]:
        if valorIgual(u, t2):
            has = True
            period = t2

    return has, period


def main():

    odds = 0
    N = 10000

    for i in range(2, N+1):
        if i % 100 == 0:
            print str(i)

        a0 = int(sqrt(i))
        largo = 0
        d = 1
        m = 0
        a = 0

        prim = True

        if a0*a0 != i:
            while (a != 2*a0):
                m = d*a - m;
                d = (i - m * m) / d;
                a = int((a0 + m) / d);
                largo += 1


        if largo % 2 == 1:
            odds += 1

    print "\n\nanswer: " + str(odds)



if __name__ == '__main__':
    main()

