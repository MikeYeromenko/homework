# Start of the script
# This script draws a picture with any sympol, even with a line
# Example:
#             python
#       pythonpythonpython
# pythonpythonpythonpythonpython
#       pythonpythonpython
#             python
#jhgjhgjh


def print_star(number, symb):
    koef = len(symb)
    for i in range(number):
        quantity_slash = abs(number // 2 - i)
        print(f"{' ' * quantity_slash * koef}{symb * (number - quantity_slash * 2)}")
    return


int_number = 0
while int_number < 1 or int_number % 2 == 0:
    print('Enter an odd positive number, please:')
    try:
        int_number = int(input())
    except ValueError:
        print("It's not a number, please try again")
        int_number = 0

symbol = ''
print('Enter symbol to write, please /default "*":')
symbol = str(input())
if symbol == '':
    symbol = '*'

print_star(int_number, symbol)

# end
