# Problem 87
# Prime power triples

import math

MAXIMO = 50000000
SQRT_MAXIMO = int(math.sqrt(MAXIMO))

primo = [True for _ in range(MAXIMO+1)]
primo[0] = False
primo[1] = False

# criba
print("Criba..")
for p in range(SQRT_MAXIMO):
	if primo[p]:
		m = 2*p
		while m < SQRT_MAXIMO:
			primo[m] = False
			m += p

f2 = lambda x: x*x
f3 = lambda x: x*x*x
f4 = lambda x: x*x*x*x
primos_2 = [f2(x) for x in range(SQRT_MAXIMO) if primo[x] and f2(x) < MAXIMO]
primos_3 = [f3(x) for x in range(SQRT_MAXIMO) if primo[x] and f3(x) < MAXIMO]
primos_4 = [f4(x) for x in range(SQRT_MAXIMO) if primo[x] and f4(x) < MAXIMO]

# El truco es que son <1000 numeros posibles en total, puedo hacer fuerza bruta
print("Calculando..")
count = 0
reses = []
for a in primos_2:
	for b in primos_3:
		for c in primos_4:
			if a + b + c < MAXIMO:
				count += 1
				reses.append(a+b+c)

print("Res:")
print(len(set(reses)))