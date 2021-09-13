#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for val in row:
            print("{:d}".format(val), end=" ")
        print()

    # x = '\n'
    # .join([' '.join(['{}'.format(item) for item in row]) for row in matrix])
    # print(x)
    # for i in range(len(matrix)):
    #     for j in range(len(matrix)):
    #         print("{}".format(matrix[i][j]), end=" ")
    #     print("")
