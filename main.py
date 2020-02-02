import game

width = 10
height = 10
max_generations = 5
grid = game.Grid(width, height, max_generations)
# -----------------------------------------------------------------------------
# main loop
while grid.generations < max_generations:
    grid.display()
    grid.generations += 1