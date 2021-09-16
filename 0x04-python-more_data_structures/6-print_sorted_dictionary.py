#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dic = sorted(a_dictionary.items())
    for i in dic:
        print("{}: {}".format(i[0], i[1]))

# for key, value in a_dictionary.items():
# 	print('{}: {}'.format(key, value))
# for key in student_score:
#     print(key, ' : ', student_score[key])
