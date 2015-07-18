# Problem 15


"""
El numero de 'lattice paths' desde (0,0) hasta (a,b)
es igual al coeficiente binomico:
   (a + b)
   (  b  )

 2x2 -->   (2 + 2)     (a + b)      ( n )    =         n!
           (  2  )     (  a  )      ( k )         (n-k)! * k!

Para resolver el problema, lo unico que hago es aplicar esa formula

http://mathworld.wolfram.com/LatticePath.html
http://mathworld.wolfram.com/BinomialCoefficient.html
"""

from math import factorial


def latice(n, k):
    return factorial(n) / (factorial(n-k) * factorial(k))


def main():
    answer = latice(20+20, 20)
    print answer

if __name__ == "__main__":
    main()
