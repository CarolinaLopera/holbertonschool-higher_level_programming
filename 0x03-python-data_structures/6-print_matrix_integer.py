#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        print(' '.join(map(str, i)))

    # x = '\n'
    # .join([' '.join(['{}'.format(item) for item in row]) for row in matrix])
    # print(x)
    # for row in matrix:
    #     for val in row:
    #         print("{:d}".format(val), end=" ")
    #     print()
