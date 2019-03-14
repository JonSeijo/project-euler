# Problem 90
# Cube digit pairs

CUADRADOS = ["01", "04", "09", "16", "25", "36", "49", "64", "81"]
SUBSETS = []
validas = 0

def esta(x, dx):
	if x == 6 or x == 9:
		return (6 in dx) or (9 in dx)
	return x in dx

def puedo_formar(v, da, db):
	a = int(v[0])
	b = int(v[1])
	return esta(a, da) and esta(b, db)

def es_valida(d0, d1):
	for valor in CUADRADOS:
		if not puedo_formar(valor, d0, d1) and not puedo_formar(valor, d1, d0):
			return False

	return True

def generar(current, SUBSETS):
	if len(current) == 6:
		SUBSETS.append(current)
		return

	last = -1
	if len(current) > 0:
		last = current[-1]

	for x in range(last+1, 10):
		generar(current + [x], SUBSETS)

generar([], SUBSETS)

for d0 in SUBSETS:
	for d1 in SUBSETS:
		validas += es_valida(d0, d1)

print(validas // 2)  # Porque estoy contanto el mismo par dos veces