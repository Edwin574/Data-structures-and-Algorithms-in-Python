from matrix import Matrix
matrix1=Matrix(2,2)
matrix1[0,0]=2
matrix1[0,1]=4
matrix1[1,0]=3
matrix1[1,1]=7
print(f'First Matrix:   {matrix1}')

matrix2=Matrix(2,2)
matrix2[0,0]=3
matrix2[0,1]=2
matrix2[1,0]=1
matrix2[1,1]=6
print(f'second matrix:  {matrix2}')
print(' ')

#scalar multiplication
scaledMatrix=matrix1.scaleBy(2)
print(F'Scaling first matrix by 2:  {scaledMatrix}')

#addition of matrix
addResult=matrix1+matrix2
print(f'adding 1st and 2nd matrix:  {addResult}')

#subtracting of matrix

subResult=matrix1-matrix2
print(f'subtracting 1st and 2nd:    {subResult}')

#transpose matrix
inverse=matrix1.transpose()
print(f'inverse of first matrix:    {inverse}')

#matrix Multiplication
multResult=matrix1*matrix2
print(f'product of 1st and 2nd matrix: {multResult}')