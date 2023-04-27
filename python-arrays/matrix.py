from array2D import Array2D


class Matrix:
    def __init__(self, numRows, numCols):
        self._theGrid = Array2D(numRows, numCols)
        # self._theGrid.clear(0)

    def numRows(self):
        return self._theGrid.numRows()

    def numCols(self):
        return self._theGrid.numCols()

    def __getitem__(self, ndxTuple):
        return self._theGrid[ndxTuple[0], ndxTuple[1]]

    def __setitem__(self, ndxTuple, scalar):
        self._theGrid[ndxTuple[0], ndxTuple[1]] = scalar

    def __repr__(self):
        return str(self._theGrid)

    def scaleBy(self, scalar): #scalar multiplication
        newMatrix=Matrix(self.numRows(),self.numCols())
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                newMatrix[r,c]=self[r, c]* scalar
        return newMatrix

    def transpose(self): #inverse matrix
        inverseMatrix=Matrix(self.numRows(),self.numCols())
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                inverseMatrix[r,c]=self[c,r]
        return inverseMatrix

    def __add__(self, rhsMatrix): #matrix addition
        assert rhsMatrix.numRows() == self.numRows(
        ) and rhsMatrix.numCols() == self.numCols()
        "Matrix sizes not compatible for the add operations."
        newMatrix = Matrix(self.numRows(), self.numCols())
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                newMatrix[r, c] = self[r, c]+rhsMatrix[r, c]
        return newMatrix

    def __sub__(self, rhsMatrix): #matrix subtraction
        assert rhsMatrix.numRows()==self.numRows() and rhsMatrix.numCols()==self.numCols()
        'The Matrix sizes are not equal for subtraction'
        resultMatrix=Matrix(self.numRows(),self.numCols())
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                resultMatrix[r,c]=self[r,c]-rhsMatrix[r,c]
        return resultMatrix

    def __mul__(self, rhsMatrix):#product of matrices
        assert rhsMatrix.numRows() == self.numRows() and rhsMatrix.numCols() == self.numCols()
        'The Matrix sizes are not equal for subtraction'
        resultMatrix=Matrix(self.numRows(),rhsMatrix.numCols())
        for r in range(self.numRows()):
            for c in range(rhsMatrix.numCols()):
                product=0
                for k in range(self.numRows()):
                    product += self[r,k]*rhsMatrix[k,c]
                    resultMatrix[r,c]=product
        return resultMatrix
