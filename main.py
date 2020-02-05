
from game import Grid

width = 10
height = 10
max_generations = 5


def generationCalculation(rows, cols, grid):
    nextGenGrid = grid.getBuffer()
    
    for i in range(rows):

        for j in range(cols):
            liveNeighbors = 0

            #edges
            if(i == 0 and j == 0):
                if(grid.buffer[i+1][j] == 1):
                    liveNeighbors += 1
                if(grid.buffer[i][j+1] == 1):
                    liveNeighbors += 1 
                if(grid.buffer[i+1][j+1] == 1):
                    liveNeighbors += 1
            elif(i == 0 and j == cols-1):
                if(grid.buffer[i+1][j] == 1):
                    liveNeighbors += 1
                if(grid.buffer[i][j-1] == 1):
                    liveNeighbors += 1 
                if(grid.buffer[i+1][j-1] == 1):
                    liveNeighbors += 1
            elif(i == rows-1 and j == 0):
                if(grid.buffer[i-1][j] == 1):
                    liveNeighbors += 1
                if(grid.buffer[i-1][j+1] == 1):
                    liveNeighbors += 1
                if(grid.buffer[i][j+1] == 1):
                    liveNeighbors += 1
            elif(i == rows-1 and j == cols-1):
                if(grid.buffer[i-1][j] == 1):
                    liveNeighbors += 1
                if(grid.buffer[i-1][j-1] == 1):
                    liveNeighbors += 1
                if(grid.buffer[i][j-1] == 1):
                    liveNeighbors += 1
            elif(i == 0 and j != 0 and j != cols-1):
                break
            elif(i == rows-1 and j != 0 and j != cols-1):
                break
            elif(j == 0 and i != 0 and i != rows-1):
                break
            elif(j == cols-1 and i != 0 and i != rows-1):
                break
                
            #8 neighbors
            elif(i != 0 and j != 0 and i != rows-1 and j != cols-1):
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

        #check number of neighbors            
        if(grid.buffer[i][j] == 1 and liveNeighbors < 2):
            nextGenGrid[i][j] = 0
        
        elif(grid.buffer[i][j] == 1 and liveNeighbors > 3):
            nextGenGrid[i][j] = 0

        elif(grid.buffer[i][j] == 0 and liveNeighbors == 3):
            nextGenGrid[i][j] = 1

        else:
            nextGenGrid[i][j] = grid.buffer[i][j]

    return nextGenGrid


def main():
    
    grid = Grid(width, height, max_generations)
    # -----------------------------------------------------------------------------
    # main loop
    while grid.getGenerations() < max_generations:
        grid.display()
        grid.setGenerations()
        grid = generationCalculation(width, height, grid)

main()