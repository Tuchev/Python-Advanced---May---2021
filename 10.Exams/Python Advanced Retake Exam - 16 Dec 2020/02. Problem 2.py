text = input()
n = int(input())

matrix = []
for x in range(n):
    matrix.append([x for x in input()])

current_position = None
for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] == "P":
            current_position = [row, col]

r, c = current_position[0], current_position[1]
matrix[r][c] = "-"
num_commands = int(input())
for command in range(num_commands):
    cmd = input()

    if cmd == "up":
        r -= 1
        if 0 <= r < n and 0 <= c < n:
            if matrix[r][c] != "-":
                text += matrix[r][c]
                matrix[r][c] = "-"
        else:
            r += 1
            text = text[0:len(text) - 1]

    elif cmd == "down":
        r += 1
        if 0 <= r < n and 0 <= c < n:
            if matrix[r][c] != "-":
                text += matrix[r][c]
                matrix[r][c] = "-"
        else:
            r -= 1
            text = text[0:len(text) - 1]

    elif cmd == "right":
        c += 1
        if 0 <= r < n and 0 <= c < n:
            if matrix[r][c] != "-":
                text += matrix[r][c]
                matrix[r][c] = "-"
        else:
            c -= 1
            text = text[0:len(text) - 1]

    elif cmd == "left":
        c -= 1
        if 0 <= r < n and 0 <= c < n:
            if matrix[r][c] != "-":
                text += matrix[r][c]
                matrix[r][c] = "-"
        else:
            c += 1
            text = text[0:len(text) - 1]

matrix[r][c] = "P"
print(text)
for row in range(n):
    print(f"{''.join(matrix[row])}")