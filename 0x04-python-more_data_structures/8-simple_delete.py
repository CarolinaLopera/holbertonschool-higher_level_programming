#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    flag = False
    for i in a_dictionary:
        if i == key:
            flag = True
    if flag == True:
        a_dictionary.pop(key)

    return a_dictionary

    # if a_dictionarykey:
    #     del a_dictionary[key]
