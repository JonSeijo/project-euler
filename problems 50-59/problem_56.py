#Powerful digit sum
#Problem 56

"""
A googol (10^100) is a massive number:
one followed by one-hundred zeros; 100^100 is almost unimaginably large:
one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b,
where a, b < 100, what is the maximum digital sum?
"""


def main():
    maxSum = 0
    for a in range(1, 100):
        for b in range(1, 100):
            biggie = a**b
            currentSum = 0
            for c in str(biggie):
                currentSum += int(c)

            if currentSum > maxSum:
                maxSum = currentSum

    print "answer: " + str(maxSum)







if __name__ == "__main__":
    main()
