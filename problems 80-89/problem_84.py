# Problem 84
# Monopoly odds

"""
Regla: if a player rolls three consecutive doubles, 
they do not advance the result of their 3rd roll. Instead they proceed directly to jail.

At the beginning of the game, the CC and CH cards are shuffled. 
When a player lands on CC or CH they take a card from the top of the respective pile and, 
after following the instructions, it is returned to the bottom of the pile. 


"""

import random

CARAS_DADO = 4
cuenta_visitas = [0 for _ in range(40)]

pos_actual = 0
ultimas_tiradas = []

tablero = ["GO", "A1", "CC1", "A2", "T1", "R1", "B1", "CH1", "B2", "B3", "JAIL",
			"C1", "U1", "C2", "C3", "R2", "D1", "CC2", "D2", "D3", "FP",
			"E1", "CH2", "E2", "E3", "R3", "F1", "F2", "U2", "F3", "G2J",
			"G1", "G2", "CC3", "G3", "R4", "CH3", "H1", "T2", "H2"]

tablero_circular = tablero + tablero

casillas = { tablero[i] : i for i in range(len(tablero)) }

# 2 Cartas de chest (de 16)
# chest = [Carta(None) for _ in range(14)]
# chest += [Carta("GO"), Carta("JAIL")]
chest = [None for _ in range(14)]
chest += ["GO", "JAIL"]
random.shuffle(chest)

# 10 Cartas de chance
chance = [None for _ in range(6)]
chance += ["GO", "JAIL", "C1", "E3", "H2", "R1", "R", "R", "U", "BACK"]
random.shuffle(chance)

def reset():
	global ultimas_tiradas
	global pos_actual
	global cuenta_visitas
	global chest
	global chance
	cuenta_visitas = [0 for _ in range(40)]
	ultimas_tiradas = []
	pos_actual = 0
	random.shuffle(chest)
	random.shuffle(chance)

def tirar_dados():
	global ultimas_tiradas
	d1 = random.randrange(1, CARAS_DADO + 1)
	d2 = random.randrange(1, CARAS_DADO + 1)
	ultimas_tiradas.append((d1, d2))
	if (len(ultimas_tiradas) > 3):
		ultimas_tiradas = ultimas_tiradas[1:]
	return d1, d2

def esDoble(par):
	return par[0] == par[1]

def ultimos_tres_dobles():
	if (len(ultimas_tiradas) < 3):
		return False
	return esDoble(ultimas_tiradas[-1]) and esDoble(ultimas_tiradas[-2]) and esDoble(ultimas_tiradas[-3])

def visitar(pos):
	global pos_actual
	pos_actual = pos
	cuenta_visitas[pos] += 1

def avanzar():
	global pos_actual
	pos_actual += sum(ultimas_tiradas[-1]) 
	pos_actual %= len(tablero)

def es_chest(pos):  # CC : Comunity Chest
	return tablero[pos][:2] == "CC"

def es_chance(pos):
	return tablero[pos][:2] == "CH"

def siguiente(casilla):
	for i in range(pos_actual, pos_actual + 40):
		if casilla == tablero_circular[i][0] and len(tablero_circular[i]) == 2:
			return i if i < 40 else i - 40
	return -1

# Modifica la pos_actual en base a la carta tomada
def accionar(cartas):
	global pos_actual

	elegida = cartas[0]
	cartas = cartas[1:] + [elegida] 	# tomo la primera, la agrego al fondo

	# ejecuto la accionar
	if elegida == "BACK":
		pos_actual -= 3
		pos_actual += 40
		pos_actual %= 40
	elif elegida in ["GO", "JAIL", "C1", "E3", "H2", "R1"]:
		pos_actual = casillas[elegida]
	elif elegida in ["R", "U"]:
		pos_actual = siguiente(elegida)


def obtener_mejores(lista):
	por_args = [ (lista[i], i) for i in range(len(lista)) ]
	coso = sorted(por_args)[::-1]
	return [coso[0], coso[1], coso[2]]

def mostrar_res(tmp_mejores):
	for m in tmp_mejores:
		v = m[1]
		if (v < 10):
			print("0" + str(v), end='')
		else:
			print(str(v), end='')
	print()

iteraciones = 0
cuenta_final = [0 for _ in range(40)]

while True:

	iteraciones += 1
	if (iteraciones % 10000 == 0):
		mejores = obtener_mejores(cuenta_visitas)
		for m in mejores:
			cuenta_final[m[1]] += 1
		reset()

		print(cuenta_final)
		tmp_mejores = obtener_mejores(cuenta_final)
		mostrar_res(tmp_mejores)

	tirar_dados()

	if (ultimos_tres_dobles()):
		visitar(casillas["JAIL"])
		continue

	avanzar()

	# si caigo en especial, tengo que ejecutar la accion
	if es_chance(pos_actual):
		accionar(chance)

	if es_chest(pos_actual):  # ojo, luego de un chance podriiiia caer en chest
		accionar(chest)

	if pos_actual == casillas["G2J"]:
		visitar(casillas["JAIL"])
	else:
		visitar(pos_actual)


