# Problem 74
# Digit factorial chains

"""
The number 145 is well known for the property that the sum of the factorial 
of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; 
it turns out that there are only three such loops that exist:

169 -> 363601 -> 1454 -> 169
871 -> 45361 -> 871
872 -> 45362 -> 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. 
For example,

69 -> 363600 -> 1454 -> 169 -> 363601 (-> 1454)
78 -> 45360 -> 871 -> 45361 (-> 871)
540 -> 145 (-> 145)

Starting with 69 produces a chain of five non-repeating terms, 
but the longest non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, 
contain exactly sixty non-repeating terms?
"""

"""
I only need to know factorials from 0 to 9, so precalculate them

For each sum of factorials, I add it to a set of results
I stop when the element was already in the set.

100percent sure it could be optimized further, execution takes <50sec
"""


factorial = [1 for i in range(10)]
for i in range(1, 10):
    factorial[i] = i * factorial[i-1]


def dame_ciclo(n):
    conj = set([])

    while(n not in conj):
        conj.add(n) 
        n = sum([factorial[int(c)] for c in str(n)])    

    return len(conj)


def main():
    contador = 0

    for i in range(2, 1000000):
        ciclo = dame_ciclo(i)
        if ciclo == 60:
            contador += 1


    print(contador)


if __name__ == "__main__":
    main()