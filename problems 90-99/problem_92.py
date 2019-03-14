# Problem 92
# Square digit chains

MAXN = 10000000
DP = [-1 for x in range(MAXN)]

def cadena_89(x):
	if x == 89:
		return 1
	if x == 1:
		return 0

	if x < MAXN and DP[x] != -1:
		return DP[x]

	xdigits = x
	res = 0
	while xdigits != 0:
		res += (xdigits % 10) ** 2
		xdigits = xdigits // 10

	retval = cadena_89(res)
	if (x < MAXN):
		DP[x] = retval

	return retval

N = 10000000
veces = 0
for x in range(1, N+1):
	if x % 10000 == 0:
		print(x)
	veces += cadena_89(x)
print(veces)
