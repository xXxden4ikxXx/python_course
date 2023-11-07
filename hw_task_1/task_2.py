def longest_list(first_list, second_list):

    if first_list > second_list:

        return len(first_list)

    else:

        return len(second_list)


print(longest_list([1, 2, 3], [1, 2, 3, 4]))
print(longest_list([1, 2, 3, 4, 5], [1, 2, 3, 4]))
