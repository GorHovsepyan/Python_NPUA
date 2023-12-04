import numpy as np

vector = [10,20]
matrix = [[1, 4], 
         [-5, 8]]
for i in range(1):
    for j in range(1):
        matrix[j][i] =abs(matrix[j][i] * vector[i])

mat = np.matrix(matrix)
with open('outfile.txt','wb') as f:
    for line in mat:
        np.savetxt(f, line, fmt='%.2f')