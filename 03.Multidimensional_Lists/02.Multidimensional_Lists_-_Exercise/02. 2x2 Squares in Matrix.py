rows, cols = [int(el) for el in input().split()]

matrix = []
number_of_sub_square_matrix = 0

for row in range(rows):
    matrix.append([el for el in input().split()])

for row in range(0, rows - 1):
    for col in range(0, cols - 1):
        if matrix[row][col] == matrix[row][col + 1] == matrix[row + 1][col] == matrix[row + 1][col + 1]:
            number_of_sub_square_matrix += 1

print(number_of_sub_square_matrix)