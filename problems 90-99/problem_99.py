# Problem 99
# Largest exponential

import math

nros = []

with open('problem_99.txt') as file:
	nlinea = 0
	for linea in file:
		nlinea += 1

		s = linea[:-1].split(',')
		base = int(s[0])
		exp = int(s[1])

		nros.append( ( exp * math.log(base) , nlinea) )

nros.sort()
nros = nros[::-1]

print(nros[0][1])