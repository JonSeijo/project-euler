# Problem 11
# Largest product in a grid

"""
What is the greatest product of four adjacent numbers 
in the same direction (up, down, left, right, or diagonally) 
in the 20×20 grid?
"""

# Grid in file "problem_11_grid"


"""
leer cada linea y almacenar todas las strings en una linea
- quedaria    lista = ["linea1" , "linea2", "linea3" ... "linea20"]

convertir cada linea(string) en una lista de ints
- listaNum = [[1,2,3,4,5...20], [23,45,74,23,75,....,56], [36,43]  ]

de esta manera quedan los numeros en un array de 2 dimensiones (tabla)
en donde accedo a los valores como   lista[fila][columna] (VER SI ES ALREVES)

teniendo los datos de este modo, ir comparando de a 4 en todas las direcciones

up down()
    productos.apend ( lista[0][0] * lista[1][0] * lista[2][0] * lista[3][0] )
    productos.apend ( lista[0][1] * lista[1][1] * lista[2][1] * lista[3][1] )
    hasta topar con 20
    y repetir moviendo una columna hacia la derecha hasta 20

left right()
    productos.apend ( lista[0][0] * lista[0][1] * lista[0][2] * lista[0][3])   
    productos.apend ( lista[1][0] * lista[1][1] * lista[1][2] * lista[1][3])
    hasta topar con 20
    y repetir moviendo una fila hacia abajo hasta 20

diagonall downright()
    productos.apend ( lista[0][0] * lista[1][1] * lista[2][2] * lista[3][3])
    productos.apend ( lista[1][0] * lista[2][1] * lista[3][2] * lista[4][3])
    hasta topar 20
    y repetir moviendo una columna haia la derecha

diagonal downleft()
    idem a la otra diagonal


despues de toooodo el procesamiento (chequear en papel)
ver max(productos)



ALTERNATIVA: comparar y almacenar el resultado maximo en una variable

"""

def main():
    


if __name__ == "__main__":
    main()
