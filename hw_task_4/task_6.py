import numpy as np


class StringFile:

    def __init__(self, path, data=None):
        self.path = path
        self.data = data

    def read_file(self):
        self.data = np.genfromtxt(self.path, str, delimiter=',')

    def search(self, string):
        search_result = ([])
        for element in self.data.flatten():
            if string in element:
                search_result.append(element)

        if not search_result:
            print('Не найдено')
        else:
            return search_result


file = StringFile("data.csv")
file.read_file()
print(file.data)
print('\n')
print(file.search('python'))