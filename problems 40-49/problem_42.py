# Coded triangle numbers
# Problem 42

"""
The nth term of the sequence of triangle numbers is
given by, tn = (n(n+1))/2; so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding
to its alphabetical position and adding these values we form a word value.
For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
If the word value is a triangle number then
we shall call the word a triangle word.

Using problem_42_words.txt, a 16K text file containing
nearly two-thousand common English words, how many are triangle words?
"""


def getTriangleNumbers(maxNumber):
    triangleNumbers = []
    n = 1
    t = 0

    while t < maxNumber:
        t = (n*(n+1))/2
        triangleNumbers.append(t)
        n += 1

    return triangleNumbers


def main():
    """
    Reusing code of problem 22
    """

    triangleWordCount = 0
    # It is waaay more efficient to have a list of triangle numbers
    # than calculating them each time
    # The biggest triangle number is more than enought (is for "ZZZZZZZZZZZ")
    triangleNumbers = getTriangleNumbers(500)

    file = open("problem_42_words.txt", "r")
    text = file.read()
    file.close()

    # Create a list with the words in the format ["jonno", "seijo", ... ]
    text = text.replace("\"", "")
    words = text.split(",")

    for word in words:
        wordValue = 0

        for c in word:
            # ord(char) returns the value of the ascii character.
            # ord('A') is 65, but I want the score to start in 1
            # so I substract 64 so score with 'A' is 1
            wordValue += ord(c)-64

        if wordValue in triangleNumbers:
            triangleWordCount += 1

    print "answer: " + str(triangleWordCount)

if __name__ == "__main__":
    main()
