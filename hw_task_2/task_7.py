def again(fun):

    def wrapper(*args, **kwargs):

        try:

            result = fun(*args, **kwargs)

        except:

            print("Попробуйте снова")

            result = fun(*args, **kwargs)

        return result

    return wrapper


@again
def input_int():

    print("Введите целое число")
    a = eval(input())

    if not type(a) is int:

        raise Exception("Вы ввели не целое число!")


@again
def question(a, b):

    print("Чему равно " + str(a) + " + " + str(b) + "?")
    c = eval(input())

    if not c == a + b:

        raise Exception("Неправильно!")


input_int()
question(1, 2)
