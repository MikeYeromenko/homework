import numpy


def fizz_buzz(numbers):
  res = ''
  for i in range(1, numbers[2] + 1):
    if not(i % numbers[0]) and not(i % numbers[1]):
      res += 'FB'
    elif not(i % numbers[0]):
      res += 'F'
    elif not(i % numbers[1]):
      res += 'B'
    else:
      res +=  str(i)
    res += ' '
  return res


# This function is used to create a data list
# for fizzbuzz task

def create_list_numbers(data_file_name):
  data = str(numpy.random.randint(1,30,(20, 3)))

  data = data.replace('[', '').replace(']', '')

  with open(data_file_name, 'w') as source:
    source.write(data)

  return

#main function is below

data_file_name = 'data.txt'
create_list_numbers(data_file_name)

with open(data_file_name, 'r') as source_data:
  lines = source_data.readlines()

with open('result.txt', 'w') as source_res:
  for line in lines:
    line = list(map(int, line.split()))
    result = fizz_buzz(line)
    source_res.write(str(line) + '___' + result + '\n')


