#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    dic_roman = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000}
    result = 0
    flag = False
    save = []
    for i in range(len(roman_string)):
        for j in dic_roman.items():
            if flag is False and roman_string[i] == j[0]:
                result += j[1]
                save.append(j[1])
                flag = True
            elif roman_string[i] == j[0] and flag is True and save[i-1] >= j[1]:
                result += j[1]
                save.append(j[1])
            elif roman_string[i] == j[0] and flag is True and save[i-1] < j[1]:
                result += j[1]
                result = result - save[i - 1] - save[i - 1]
                save.append(j[1])
    return result

    # for key, value in dic_roman.items():
    # print(save)
