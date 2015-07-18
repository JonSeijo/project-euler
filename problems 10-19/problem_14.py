# Longest Collatz sequence
# Problem 14

"""
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms.
Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
"""


def collatz(n):
    if n % 2 == 0:
        return n/2
    else:
        return 3*n + 1


def main():
    """Gives an answer in 24 seconds on my machine, 
    it could probably be optimized"""

    maxNumber = 1
    maxTimes = 1

    for number in range(1, 1000000):
        n = number
        times = 1

        # Use collatz function until reaches 1
        # Count how many times it is aplied to see "lenght of chain"
        while n != 1:
            n = collatz(n)
            times += 1

        # If last number produced a longest chain, we got a winner
        if times > maxTimes:
            maxNumber = number
            maxTimes = times

    print maxNumber
    print times


if __name__ == "__main__":
    main()
