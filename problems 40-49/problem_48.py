# Self powers
# Problem 48

"""
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series,
1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""


def main():
    """
    Using python feels like cheating
    """
    result = 0
    for n in range(1, 1001):
        result += n**n

    result = str(result)
    answer = result[len(result)-10::]

    print "answer: " + answer


if __name__ == "__main__":
    main()
