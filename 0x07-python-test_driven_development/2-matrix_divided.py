#!/usr/bin/python3
'''
This function divides all elements of a matrix.
matrix must be a list of lists
div must be a number
'''


def matrix_divided(matrix, div):
    '''
    div matrix to div
    '''
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = list(map(list, matrix))
    flag = False

    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[i])):
            if isinstance(new_matrix[i][j], (int, float)) is False:
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")
            new_matrix[i][j] = round(new_matrix[i][j] / div, 2)
        if flag is False:
            aux = j
            flag = True
        if aux != j:
            raise TypeError("Each row of the matrix must have the same size")

    return new_matrix
