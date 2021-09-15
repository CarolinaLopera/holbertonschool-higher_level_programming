#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = list(map(list, matrix))

    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[i])):
            new_matrix[i][j] = new_matrix[i][j] ** 2

    return new_matrix

# [row[i] for row in matrix]
# new_matrix = list(map(lambda x: x, matrix))
# [list(map(lambda x: x * x, row)) for row in matrix]
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         new_matrix.insert([i][j], matrix[i][j])
