# 1000-digit Fibonacci number
# Problem 25

"""
Starting with
F1 = 1
F2 = 1
What is the index of the first term in the Fibonacci
sequence to contain 1000 digits?
"""


def main():
    fibOne = 1
    fibTwo = 1
    index = 2

    # When number contains 1000 digits, its over
    while len(str(fibTwo)) < 1000:
        # Last item will now be the 'next-to-last',
        # and the new last item, will now be the sum of the previous
        fibOne, fibTwo = fibTwo, fibOne + fibTwo
        index += 1

    print index

if __name__ == "__main__":
    main()
