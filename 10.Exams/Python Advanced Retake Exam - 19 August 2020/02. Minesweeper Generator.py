def is_in_range(r, c, n):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False

n = int(input())
number_of_bombs = int(input())

matrix = []
for row in range(n):
    matrix.append([0] * n)

for _ in range(number_of_bombs):
    [row, col] = map(lambda x: int(x), input()[1:][:-1].split(', '))
    matrix[row][col] = '*'

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1),
    "up_right": (-1, 1),
    "down_right": (1, 1),
    "up_left": (-1, -1),
    "down_left": (1, -1)
}

for row in range(n):
    for col in range(n):
        if matrix[row][col] == "*":
            continue
        else:
            count_bombs = 0
            for direction in directions:
                next_row = row + directions[direction][0]
                next_col = col + directions[direction][1]
                if is_in_range(next_row, next_col, n):
                    if matrix[next_row][next_col] == "*":
                        count_bombs += 1
            matrix[row][col] = str(count_bombs)

for row in range(n):
    for col in range(n):
        print(matrix[row][col], end=" ")
    print()
