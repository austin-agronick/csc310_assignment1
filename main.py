import game

width = 10
height = 10
max_generations = 10


def generationCalculation(grid, rows, cols):
    nextGenGrid = grid

    for i in range(cols):
        for j in range(rows):
            liveNeighbors = 0

            if (i + 1 <= cols - 1 and grid[i + 1][j] == 1):
                liveNeighbors += 1
            if (i - 1 >= 0 and grid[i - 1][j] == 1):
                liveNeighbors += 1
            if (j + 1 <= rows - 1 and grid[i][j + 1] == 1):
                liveNeighbors += 1
            if (j - 1 >= 0 and grid[i][j - 1] == 1):
                liveNeighbors += 1
            # diagonals
            if (i + 1 <= cols - 1 and j + 1 <= rows - 1 and grid[i + 1][j + 1] == 1):
                liveNeighbors += 1
            if (i - 1 >= 0 and j - 1 >= 0 and grid[i - 1][j - 1] == 1):
                liveNeighbors += 1
            if (i - 1 >= 0 and j + 1 <= rows - 1 and grid[i - 1][j + 1] == 1):
                liveNeighbors += 1
            if (i + 1 <= cols - 1 and j - 1 >= 0 and grid[i + 1][j - 1] == 1):
                liveNeighbors += 1

            if grid[i][j] == 1:
                if liveNeighbors < 2:
                    nextGenGrid[i][j] = 0
                elif liveNeighbors > 3:
                    nextGenGrid[i][j] = 0
                elif liveNeighbors == 3:
                    nextGenGrid[i][j] = 1
                else:
                    nextGenGrid[i][j] = grid[i][j]
            elif liveNeighbors == 3:
                nextGenGrid[i][j] = 1

    return nextGenGrid


def main():
    grid = game.Grid(width, height, max_generations)

    # -----------------------------------------------------------------------------
    # main loop
    while grid.generations < max_generations:
        grid.display()
        grid.generations += 1

        grid.data = generationCalculation(grid.data, width, height)


main()
