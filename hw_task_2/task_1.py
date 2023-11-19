some_words = "Python blabla php blabla bla go bla C C blablabla C C Python"

some_stop_words = ["Python", "php", "go", "C"]


def remove_stop_words(words, stop_words):

    new_words = words

    for stop_word in stop_words:

        while stop_word in new_words:

            start_index = new_words.index(stop_word)
            end_index = (new_words.index(stop_word) + len(stop_word) + 1)

            new_words = new_words[0:start_index] + new_words[end_index:len(new_words)]

    return new_words


print(remove_stop_words(some_words, some_stop_words))
    