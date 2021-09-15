#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff_set1 = list(set(set_1).difference(set_2))
    diff_set2 = list(set(set_2).difference(set_1))
    for i in range(len(diff_set2)):
        diff_set1.append(diff_set2[i])

    return diff_set1
