# Problem 73
# Counting fractions in a range

"""
How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d <= 12,000?
"""

def main():

    """
    Recorro todos los posibles valores de d,
    y recorro todos los valores de n en un rango acotado

    1/3 < n/d < 1/2   <--->   d/3 < n < d/2

    Guardo todos los resultados de mis divisiones en un conjunto.
    Cuando hay una fraccion que puede reducirse, 
    el resultado de la division ya se encuentra en el conjunto, lo uso para evitar duplicados

    El cardinal del conjunto es la cantidad de fracciones irreducibles
    
    Resuelve en tiempo < 10seg
    """

    en_rango = set([])
    
    for d in range(2, 12001):
        
        d_2 = d / 2.0
        d_3 = d / 3.0

        for n in range(int(d_3) + 1, int(d_2)+1):
            if (n == d_2):
                break
                
            en_rango.add(n/d)


    print(len(en_rango))


if __name__ == "__main__":
    main()