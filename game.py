import os
import sys
import time
import random

# grid class to store cells
class Grid:
    def __init__(self, width, height, max_generations):
        self.buffer = build_grid(width, height)
        self.width = width
        self.height = height
        self.max_generations = max_generations
        self.generations = 0

    def getBuffer(self):
        return self.buffer

    def setBuffer(self, grid):
        self.buffer = grid

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getGenerations(self):
        return self.generations

    def setGenerations(self):
        self.generations += 1


    def set_cell(self, x, y, state):
        pass

    def display(self):
        # clear the screen, display the contents of a grid, wait for 1sec
        os.system('clear') # outputs 'TERM environment variable not set.' error if executed in python console

        if self.height == 0:
            raise ValueError("Grid contains no data")

        for i in range(self.height):
            for j in range(self.width):
                print(self.buffer[i][j], end=' ')
            print()

        time.sleep(1)

def getNum():
    return random.randint(0,1)

def build_grid(width, height):
    grid = []

    for row in range(height):
        grid.append([])
        for column in range(width):
            grid[row].append(random.randint(0,1))
    
    return grid