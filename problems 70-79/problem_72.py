# Problem 72
# Counting fractions

"""
How many elements would be contained in the set of reduced proper fractions for d <= 1,000,000?
"""

""" 
Muy buen problema

Para visualizarlo listar las fracciones posibles en una cuadricula
Para cada denominador, la cantidad de fracciones irreducibles que tienen ese numerador
es exactamente phi(n),   donde phi es la funcion euler de coprimalidad

Entonces, el resultado final es la sumatoria de todos los phi(i), con i <= 1 000 000

Uso el mismo codigo que en el problema #69, solo cambia el sumador del final
"""


n = 1000001
primo = [True for i in range(n)]

def criba():
    primo[0] = False
    primo[1] = False

    for i in range(4, n, 2):
        primo[i] = False

    for p in range(3, n, 2):
        if (primo[p]):
            for i in range(p*2, n, p):
                primo[i] = False


def phi(primos, n):
    res = n
    for p in primos:
        if p*p > n:
            break
        
        if n % p == 0:
            while (n % p == 0):
                n /= p

            res -= res/p

    if (n > 1):
        res -= res/n

    return res


def main():
    criba()
    primos = [i for i in range(len(primo)) if primo[i]]

    sumatoria_phi = 0

    for i in range(2, n):
        sumatoria_phi += phi(primos, i)

    print(sumatoria_phi)


if __name__ == '__main__':
    main()