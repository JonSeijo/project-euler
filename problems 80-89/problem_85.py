# Problem 85
# Counting rectangles

OBJ = 2000000

def cant(f, c):
	return f*(f+1)//2 * c*(c+1)//2

def mejor_r(f):
	lo = 1
	hi = f
	while lo + 1 < hi:
		m = (lo + hi) // 2
		if (cant(f, m) < OBJ):
			lo = m
		else:
			hi = m

	return lo

area = 0
min_diff = OBJ

for f in range(1, 10000): # sqrt(obj)
	r = mejor_r(f) # binaria
	rects = cant(f, r)
	if (abs(OBJ - rects) < min_diff):
		min_diff = abs(OBJ - rects)
		area = f*r

print(area)