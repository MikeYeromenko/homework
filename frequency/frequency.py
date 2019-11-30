from re import findall

with open('text.txt', 'r') as source:
    my_text_read = source.read()
    my_text = my_text_read.lower()


def frequancy(line):
    return f"word '{line}' we met for {str(my_text.count(line))} time(s)"


# we choose only words from our text
list_words = findall(r'[\w]+', my_text)

my_text = list_words

list_words = list(set(list_words))
list_words.sort()

print('\n'.join(list(map(frequancy, list_words))))
