# Problem 18
# Maximum path sum 1

"""
By starting at the top of the triangle below
and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle
"""

# tri will contain the 'triangle'
tri = []
sums = []

# Read lines of the file and store them as a list of strings
with open("problem_18_triangle") as f:
    lines = f.read().splitlines()

# Take each line and split each string when there is a space
for fila in lines:
    tri.append(fila.split())


def traverse(y, x, partial):
    # y and x are the CURRENT positions (index) in the tree
    partial += int(tri[y][x])

    # If the next one is out of limits, current position is the last node
    if y + 1 == len(tri):
        # print tri[y][x] + " " + str(partial)
        # No more nodes, so partial sum is the last sum
        sums.append(partial)
        return

    # Recursive magic. (y+1) goes down, (x) goes left, (x+1) goes right
    traverse(y+1, x, partial)
    traverse(y+1, x+1, partial)

def main():
    """
    Jonathan Seijo

    This was a nice problem to understad recursion and binary trees.
    Example of what it does with a small tree:

    triangle:
    10
    20 30
    40 50 60

    how it goes
    10-> 20-> 40 
    10-> 20-> 50
    10-> 30-> 50
    10-> 30-> 60

    Supose I'm in '30'
    two paths: LEFT -> 40, RIGHT -> 50
    I'm using lists, so:
    NN = [y][x]
    30 = [1][1]
    40 = [2][1]
    50 = [2][2]

    To find next in the tree, y must be one more, so I use [y+1] to go down
    To go left, notice the x is the same, so I use  [y+1][x]
    To go right, notice the x is one more, so I use [y+1][x+1]

    The problem is solved using recursion, calculating the partial sums
    and pass it by parametres to the next element.
    To find more information of how this type of algorithms works, see

    https://en.wikipedia.org/wiki/Tree_traversal
    http://www.geeksforgeeks.org/618/
    """
    # Magic. See comments in main()
    traverse(0, 0, 0)
    print max(sums)


if __name__ == "__main__":
    main()
