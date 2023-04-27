from array1D import Array


class Array2D:
    def __init__(self, numRows, numCols):
        self._theRows = Array(numRows)

        for i in range(numRows):
            self._theRows[i] = Array(numCols)

    def numRows(self):
        return len(self._theRows)

    def numCols(self):
        return len(self._theRows[0])

    def clear(self, value):
        for row in range(self.numRows()):
            row.clear(value)

    def __getitem__(self, ndxTuple):
        assert len(ndxTuple) == 2, 'invalid number of array subcripts'
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 & row < self.numRows(
        ) and col >= 0 and col < self.numCols(), 'Array subscript out of range'
        the1dArray = self._theRows[row]
        return the1dArray[col]

    def __setitem__(self, ndxTuple, value):
        assert len(ndxTuple) == 2, "invalid number of array subscripts"
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows(
        ) and col >= 0 and col < self.numCols(), 'Array subscript out of range.'
        the1dArray = self._theRows[row]
        the1dArray[col] = value
        
    def __repr__(self):
        return str(self._theRows)