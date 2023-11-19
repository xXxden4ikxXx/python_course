def fun(*args):

    return tuple(filter(lambda x: isinstance(x, str), [*args]))


print(fun(3, 'asd', 'sdfdsf', 34))
