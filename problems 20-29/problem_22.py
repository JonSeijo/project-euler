# Names scores
# Problem 22

"""
Using problem_22_names.txt,
a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order.
Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list
to obtain a name score.

For example, when the list is sorted into alphabetical order,
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?
"""

# problem_22_names.txt tiene los nombres en formato:
# "JONNO", "JUAN", "JOSE", "JAVIER", ...


def main():
    scores = []
    index = 0

    file = open("problem_22_names.txt", "r")
    text = file.read()
    file.close()

    text = text.replace("\"", "")
    names = text.split(",")
    names.sort()

    for name in names:
        nameScore = 0
        index += 1
        for c in name:
            # ord(char) returns the value of the ascii character.
            # ord('A') is 65, but I want the score to start in 1
            # so I substract 64 so score with 'A' is 1
            nameScore += ord(c)-64

        scores.append(nameScore * index)

    print sum(scores)

if __name__ == "__main__":
    main()
