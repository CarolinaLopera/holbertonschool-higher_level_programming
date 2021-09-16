#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    order = sorted(a_dictionary.items(), key=lambda x: x[1])
    return order[-1][-1]
