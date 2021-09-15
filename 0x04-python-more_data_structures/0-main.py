#!/usr/bin/python3
square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# for i in range(len(matrix)):
# 	for j in range(len(matrix[i])):
# 		print(matrix[i][j])

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
