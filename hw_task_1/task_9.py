def factorial(number):

    fact = 1

    for numbers in range(number):

        fact = fact * (numbers + 1)

    return fact


print(factorial(1))
print(factorial(4))
print(factorial(1000))
print(factorial(0))
