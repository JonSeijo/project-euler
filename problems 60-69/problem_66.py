#Diophantine equation
#Problem 66

"""
x^2 - D*y^2 = 1

Find the value of D <= 1000 in minimal solutions of x for which the largest value of x is obtained.
"""



from math import *

def obtenerFraccionContinua(A, x):
    a0 = int(sqrt(x))
    d = 1
    m = 0
    a = 0

    prim = True

    if a0*a0 != x:
        while (a != 2*a0):
            m = d*a - m;
            d = (x - m * m) / d;
            a = int((a0 + m) / d);
            if not prim: 
                A.append(a)
            prim = False


def result(A, n, d, i, maximo):
    if (i >= maximo):
        return n*A[i] + 1, A[i]
    else:
        rn, rd = result(A, d, A[i+1], i+1, maximo)
        n = n*rn + rd
        d = rn
        return n, d


def main():
    maxD = 0
    maxX = 0

    for d in range(2, 1001):
        A = []
        a0 = int(sqrt(d))
        #A.append(a0)
        obtenerFraccionContinua(A, d)

        longCiclo = len(A)-1
        p=0
        print "d: " + str(d)
        if longCiclo <= 0:
            continue

        if longCiclo%2 == 0:
            p, q = result(A, A[0], A[1], 1, longCiclo-2)

            print "D: " + str(d)
            print "P: " + str(p)
        else:
            A += A[1:] +A[1:]
            p, q = result(A, A[0], A[1], 1, 2*longCiclo-1)
            print "D: " + str(d)
            print "P: " + str(p)

        if p > maxX:
            maxX = p
            maxD = d


        print d
        print A
        print " "

    print "rta: " + str(maxD)


if __name__ == '__main__':
    main()
