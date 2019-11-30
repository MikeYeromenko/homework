

def stage_entrance(number, stages, flats_stage):
    num_entrance = number // (flats_stage * stages + 1) + 1
    if number > flats_stage * stages:
        number = number - (num_entrance - 1) * flats_stage * stages

    num_stage = number // (flats_stage + 1) + 1
    return num_stage, num_entrance


print('Enter the flat number')
flat_number = int(input())
print('Enter the quantity of stages in the house')
quantity_stages = int(input())
print('Enter the quantity of flats on a stage')
flats_on_stage = int(input())
number_stage, number_entrance = stage_entrance(flat_number, quantity_stages, flats_on_stage)
print(f'For you to find the flat number {flat_number} you have to come to the \n'
      f'entrance number {number_entrance} and go to the {number_stage} floor')

