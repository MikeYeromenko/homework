socks = {'Russia': (21, 22, 23, 24, 25, 26, 27), 'Europe': (0, 1, 2, 3, 4, 5, 6), 'USA and UK': (8, 8.5, 9, 9.5, 10, 10.5, 11)}
new_dict = dict()
i = 1
for key, value in socks.items():
    print(f'for {key} press {i}')
    new_dict[i] = key
    i += 1


# print(new_dict)

chosen_country = int(input())

my_key = new_dict[chosen_country]
print(f'for {my_key} there are sizes {socks[my_key]}. Please, select one of them:')

my_size = float(input())

my_index = socks[my_key].index(my_size)

i = f'The equivalents of {my_size} are: ' \
    f'{list(str(key + ": " + str(socks[key][my_index])) for key, value in socks.items() if key != my_key)}'

print(i.replace('[', '').replace(']', '').replace("'",""))

