import numpy as np


def factor(number):
    potential_factors = list(range(1, number + 1))
    factors = ([])
    for num in potential_factors:
        if not number % num:
            factors.append(num)

    factors = np.array(factors)

    if len(factors) == 2:
        print('Невозможно построить матрицу с размерностью из множителей числа')
    else:
        for i in range(1, len(factors) - 1):
            mat = np.full((factors[i], factors[-(i + 1)]), 0)
            print(mat)
            print('\n')


factor(60)
