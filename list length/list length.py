# start of the script, main file

from re import findall


def differ_func(my_zip):
    max_differ = 0
    for line1, line2 in my_zip:
        if abs(len(line1) - len(line2)) > max_differ:
            max_differ = abs(len(line1) - len(line2))
    return max_differ


with open('list1.txt', 'r') as source1:
    my_list1 = source1.read()

with open('list2.txt', 'r') as source2:
    my_list2 = source2.read()

my_list1 = findall(r'[\S]+[.,]*\S+[^,.!?\s]', my_list1)
my_list2 = findall(r'[\S]+[.,]*\S+[^,.!?\s]', my_list2)

print(differ_func(zip(my_list1, my_list2)))