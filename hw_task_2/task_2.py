def fun(num):

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    return list(filter(lambda x: x % num == 0, numbers))


print(fun(3))
