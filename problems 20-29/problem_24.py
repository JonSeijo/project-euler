# Lexicographic permutations
# Problem 24

"""
A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the digits
1, 2, 3 and 4. If all of the permutations are listed numerically
or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of
the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""



def main():
    a = [1, 2, 3, 4]
    k = 0
    l = 0

    print a

    for i in range(0, len(a)-1):
        if a[i] < a[i+1]:
            k = i

    for i in range(k+1, len(a)):
        if a[i] > a[k]:
            l = i

    a[k], a[l] = a[l], a[k]

    a = a[0:k+1] + a[3:k:-1]
    print a

if __name__ == "__main__":
    main()
