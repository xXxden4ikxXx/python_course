import numpy as np


def fun(A, S, last=False):
    X = len(A)
    B = np.random.randint(10, size = (S, X))
    C = np.dot(B, A)

    vector = list(map(lambda x: x.sum(), C))
    print(f"Длина вектора:{len(vector)}")

    if last:
        result = np.maximum(vector, 0)
    else:
        result = np.sin(vector)

    return result, B


first, mat1 = fun(np.random.randint(10, size=5), 10)
second, mat2 = fun(first, 10)
third, mat3 = fun(second, 5, last=True)

# print(first, mat1)
# print(second, mat2)

print(third / 100)
