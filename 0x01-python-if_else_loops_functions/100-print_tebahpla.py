#!/usr/bin/python3
flag = 1
for i in range(122, 96, -1):
    aux = i
    if flag == 0:
        i -= 32
        flag = 1
    elif flag == 1:
        flag = 0

    print("{}".format(chr(i)), end="")
    i = aux
