def intersection(list_1, list_2):

    return list(filter(lambda x: x in list_1, list_2))


print(intersection([1, 2, 3, 4, 5], [9, 8, 7, 6, 5, 3]))