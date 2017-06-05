# Problem 75
# Singular integer right triangles

"""
It turns out that 12 cm is the smallest length of wire that can be bent
to form an integer sided right angle triangle in exactly one way,
but there are many more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm,
cannot be bent to form an integer sided right angle triangle,
and other lengths allow more than one solution to be found;
for example, using 120 cm it is possible to form
exactly three different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire,
for how many values of L <= 1,500,000 can
exactly one integer sided right angle triangle be formed?
"""

import math

Lmax = 1500000
triangles = {}
ps = []

"""
https://en.wikipedia.org/wiki/Farey_sequence
https://en.wikipedia.org/wiki/Pythagorean_triple

farey_function generates a and b coprimes.
If a and b aren't both odd,
then the euclid's formula will generate a _primitive_ pythagorean triplet
From the primitive triplets, I get every posible triplet by multiplying by a natural k,
Then I count the results that were generated only once
"""
def farey_function(n):
    a, b, c, d = 0, 1, 1, n
    while (c <= n):
        k = int((n + b) / d)
        a, b, c, d = c, d, (k*c-a), (k*d-b)

        # If a and b aren't both odd,
        if (a % 2 == 1 and b % 2 == 1):
            continue

        # a < b
        # Euclid's formula: generate a _primitive_ pythagorean triplet
        x1 = b*b - a*a
        x2 = 2*a*b
        x3 = b*b + a*a

        L = x1 + x2 + x3
        if (L <= Lmax):
            ps.append(L)

farey_function(10000)

# ps has the primitive triplets, I want to get every one so multiply by k
for p in ps:
    k = 1
    while (k*p <= Lmax):
        saved_value = triangles.get(k*p, 0)
        triangles[k*p] = saved_value + 1
        k += 1

rta = 0
# answer is the amount of Ls that are made from only oone combination
for l, cant in triangles.items():
    if (cant == 1):
        rta += 1

print("rta: " + str(rta))