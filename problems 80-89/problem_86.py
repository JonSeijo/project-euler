# Problem 86
# Cuboid route

import math

EXPECTED = 1000000

def norma_cuad(c1, c2):
	return c1*c1 + c2*c2

def es_cuad_perfecto(d):
	return math.sqrt(d) == round(math.sqrt(d))

# Me da la cantidad de elementos mayores a x en la lista, log n
def cant_mayores(lista, x):
	lo = -1
	hi = len(lista) 
	while lo + 1 < hi:
		m = (lo + hi) // 2
		if lista[m] < x:
			lo = m
		else:
			hi = m

	cant = len(lista) - hi
	return cant


def res(M):
	cuboides = 0
	perfectos = [ [] for _ in range(2*M+1)]

	for base in range(1, 2*M+1):
		for h in range(1, M+1):
			if es_cuad_perfecto( norma_cuad(base, h) ):
				perfectos[base].append(h)

	for a in range(1, M+1):
		for b in range(a, M+1):
			cuboides += cant_mayores(perfectos[a+b], b)

	return cuboides

# binaria en M
lo = 0
hi = 2000
while lo + 1 < hi:
	m = (lo + hi) // 2
	print("Probando M:", m)

	if res(m) < EXPECTED:
		lo = m
	else:
		hi = m

print(hi)
