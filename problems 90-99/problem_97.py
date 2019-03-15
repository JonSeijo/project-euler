# Problem 97
# Large non-Mersenne prime

# 28433×2^(7830457)+1.

MOD = 10**10

def expmod(b, e):
	if e == 0:
		return 1

	val = expmod(b, e//2)
	res = val * val
	if e % 2 == 1:
		res *= b

	return res % MOD

res = 28433 * expmod(2, 7830457) + 1
res %= MOD
print(res)