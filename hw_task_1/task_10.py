lst = [2, 4, 5, 8, 9, 13]

number = 0
while number < len(lst):
    lst[number] *= number
    number += 1

print(lst)
