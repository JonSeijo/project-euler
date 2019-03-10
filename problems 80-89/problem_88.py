# Problem 88
# Product-sum numbers

import math

class Solver:

	def f(self, k, suma_mps=0, prod_mps=1, ultimo=1):
		if k == 0:
			if suma_mps == prod_mps and suma_mps < self.mps:
				self.mps = suma_mps
			return

		i = ultimo

		while suma_mps+i < self.mps and suma_mps+i >= prod_mps*i:
			self.f(k-1, suma_mps+i, prod_mps*i, i)
			i += 1

	def solve(self, k):
		self.k = k
		self.mps = 2*k + 1

		raiz = int(math.log(k)) + 4
		unos = max(k - raiz, 0)

		self.f(k-unos, unos, 1)

		return self.mps

solver = Solver()

rtas = []
for i in range(2, 12000+1):
	if i % 10 == 0:
		print("Solving: ", i)
	res = solver.solve(i)
	rtas.append(res)

print(sum(set(rtas)))