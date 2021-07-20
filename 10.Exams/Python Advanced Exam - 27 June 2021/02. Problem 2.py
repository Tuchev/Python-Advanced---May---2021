n = 5

matrix = []
for row in range(n):
    matrix.append(input().split())

current_position = None
all_matrix_target = []
for row in range(n):
    for col in range(n):
        if matrix[row][col] == "A":
            current_position = (row, col)
        elif matrix[row][col] == "x":
            all_matrix_target.append((row, col))
current_row, current_col = current_position

all_targets = []

count_of_commands = int(input())
for _ in range(count_of_commands):
    data = input().split()
    if data[0] == "shoot":
        current_row, current_col = current_position
        if data[1] == "up":
            while True:
                current_row -= 1
                if 0 <= current_row < n and 0 <= current_col < n:
                    if matrix[current_row][current_col] == "x":
                        all_targets.append((current_row, current_col))
                        matrix[current_row][current_col] = "."
                        break
                else:
                    break

        elif data[1] == "down":
            while True:
                current_row += 1
                if 0 <= current_row < n and 0 <= current_col < n:
                    if matrix[current_row][current_col] == "x":
                        all_targets.append((current_row, current_col))
                        matrix[current_row][current_col] = "."
                        break
                else:
                    break

        elif data[1] == "right":
            while True:
                current_col += 1
                if 0 <= current_row < n and 0 <= current_col < n:
                    if matrix[current_row][current_col] == "x":
                        all_targets.append((current_row, current_col))
                        matrix[current_row][current_col] = "."
                        break
                else:
                    break

        elif data[1] == "left":
            while True:
                current_col -= 1
                if 0 <= current_row < n and 0 <= current_col < n:
                    if matrix[current_row][current_col] == "x":
                        all_targets.append((current_row, current_col))
                        matrix[current_row][current_col] = "."
                        break
                else:
                    break

    elif data[0] == "move":
        current_row, current_col = current_position
        if data[1] == "up":
            matrix[current_row][current_col] = "."
            current_row -= int(data[2])
            if 0 <= current_row < n and 0 <= current_col < n:
                if matrix[current_row][current_col] == ".":
                    matrix[current_row][current_col] = "A"
                    current_position = (current_row, current_col)
                else:
                    current_row += int(data[2])
                    matrix[current_row][current_col] = "A"
            else:
                current_row += int(data[2])
                matrix[current_row][current_col] = "A"

        elif data[1] == "down":
            matrix[current_row][current_col] = "."
            current_row += int(data[2])
            if 0 <= current_row < n and 0 <= current_col < n:
                if matrix[current_row][current_col] == ".":
                    matrix[current_row][current_col] = "A"
                    current_position = (current_row, current_col)
                else:
                    current_row -= int(data[2])
                    matrix[current_row][current_col] = "A"
            else:
                current_row -= int(data[2])
                matrix[current_row][current_col] = "A"

        elif data[1] == "right":
            matrix[current_row][current_col] = "."
            current_col += int(data[2])
            if 0 <= current_row < n and 0 <= current_col < n:
                if matrix[current_row][current_col] == ".":
                    matrix[current_row][current_col] = "A"
                    current_position = (current_row, current_col)
                else:
                    current_col -= int(data[2])
                    matrix[current_row][current_col] = "A"
            else:
                current_col -= int(data[2])
                matrix[current_row][current_col] = "A"

        elif data[1] == "left":
            matrix[current_row][current_col] = "."
            current_col -= int(data[2])
            if 0 <= current_row < n and 0 <= current_col < n:
                if matrix[current_row][current_col] == ".":
                    matrix[current_row][current_col] = "A"
                    current_position = (current_row, current_col)
                else:
                    current_col += int(data[2])
                    matrix[current_row][current_col] = "A"
            else:
                current_col += int(data[2])
                matrix[current_row][current_col] = "A"

rest_target = []
for row in range(n):
    for col in range(n):
        if matrix[row][col] == "x":
            rest_target.append((row, col))

if rest_target:
    result = abs(len(all_matrix_target) - len(all_targets))
    print(f"Training not completed! {result} targets left.")
else:
    print(f"Training completed! All {len(all_matrix_target)} targets hit.")
for el in all_targets:
    print(list(el))