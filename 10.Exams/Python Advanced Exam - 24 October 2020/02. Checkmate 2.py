def find_king(mat):
    for row_ in range(n):
        for col_ in range(n):
            if mat[row_][col_] == "K":
                return (row_, col_)


matrix = []
n = 8

for _ in range(n):
    row__ = input().split()
    matrix.append(row__)

king_row, king_col = find_king(matrix)
queens = []
is_killed = False

for col in range(king_col + 1, n):
    if matrix[king_row][col] == "Q":
        queens.append([king_row, col])
        is_killed = True
        break
for col in range(0, king_col):
    if matrix[king_row][col] == "Q":
        queens.append([king_row, col])
        is_killed = True
        break
for row in range(king_row + 1, n):
    if matrix[row][king_col] == "Q":
        queens.append([row, king_col])
        is_killed = True
        break
for row in range(0, king_row):
    if matrix[row][king_col] == "Q":
        queens.append([row, king_col])
        is_killed = True
        break

for i in range(n):
    try:
        if matrix[king_row - i][king_col - i] == "Q":
            queens.append([king_row - i, king_col - i])
    except:
        IndexError
    try:
        if matrix[king_row + i][king_col + i] == "Q":
            queens.append([king_row + i, king_col + i])
    except:
        IndexError
    try:
        if matrix[king_row - i][king_col + i] == "Q":
            queens.append([king_row - i, king_col + i])
    except:
        IndexError
    try:
        if matrix[king_row + i][king_col - i] == "Q":
            queens.append([king_row + i, king_col - i])
    except:
        IndexError

if not is_killed:
    print("The king is safe!")
else:
    for el in queens:
        print(el)
