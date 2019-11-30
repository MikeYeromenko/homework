
def simple_set_create(last_member):
    simple_set = set(list(range(2, last_member + 1)))
    p = 2
    while True:
        help_set: Set[int] = set()
        for i in range(p ** 2, last_member + 1, 2 * p if p > 2 else 2):
            help_set.add(i)
        simple_set -= help_set
        help_list = sorted(list(simple_set))

        var = help_list.index(p)
        if len(help_list) - 1 == var:
            return simple_set
        else:
            p = help_list[var + 1]
            if p ** 2 >= help_list[len(help_list) - 1]:
                return simple_set - set([p ** 2])


def my_square(my_num):
    return my_num ** 2


number = 1
while number < 2:
    print('Enter the last element of your simple set. It must be an integer more then 1:')
    try:
        number = int(input())
    except ValueError:
        print('Please, enter a number, not a symbol')

simple_list = sorted(list(map(my_square, list(simple_set_create(number)))))
print(f'our simple set in 2d power is: {simple_list}')



