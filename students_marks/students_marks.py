# with open('students.txt', 'r') as source:
#     students = source.readlines()
#     Students = {}


students = {'ivanov': (1, 3, 4), 'petrov': (3, 5, 4), 'sidorov': (4, 4, 5), 'kozlov': (4, 4, 5)}

# max_mark = 0.0
# worse_mark = 5.0
# best_students = ['default']
# worse_students = ['default']
# middle_mark = 0.0
#
# for key, val in midlmark.items():
#     middle_mark = round(sum(val) / len(val), 2)
#     if middle_mark == max_mark:
#         best_students.append(key)
#         break
#     if middle_mark == worse_mark:
#         worse_students.append(key)
#         break
#     if middle_mark > max_mark:
#         best_students = [key]
#         max_mark = middle_mark
#     if middle_mark < worse_mark:
#         worse_students = [key]
#         worse_mark = middle_mark
#
#
#
# print(f'The best student(s) is(are) {best_students} with middle mark: {max_mark}')
# print(f'The worse student(s) is(are) {worse_students} with middle mark: {worse_mark}')

max_val = max(students.values())
max_dict = {k: v for k, v in students.items() if v == max_val}

min_val = min(students.values())
min_dict = {k: v for k, v in students.items() if v == min_val}

print(f'The best student(s) is(are) {tuple(max_dict.keys())} with middle mark: {sum(max_val) / len(max_val)}')
print(f'The worse student(s) is(are) {tuple(min_dict.keys())} with middle mark: {sum(min_val) / len(min_val)}')