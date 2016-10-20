#Convergents of e
#Problem 65
#Jonathan Seijo
"""
e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

The first ten terms in the sequence of convergents for e are:

2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.
"""



# Creo la fraccion continua de e, usando el enunciado
e = [2, 1]
for i in range(3, 101):
    if i%3 == 0:
        e.append(2*i/3)
    else:
        e.append(1)

"""
Deducido en papel, en el caso base ya no tengo denominadores por calcular
n + 1/d = (d*n + 1) / d

en el caso recursivo, donde r es el resultado de la recursion,
r := rn / rd

n + 1/r <-> n + 1/(rn/rd) <-> n + rd/rn <-> (n*rn + rd)/rn
"""
def r(n, d, i):
    if (i == 98):
        return n*e[i] + 1, e[i]
    else:
        rn, rd = r(d, e[i+1], i+1)
        n = n*rn + rd
        d = rn
        return n, d

def sumadigitos(n):
    s = 0
    while n:
        s += n % 10
        n /= 10
    return s

def main():

    print e
    inic = e.pop(0)

    n_final, d_final = r(inic, e[0], 0)

    print n_final
    print d_final
    print "rta: " + str(sumadigitos(n_final))

if __name__ == '__main__':
    main()

