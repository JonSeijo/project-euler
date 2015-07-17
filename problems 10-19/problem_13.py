# Large sum
# Problem 13

"""
Work out the first ten digits of the sum
of the following one-hundred 50-digit numbers.
"""

# Numbers in file "problem_13_numbers"


def main():
    result = 0
    with open("problem_13_numbers") as f:
        lines = f.read().splitlines()

    for num in lines:
        result += int(num)

    answer = str(result)[:10]
    print answer


if __name__ == "__main__":
    main()
