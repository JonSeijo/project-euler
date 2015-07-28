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
    """
    I KNOW that I can just import "itertools" and call a permutation function.
    That is NO fun at all, and I won't learn anything.
    Learning is my main motivator here.


    The idea of the algorithm was taken from here:
    https://en.wikipedia.org/wiki/Permutation
    although there are many sources.

    From wikipedia:
    "The following algorithm generates the next permutation lexicographically
    after a given permutation. It changes the given permutation in-place.

    1. Find the largest index k such that a[k] < a[k + 1].
    If no such index exists, the permutation is the last permutation.

    2 .Find the largest index l greater than k such that a[k] < a[l].
    
    3. Swap the value of a[k] with that of a[l].
    
    4. Reverse the sequence from a[k + 1] up to and including
    the final element a[n].
    """
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    pos = 1

    while True:
        k = 0
        l = 0

        last = True
        for i in range(0, len(digits)-1):
            # If this does not exist, there are no more permutations
            if digits[i] < digits[i+1]:
                k = i
                last = False

        if last:
            break

        for i in range(k+1, len(digits)):
            # Find the biggest digit larger than k
            if digits[i] > digits[k]:
                l = i

        # Swap those two digits
        digits[k], digits[l] = digits[l], digits[k]

        # Reverses the digits from k+1
        # Python magic, list[begin:end:step] returns that slice-[::-1] reverses
        digits = digits[0:k+1] + digits[len(digits)-1:k:-1]

        pos += 1
        if pos == 1000000:
            break

    print pos
    print digits

if __name__ == "__main__":
    main()
