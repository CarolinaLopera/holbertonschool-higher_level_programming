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

	# numerator = sum([distribution[i]*weights[i] for i in range(len(distribution))])
    # denominator = sum(weights)
	# return round(numerator/denominator, 2)
	# weighted_sum = []
    # for salary, weight in zip(distribution, weights):
    #     weighted_sum.append(salary * weight)
    # return round(sum(weighted_sum) / sum(weights),2)
