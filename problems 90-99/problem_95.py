# Problem 95
# Amicable chains

MAXN = 1000001
# MAXN = 51
G = [0 for _ in range(MAXN)]
visited = [0 for _ in range(MAXN)]
visited[0] = 2
visited[1] = 2

def generar_divs(i, factores, acum):
	if i == len(factores):
		return [acum]

	primo = factores[i][0]
	tope = factores[i][1]

	res = []
	for j in range(tope+1):
		res += generar_divs(i+1, factores, acum * (primo**j) )
	return res


print("Criba")
# criba
facts = [ [] for _ in range(MAXN)]
for p in range(2, MAXN):
	if len(facts[p]) == 0:  # es_primo
		m = 2*p
		while m < MAXN:
			facts[m].append(p)
			m += p

# hallo divisores de cada numero
for n in range(2, MAXN):
	if n % 10000 == 0:
		print("Divisores ... ", n)

	info_factores = []
	num = n
	for p in facts[n]:
		cuenta = 0
		while num % p == 0:
			num = num // p
			cuenta += 1

		info_factores.append((p, cuenta))

	divisores = generar_divs(0, info_factores, 1)

	# quito el mismo numero de sus divisores
	value = sum(divisores) - n
	G[n] = max(0, value)
	if G[n] >= MAXN:
		G[n] = 0


def hallar_ciclo(n):
	if visited[n] == 2:
		return -1

	# halle un ciclo
	if visited[n] == 1:
		return n

	visited[n] = 1
	res = hallar_ciclo(G[n])
	visited[n] = 2

	return res

def dame_ciclo(n, tope):
	if n == tope:
		return [tope]

	# print(n, tope)
	return [n] + dame_ciclo(G[n], tope)


elciclo = []
maxc = 0
minv = 0


# TEST
# G = [0 for _ in range(MAXN)]

# G[2] = 3
# G[3] = 4
# G[4] = 5
# G[5] = 2

# G[6] = 7
# G[7] = 8
# G[8] = 9
# G[9] = 6

# Tengo un grafo dirigido G, quiero hallar el minimo elemento del ciclo mas grande
for s in range(2, MAXN):
	if visited[s]:
		continue

	if s % 10000 == 0:
		print("Calculando ciclos ... ", s)

	ciclo_start = hallar_ciclo(s)
	if ciclo_start == -1:
		continue

	ciclo = dame_ciclo(G[ciclo_start], ciclo_start)

	if len(ciclo) > maxc:
		maxc = len(ciclo)
		minv = min(ciclo)
		elciclo = ciclo
	elif len(ciclo) == maxc and min(ciclo) < minv:
		minv = min(ciclo)
		elciclo = ciclo

print("max ciclo: ", maxc)
print(elciclo)
print(minv)