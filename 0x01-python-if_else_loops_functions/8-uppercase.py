#!/usr/bin/python3
def uppercase(str):
	for i in range(len(str)):
		char = chr(ord(str[i]))
		if ord(str[i]) >= 97 and ord(str[i]) <= 122:
			char = chr(ord(str[i]) - 32)

		print("{}".format(char), end="")
	print("")
