def int_check(fun):

    def wrapper(*args, **kwargs):

        result = fun(*args, **kwargs)

        if not type(result) is int:

            raise Exception("Тип данных результата не int")

        else:

            return result

    return wrapper


@int_check
def summation(a, b):

    return a + b


@int_check
def multiplication(a, b):

    return a * b


print(summation(1, 2))
print(multiplication(4, 2))
print(multiplication(1, 1 / 2))