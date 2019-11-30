from re import findall


def check_correct(my_list):
    my_sum = sum(my_list[0])
    var1 = my_sum // len(my_list[0])
    var2 = my_sum % len(my_list[0])
    if var1 == my_list[1][0] and var2 == my_list[1][1]:
        my_list.append('True')
    else:
        my_list.append('False')
    my_list = list(map(str, my_list))
    return f"{''.join(x for x in my_list[0] if (x != '[') and x != ']')}; " \
           f"{''.join(x for x in my_list[1] if (x != '[') and x != ']')}; {my_list[2]}"


data_source = 'numbers.txt'

with open(data_source, 'r') as numbers_source:
    our_lines = numbers_source.readlines()

for line in our_lines:
    numbers = list(findall(r'[\s\d]+', line))
    if len(numbers) == 2:
        mas_help = []
        for num in numbers:
            mas_help.append(list(map(int, num.split())))
        print(check_correct(mas_help))


# print(input_data)