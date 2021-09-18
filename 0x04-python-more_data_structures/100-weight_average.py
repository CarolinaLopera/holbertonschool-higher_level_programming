#!/usr/bin/python3
def weight_average(my_list=[]):
    if list is None or len(my_list) == 0:
        return 0
    mul = 0
    div = 0
    for i in my_list:
        mul += i[0] * i[1]
        div += i[1]

    return mul / div

	# numerator = sum([my_list[i[0]]*my_list[i[1]] for i in range(len(mi_list))])
	# denominator = sum(my_list[i[1]])
