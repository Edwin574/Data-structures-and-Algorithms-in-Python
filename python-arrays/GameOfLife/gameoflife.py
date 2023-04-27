from life import LifeGrid

INIT_CONFIG = [(1, 1), (1, 2), (2, 2), (3, 2)]

GRID_WIDTH = 5
GRID_HEIGHT = 5

NUM_GENS=8

def main():
    grid=LifeGrid(GRID_WIDTH, GRID_HEIGHT)
    grid.configure(INIT_CONFIG)

    draw(grid)
    for i in range(NUM_GENS):
        evolve(grid)
        draw(grid)
def evolve(grid):
    livecells=list()

    for i in range (grid.numRows()):
        for j in range(grid.numCols()):

            neighbors=grid.numLiveNieghbors(i, j)
        if (neighbors==2 and grid.isLiveCell(i, j)) or (neighbors==3):
            livecells.append((i,j))
    grid.configure(livecells)
def draw(grid):
    pass

main()