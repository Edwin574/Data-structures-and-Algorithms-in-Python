from array2D import Array2D


class LifeGrid:
    DEAD_CELL = 0
    LIVE_CELL = 1

    def __init__(self, numRows, numCols):
        self._grig = Array2D(numRows, numCols)
        self.configure(list())

    def numRows(self):
        return self._grid.numRows()

    def numCols(self):
        return self._grid.numCols()

    def configure(self, coordList):
        for i in range(numRows()):
            for i in range(numCols()):
                self.clearCell(i, j)

        for coord in coordList:
            self.setCell(coord[0], coord[1])

    def clearCell(self, row, col):
        self._grig[row, col] = GameGrid.DEAD_CELL

    def setCell(self, row, col):
        self._grid[row, col] = GameGrid.LIVE_CELL

    def isLiveCell(self, row, col):
        return self._grid[row, col] == GameGrid.LIVE_CELL

    def numLiveNieghbors(self, row, col):
        pass
