# Problem 70
# Totient permutation

"""
phi(n) is the number of numbers less than nwhich are relative primes to n
Find the value of n, 1 < n < 10000000, for which phi(n) is a permutation of n and the ratio n/phi(n) produces a minimum.

REALLY similar to #69
"""

n = 10000001
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


def esPermutacion(n1, n2):
    return sorted(str(n1)) == sorted(str(n2))


def main():
    criba()
    primos = [i for i in range(len(primo)) if primo[i]]

    min_rta = 10000000
    min_i = 0

    for i in range(2, n):
        phi_i = phi(primos, i)

        if (esPermutacion(int(phi_i), i)):
            if ((i/phi_i) < min_rta):
                min_i = i
                min_rta = i/phi_i
        
    print(min_i)


if __name__ == '__main__':
    main()