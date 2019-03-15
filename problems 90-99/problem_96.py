# Problem 96
# Su Doku

import copy

# Parsear tableros
contenidos = []
with open('problem_96.txt') as file:
	lineas = 0
	contenido_act = []
	for line in file:
		lineas += 1
		contenido_act.append(line[:-1])
		if lineas % 10 == 0:
			contenidos.append(contenido_act[1:])
			contenido_act = []

class Sudoku:
	def __init__(self, tablero):
		self.T = tablero
		self.T_solved = copy.deepcopy(tablero)

	# Debug para mostrar en pantalla
	def print(self, psolved=False):
		for i in range(9):
			for j in range(9):
				if psolved and self._valid_solved():
					print(self.T_solved[i][j], end=' ')
				else:
					print(self.T[i][j], end=' ')
			print()
		print("\n\n")

	def _valid_solved(self):
		return self.T_solved != None and len(self.T_solved) > 0

	# Primeros 3 digitos
	def rta(self):
		if not self._valid_solved():
			return -1

		return int( str(self.T_solved[0][0]) + str(self.T_solved[0][1]) + str(self.T_solved[0][2])  )

	def en_fila(self, fila, valor):
		return valor in self.T[fila]

	def en_columna(self, col, valor):
		for f in range(9):
			if self.T[f][col] == valor:
				return True
		return False

	def en_cuadro(self, fila, col, valor):
		fila_inicio = fila - fila % 3
		col_inicio = col - col % 3
		for f in range(fila_inicio, fila_inicio+3):
			for c in range(col_inicio, col_inicio+3):
				if self.T[f][c] == valor:
					return True
		return False

	def puedo_colocar(self, fila, col, valor):
		return not self.en_fila(fila, valor) and not self.en_columna(col, valor) and not self.en_cuadro(fila, col, valor)

	def solve_sudoku(self):
		self.solve(0)

	def vacio(self, fila, col):
		return self.T[fila][col] == 0

	def set(self, fila, col, v):
		self.T[fila][col] = v

	def tablero_valido(self):
		for f in range(9):
			for c in range(9):
				# Hack -----, el tablero esta completo entonces el value ya esta en cuadro
				prev = self.T[f][c]
				self.set(f, c, 0)
				puedo = self.puedo_colocar(f, c, prev)
				self.set(f, c, prev)
				# EndHack -----

				if not puedo:
					return False
		return True

	def solve(self, i):
		if i == 81:
			if self.tablero_valido():
				self.T_solved = copy.deepcopy(self.T)
			return

		fila = i // 9
		col = i % 9

		# Ocupado, nada que hacer
		if not self.vacio(fila, col):
			self.solve(i+1)
			return

		# Vacio
		for v in range(1, 10):
			if self.puedo_colocar(fila, col, v):
				self.set(fila, col, v)
				self.solve(i+1)
				self.set(fila, col, 0)

# Un contenido es un tablero
def armar_tabla(contenido):
	tabla = [ [0 for __ in range(9)]  for _ in range(9) ]
	for f in range(len(contenido)):
		for i in range(9):
			tabla[f][i] = int(contenido[f][i])
	return tabla

contenidos = [ armar_tabla(contenido) for contenido in contenidos ]

# Main
res = 0
i = 0
for contenido in contenidos:
	print("Resolviendo ... ", i)
	i += 1
	sudoku = Sudoku(contenido)
	# sudoku.print()
	sudoku.solve_sudoku()
	# sudoku.print(True)
	res += sudoku.rta()

print(res)