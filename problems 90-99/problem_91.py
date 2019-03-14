# Problem 91
# Right triangles with integer coordinates

cuenta = 0
N = 50

p0 = (0, 0)
pares = [(x,y) for x in range(0, N+1) for y in range(0, N+1)]

def ortog(ra, rb):
	return (ra[0] * rb[0] + ra[1] * rb[1]) == 0

def forma_t_rect(p1, p2):
	r0 = (p1[0]-p2[0], p1[1]-p2[1])
	r1 = p1
	r2 = p2
	return ortog(r0, r1) or ortog(r0, r2) or ortog(r1, r2)

t_rects = 0
for i in range(1, len(pares)): 
	for j in range(i+1, len(pares)):
		t_rects += forma_t_rect(pares[i], pares[j])
print(t_rects)


