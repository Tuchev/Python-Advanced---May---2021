# matrix = []
#
# for i in range(3):
#     matrix.append([])
#     for j in range(1, 4):
#         matrix[i].append(j)
# print(matrix)
#
# matrix_2 = [[j for j in range(1, 4)] for i in range(3)]
# print(matrix_2)

# ################################################################

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# for row in range(len(matrix)):
#     for col in range(len(matrix[row])):
#         print(matrix[row][col], end=" ")
#     print()

# ################################################################

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in range(len(matrix)):
    for col in range(len(matrix)):
        matrix[row][col] += 1
print(matrix)