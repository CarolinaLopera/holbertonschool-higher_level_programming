#!/usr/bin/python3
def complex_delete(a_dictionary, value):
	dic_cpy = a_dictionary.copy()
	for x, y in dic_cpy.items():
		if y == value:
			del a_dictionary[x]

	return a_dictionary
