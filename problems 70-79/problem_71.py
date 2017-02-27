# Problem 71
# Ordered fractions

"""
By listing the set of reduced proper fractions for d <= 1,000,000 in ascending order of size,
find the numerator of the fraction immediately to the left of 3/7.
"""

def main():
    """
    3/7 = 0.42857142857, y como d <= 1000000
    probe si el resultado era 428571/1000000, y no lo era,
    deduzco entonces que tiene que ser mayor a esto
    
    Acotando los valores de n,
    const_minima < n/d < 3/7 
    const_minima * d < n < 3/7 * d
    
    Son pocos los valores de n a probar.
    El algoritmo NO es lineal en d, pero es cercano, habria que hacer las cuentas bien

    Resuelve en alrededor de 2 segundos
    """
    
    const_minima = 0.428571
    tres_septimos = 0.42857142857

    epsilon = 1
    cercano = [0, 0]

    for d in range(1, 1000001):

        cota_inf = const_minima * d
        cota_sup = tres_septimos * d

        for n in range(int(cota_inf), int(cota_sup)+1):

            n_d = n*1.0 / d

            if n_d > tres_septimos:
                break

            if ((tres_septimos - n_d) < epsilon):
                cercano = [n, d]
                epsilon = tres_septimos - n_d


    # La reduccion la hago a mano
    print(cercano)


if __name__ == "__main__":
    main()