# Problem 87
# Prime power triples

import math

# MAXIMO = 50
MAXIMO = 50000000

primo = [True for _ in range(MAXIMO+1)]
primo[0] = False
primo[1] = False

# criba
print("Criba..")
for p in range(MAXIMO):
	if primo[p]:
		m = 2*p
		while m < MAXIMO:
			primo[m] = False
			m += p

f2 = lambda x: x*x
f3 = lambda x: x*x*x
f4 = lambda x: x*x*x*x
primos_2 = [f2(x) for x in range(MAXIMO) if primo[x] and f2(x) < MAXIMO]
primos_3 = [f3(x) for x in range(MAXIMO) if primo[x] and f3(x) < MAXIMO]
primos_4 = [f4(x) for x in range(MAXIMO) if primo[x] and f4(x) < MAXIMO]


# El truco es que son <500 numeros posibles, puedo hacer fuerza bruta
print("Calculando..")
count = 0
reses = []
for a in primos_2:
	for b in primos_3:
		for c in primos_4:
			if a + b + c < MAXIMO:
				count += 1
				reses.append(a+b+c)

print(count)
print(len(set(reses)))