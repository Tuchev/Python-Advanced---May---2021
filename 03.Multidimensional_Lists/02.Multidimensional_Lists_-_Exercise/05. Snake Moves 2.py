from collections import deque


def create_matrix(row, col):
    m = [[' '] * col for _ in range(row)]
    return m


def printing(mat):
    for x in range(len(mat)):
        for y in range(len(mat[x])):
            print(''.join(mat[x][y]), end='')
        print()


rows, columns = map(int, input().split())
matrix = create_matrix(rows, columns)
snake = input()
string = deque(x for x in snake)

for r in range(rows):
    for c in range(columns):
        char = string.popleft()
        string.append(char)
        if r % 2 == 0:
            matrix[r][c] = char
        else:
            matrix[r][-(c + 1)] = char

printing(matrix)