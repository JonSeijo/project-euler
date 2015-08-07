# Double-base palindromes
# Problem 36

"""
The decimal number, 585 = 1001001001 (binary),
is palindromic in both bases.

Find the sum of all numbers, less than one million,
which are palindromic in base 10 and base 2.

(Please note that the palindromic number,
in either base, may not include leading zeros.)
"""


def isPalindrome(number):
    return str(number) == str(number)[::-1]


def getBinary(number):
    binary = ""
    while number >= 1:
        binary += str(number % 2)
        number /= 2

    return int(binary[::-1])


def main():
    answer = 0
    for number in range(1, 1000000):
        if isPalindrome(number):
            if isPalindrome(getBinary(number)):
                answer += number

    print answer


if __name__ == "__main__":
    main()
