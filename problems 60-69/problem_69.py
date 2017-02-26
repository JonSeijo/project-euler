# Problem 69
# Totient maximum

"""
phi(n) is the number of numbers less than nwhich are relative primes to n

Find the value of n <= 1,000,000 for which n/phi(n) is a maximum."""


n = 1000001
primo = [True for i in range(n)]

def criba():
    print("entro a criba")
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

    max_rta = 1
    max_i = 0

    for i in range(2, n):
        phi_i = phi(primos, i)

        if ((i/phi_i) > max_rta):
            max_i = i
            max_rta = i/phi_i
        
    print(max_i)


if __name__ == '__main__':
    main()