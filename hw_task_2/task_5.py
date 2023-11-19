import math


def number_of_stairs(n, k):

    if n == 0:

        return 1

    n_stairs = 0

    for i in range(k + 1, n + 1):

        n_stairs += number_of_stairs(n - i, i)

    return n_stairs


print(number_of_stairs(7, 0))
