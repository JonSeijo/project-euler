#Maximum path sum II
#Problem 67

"""
Similar to problem 18, but way bigger
Find the maximum total from top to bottom in triangle.txt, a 15K text file containing a triangle with one-hundred rows.
"""

"""
IDEA DEL ALGORITMO: en main()
"""

# tri will contain the 'triangle'
tri = []

# Read lines of the file and store them as a list of strings
with open("problem_67_triangle.txt") as f:
    lines = f.read().splitlines()

# Take each line and split each string when there is a space
for fila in lines:
    tri.append(fila.split())

for i in range(0, len(tri)):
    for j in range(0, len(tri[i])):
        tri[i][j] = int(tri[i][j])

# create array of partial sums
sumasParciales = []
for i in range(0, len(tri)):
    sumasParciales.append([])
    for j in range(0, len(tri[i])):
        sumasParciales[i].append(0)


altoTotal = len(tri[len(tri) - 1])

def solve():
    for v in xrange(altoTotal-1, -1, -1):  #alto
        for i in xrange(0, v):  #ancho
            valueToSum = tri[v][i]
            if (v == altoTotal-1):
                sumasParciales[v][i] = valueToSum
            else:
                sumasParciales[v][i] = valueToSum + max(sumasParciales[v+1][i], sumasParciales[v+1][i+1])

        if (v == 0):  #sum the last node
            sumasParciales[0][0] = max(sumasParciales[1][0], sumasParciales[1][1]) + tri[0][0]

"""
IDEA DEL ALGORITMO:
Le sumo a mi nodo actual el maximo de la suma acumulada por mis dos hijos

Para esto, voy guardando los  valores en una lista de sumasparciales,
comienzo desde abajo, eligiendo la maxima suma actual que ya fue precalculada en la iteracion anterior
"""
def main():
    solve()
    print sumasParciales[0][0]

if __name__ == '__main__':
    main()
