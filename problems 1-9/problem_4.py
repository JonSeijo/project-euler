# Problem 4
# Largest palindrome product

"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of
two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def isPalindrome(number):
    right = str(number)
    left = right[::-1]
    return right == left


def main():

    palindromes = []

    for num1 in range(100, 1000):
        for num2 in range(100, 1000):
            number = num1 * num2
            if isPalindrome(number):
                print str(num1) + " * " + str(num2) + " = " + str(number)
                palindromes.append(number)

    answer = max(palindromes)
    print "\n" + "Max: " + str(answer)


if __name__ == "__main__":
    main()
