# Problem 93
# Arithmetic expressions

SUBSETS = []

def aplicar_op(a, op, b):
	if a == None or b == None or op == None:
		return None

	if op == 0:
		return a+b
	elif op == 1:
		return a-b
	elif op == 2:
		return a*b
	
	if b != 0 and a % b == 0:
		return a // b
	else:
		return None

# Aplico ops una a una 
def calc_result_1(digits, v, ops):
	result = digits[ v[0] ]
	for i in range(3):
		result = aplicar_op(result, ops[i], digits[ v[i+1] ])
		if result == None:
			return 0
	return result
# Aplico ops en dos grupos y mergeo
def calc_result_2(digits, v, ops):
	res1 = aplicar_op(digits[ v[0] ], ops[0], digits[ v[1] ])
	res2 = aplicar_op(digits[ v[2] ], ops[2], digits[ v[3] ])
	res = aplicar_op(res1, ops[1], res2)
	if res == None:
		return 0
	return res

# Aplico ops en grupo de tres a derecha
def calc_result_3(digits, v, ops):
	res1 = aplicar_op(digits[ v[1] ], ops[1], digits[ v[2] ])
	res2 = aplicar_op(res1, ops[2], digits[ v[3] ])
	res = aplicar_op(digits[ v[0] ], ops[1], res2)
	if res == None:
		return 0
	return res

def calc_result_4(digits, v, ops):
	res1 = aplicar_op(digits[ v[2] ], ops[1], digits[ v[3] ])
	res2 = aplicar_op(digits[ v[1] ], ops[2], res1)
	res = aplicar_op(digits[ v[0] ], ops[1], res2)
	if res == None:
		return 0
	return res

def calc_result_5(digits, v, ops):
	res1 = aplicar_op(digits[ v[2] ], ops[1], digits[ v[3] ])
	res2 = aplicar_op(digits[ v[1] ], ops[2], res1)
	res = aplicar_op(res2, ops[1], digits[ v[0] ])
	if res == None:
		return 0
	return res



def longest_consecutive(lista):
	if lista == None or len(lista) == 0:
		return 0

	if len(lista) == 1:
		return max(0, lista[0])


	maximo = 0
	lista.sort()
	# print(lista)
	for i in range(len(lista) - 1):
		if lista[i] <= 0:
			continue

		if lista[i] == lista[i+1] or lista[i] == lista[i+1] - 1:
			maximo = lista[i+1]
		else:
			break

	return maximo


# S es mi subset de 4 digitos para trabajar
def calc(S):
	resultados = []
	for v in PERMS_4:  # v: valor
		for o in OPERACIONES:  # o: operacion
			# Agrego las distintas combinaciones de parentesis
			resultados.append(calc_result_1(S, v, o))
			resultados.append(calc_result_2(S, v, o))
			resultados.append(calc_result_3(S, v, o))
			resultados.append(calc_result_4(S, v, o))
			resultados.append(calc_result_5(S, v, o))

	return longest_consecutive(resultados)

def aplicar(x, lista):
	return [ s + [x] for s in lista ]

def generar_permutaciones(x, perms, limite):
	if x == limite:
		return perms

	perms = [perm + [i] for perm in perms for i in range(limite) if i not in perm]
	return generar_permutaciones(x+1, perms, limite)

def generar_subsets(current, SUBSETS):
	if len(current) == 4:
		SUBSETS.append(current)
		return

	last = -1
	if len(current) > 0:
		last = current[-1]

	for x in range(last+1, 10):
		generar_subsets(current + [x], SUBSETS)

def generar_operaciones(current):
	if len(current) == 3:
		return [ current ]

	res = []
	for i in range(4):
		res += generar_operaciones(current + [i])
	return res


generar_subsets([], SUBSETS)
PERMS_4 = generar_permutaciones(0, [[]], 4)
OPERACIONES = generar_operaciones([])

maxv = 0
maxi = []

for s in SUBSETS:
	cant = calc(s)
	if cant >= maxv:
		print(cant, s)
		maxv = cant
		maxi = s


rta = ""
maxi = [str(x) for x in maxi]
for c in maxi:
	rta += c
print(rta)

