#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = list(set(my_list))
    result = 0
    for i in unique:
        result += i
    return result

	# return (sum(set(my_list)))
