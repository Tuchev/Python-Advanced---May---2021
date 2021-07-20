n = 8

matrix = []
for row in range(n):
    matrix.append(input().split())

position_king = None
for row in range(n):
    for col in range(n):
        if matrix[row][col] == "K":
            position_king = (row, col)

current_row, current_col = position_king
is_safe = False
for i in range(n):
    if matrix[current_row][i] == "Q":
        print([current_row, i])
        continue

    elif matrix[i][current_col] == "Q":
        print([i, current_col])
        continue
    else:
        is_safe = True
if is_safe:
    print("The king is safe!")

 # or matrix[current_row][i] == "Q" and matrix[i][current_col] == "Q" or matrix[i][current_col] == "Q"