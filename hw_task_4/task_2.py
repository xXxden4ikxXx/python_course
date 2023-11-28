import numpy as np

size = 8
mat = np.array([])

for i in range(size):
    for j in range(size):
        mat = np.append(mat, int((i * (size + 1) + j) % 2 == 0))

mat = mat.reshape((size, size))

print(mat)
