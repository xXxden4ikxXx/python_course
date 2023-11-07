# str_2 содержит в себе str_1?

str_1 = 'test'
str_2 = 'test1'


def soderzhit(string, string_part):

    if string_part in string:

        print('ДА')

    else:

        print('НЕТ')


soderzhit(str_2, str_1)
