import game

width = 10
height = 10
max_generations = 5

grid = game.Grid(width, height, max_generations)


def generationCalculation(rows, cols):
    nextGenGrid = grid.buffer
    
    for i in range(cols):

        for j in range(rows):

            liveNeighbors = 0

            
            if(grid.buffer[i+1][j] == 1):
                liveNeighbors += 1
            if(grid.buffer[i-1][j] == 1):
                liveNeighbors += 1
            if(grid.buffer[i][j+1] == 1):
                liveNeighbors += 1
            if(grid.buffer[i][j-1] == 1):
                liveNeighbors += 1
            #diagonals
            if(grid.buffer[i+1][j+1] == 1):
                liveNeighbors += 1
            if(grid.buffer[i-1][j-1] == 1):
                liveNeighbors += 1
            if(grid.buffer[i-1][j+1] == 1):
                liveNeighbors += 1
            if(grid.buffer[i-1][j-1] == 1):
                liveNeighbors += 1


        if((grid.buffer[i][j]) == 1) and (liveNeighbors < 2):
            nextGenGrid[i][j] = 0
        
        elif((grid.buffer[i][j] == 1) and (liveNeighbors > 3)):
            nextGenGrid[i][j] = 0

        elif((grid.buffer[i][j] == 1) and (liveNeighbors == 3)):
            nextGenGrid[i][j] = 1

        else:
            nextGenGrid[i][j] = grid.buffer[i][j]

        return nextGenGrid


def main():
    
    grid = game.Grid(width, height, max_generations)
    # -----------------------------------------------------------------------------
    # main loop
    while grid.generations < max_generations:
        grid.display()
        grid.generations += 1
        grid = generationCalculation(width, height)

main()