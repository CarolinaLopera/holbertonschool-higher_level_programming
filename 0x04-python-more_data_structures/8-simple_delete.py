#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for i in a_dictionary:
        if i == key:
            del a_dictionary[key]
            break

    return a_dictionary

    # if key in a_dictionary:
    #     del a_dictionary[key]
