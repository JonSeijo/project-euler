# Problem 11
# Largest product in a grid

"""
What is the greatest product of four adjacent numbers 
in the same direction (up, down, left, right, or diagonally) 
in the 20x20 grid?
"""

# Grid in file "problem_11_grid"


def storeValues(grid):
    """Stores values in a two dimensional list that holds the grid"""

    gridStr = []

    with open("problem_11_grid") as f:
        lines = f.read().splitlines()

    for fila in lines:
        gridStr.append(fila.split())

    # Create a grid with ints
    for y in range(20):
        for x in range(20):
            grid[y][x] = int(gridStr[y][x])


def main():
    # grid[Y][X]
    grid = [[0 for x in range(20)] for x in range(20)]
    storeValues(grid)

    products = []

    # Analiza todos en vertical
    for x in range(20):
        for y in range(17): #no incluye 17, 18, 19, 20
            products.append(grid[y][x] * grid[y+1][x] * 
                grid[y+2][x] * grid[y+3][x])

    # Analiza todos en horizontal
    for y in range(20):
        for x in range(17): #no incluye 17, 18, 19, 20
            products.append(grid[y][x] * 
                grid[y][x+1] * grid[y][x+2] * grid[y][x+3])

    # Analiza todos en diagonal rightdown
    for y in range(17):
        for x in range(17): #no incluye 17, 18, 19, 20
            products.append(grid[y][x] * 
                grid[y+1][x+1] * grid[y+2][x+2] * grid[y+3][x+3])

    # Analiza todos en diagonal leftdown
    for y in range(17):
        for x in range(17): #no incluye 17, 18, 19, 20
            products.append(grid[y][x+3] * 
                grid[y+1][x+2] * grid[y+2][x+1] * grid[y+3][x])

    answer = max(products)
    print answer

if __name__ == "__main__":
    main()
