# Problem 94
# Almost equilateral triangles

import math

MAXN = 1000000000

def es_cuad_perf(x):
	raiz = round(math.sqrt(x))
	return raiz*raiz == x

def es_casi_equilatero(a, b):
	if b % 2 != 0:
		return False

	return es_cuad_perf(a**2 - (b//2)**2)

cuenta = 0
# for x in range(2, 10 + 1):
for x in range(2, MAXN//3 + 1):
	if x % 1000000 == 0:
		print("x", x)

	if es_casi_equilatero(x, x+1):
		cuenta += 3*x + 1
	if es_casi_equilatero(x, x-1):
		cuenta += 3*x - 1

print(cuenta)