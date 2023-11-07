def positive_numbers(some_list):

    count = 0

    for number in some_list:

        if number > 0:

            count += 1

    return count


print(positive_numbers([1, -1, 100, 0, -1]))
print(positive_numbers([1, 2, 3, 4, 5]))
print(positive_numbers([-1, -1, -1, -1, -1]))
