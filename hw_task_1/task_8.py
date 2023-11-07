def abbrev(some_string):

    if not isinstance(some_string, str):

        raise Exception('data type must be string')

    abbreviation = some_string[0]

    for i in range(len(some_string)):

        if some_string[i] == " ":

            abbreviation += some_string[i + 1]

    return abbreviation


print(abbrev("Московский Государственный Университет"))
print(abbrev(34234))
