n = int(input())

matrix = []

sum_primary_diagonal = 0
sum_secondary_diagonal = 0

for row in range(n):
    matrix.append([int(el) for el in input().split()])
    sum_primary_diagonal += matrix[row][row]

for row in range(n):
    for col in range(n):
        if (row + col) == (n - 1):
            sum_secondary_diagonal += matrix[row][col]
print(abs(sum_primary_diagonal - sum_secondary_diagonal))