from collections import deque

rows, cols = [int(el) for el in input().split()]

snake = input()
string = deque(x for x in snake)

# matrix = [[' '] * cols for _ in range(rows)]

matrix = []
for row in range(rows):
    matrix.append([" "] * cols)

for row in range(rows):
    for col in range(cols):
        char = string.popleft()
        string.append(char)
        if row % 2 == 0:
            matrix[row][col] = char
        else:
            matrix[row][-(col + 1)] = char

for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        print("".join(matrix[x][y]), end="")
    print()