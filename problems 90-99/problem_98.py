# Problem 98
# Anagramic squares

import math

MAXN = 2000000000

# Parse words
with open('problem_98.txt') as file:
	for linea in file:
		contenido = linea
	contenido = contenido.replace('"', '')
	palabras = contenido.split(',')

# Agrupar anagramas
anagramas = {}
for s in palabras:
	s_sorted = ''.join(sorted(s))

	if s_sorted in anagramas:
		anagramas[s_sorted].append(s)
	else:
		anagramas[s_sorted] = [s]

anagramas = { k : anagramas[k] for k in anagramas if len(anagramas[k]) > 1}

# Crear lista de cuadrados perfectos
cuadrados_perf = [ x*x for x in range(int(math.sqrt(MAXN))) if x*x < MAXN ]

# Tiene que haber una biyeccion entre digitos y letras
def obtener_asignacion(palabra, x):
	s = str(x)
	if len(palabra) != len(s):
		return None

	n = len(palabra)

	# Dos letras iguales tienen que estar en el mismo numero
	# Dos numeros iguales tienen que ir a la misma letra
	for i in range(n):
		for j in range(n):
			if palabra[i] == palabra[j] and s[i] != s[j]:
				return None
			if s[i] == s[j] and palabra[i] != palabra[j]:
				return None

	return (palabra, s)

# Retorno el numero de la transformacion
def transformar(palabra, asig):
	palabra_orig = asig[0]
	numero_str = asig[1]
	n = len(palabra)

	result = ""
	for i in range(n):
		for j in range(n):
			if palabra[j] == palabra_orig[i]:
				result += numero_str[j]
				break
	if result[0] == '0':
		return None
	return int(result)

maxv = 0

# Proceso cada conjunto de anagramas por tanda
for key in anagramas:
	palabras = anagramas[key]
	palabra = palabras[0]

	print(palabra, "...")

	# Pruebo cada posible asignacion de cuadrados, TODO: se puede optimizar, se la longitud por ej
	for x in cuadrados_perf:

		potables = []

		# Veo si la asignacion del cuadrado a la palabra es posible
		asig = obtener_asignacion(palabra, x)
		if asig == None:
			continue

		# Recorro el conjunto de palabras del anagrama actual
		for p in palabras:

			# Ya tengo una asignacion, transformo la palabra actual con la asignacion
			transf = transformar(p, asig)
			if transf == None:
				continue

			# Veo si el valor obtenido es un cuadrado perfector
			if transf in cuadrados_perf:  # TODO: busq_binaria o hashset
				potables.append(transf)

		# Tengo que haber matcheado con al menos dos del grupo de anagramas
		if len(potables) <= 1:
			continue

		# Me quedo con el maximo cuadrado de las transformaciones hechas
		maxv = max(maxv, max(potables))

print(maxv)