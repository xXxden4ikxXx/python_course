import numpy as np

mat1 = np.random.randint(10, size=(8, 4))
mat2 = np.random.randint(10, size=(4, 2))

mat = np.dot(mat1, mat2)

print(mat)
