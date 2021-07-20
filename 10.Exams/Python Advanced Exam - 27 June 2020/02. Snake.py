def is_in_range(r, c, num):
    if 0 <= r < num and 0 <= c < num:
        return True
    return False


n = int(input())

matrix = []
for row in range(n):
    matrix.append([el for el in input()])

snake_current_position = None

for row in range(n):
    for col in range(n):
        if matrix[row][col] == "S":
            snake_current_position = (row, col)

current_row = snake_current_position[0]
current_col = snake_current_position[1]
matrix[current_row][current_col] = "."

total_food = 0
is_Game_Finish = False

command = input()
while True:
    if command == "up":
        current_row -= 1
        if is_in_range(current_row, current_col, n):
            if matrix[current_row][current_col] == "*":
                total_food += 1
                matrix[current_row][current_col] = "."
            elif matrix[current_row][current_col] == "-":
                matrix[current_row][current_col] = "."
            elif matrix[current_row][current_col] == "B":
                matrix[current_row][current_col] = "."
                for row in range(n):
                    for col in range(n):
                        if matrix[row][col] == "B":
                            current_row = row
                            current_col = col
                            matrix[current_row][current_col] = "."
                            break
        else:
            is_Game_Finish = True
            break
    elif command == "down":
        current_row += 1
        if is_in_range(current_row, current_col, n):
            if matrix[current_row][current_col] == "*":
                total_food += 1
                matrix[current_row][current_col] = "."
            elif matrix[current_row][current_col] == "-":
                matrix[current_row][current_col] = "."
            elif matrix[current_row][current_col] == "B":
                matrix[current_row][current_col] = "."
                for row in range(n):
                    for col in range(n):
                        if matrix[row][col] == "B":
                            current_row = row
                            current_col = col
                            matrix[current_row][current_col] = "."
                            break
        else:
            is_Game_Finish = True
            break
    elif command == "right":
        current_col += 1
        if is_in_range(current_row, current_col, n):
            if matrix[current_row][current_col] == "*":
                total_food += 1
                matrix[current_row][current_col] = "."
            elif matrix[current_row][current_col] == "-":
                matrix[current_row][current_col] = "."
            elif matrix[current_row][current_col] == "B":
                matrix[current_row][current_col] = "."
                for row in range(n):
                    for col in range(n):
                        if matrix[row][col] == "B":
                            current_row = row
                            current_col = col
                            matrix[current_row][current_col] = "."
                            break
        else:
            is_Game_Finish = True
            break
    elif command == "left":
        current_col -= 1
        if is_in_range(current_row, current_col, n):
            if matrix[current_row][current_col] == "*":
                total_food += 1
                matrix[current_row][current_col] = "."
            elif matrix[current_row][current_col] == "-":
                matrix[current_row][current_col] = "."
            elif matrix[current_row][current_col] == "B":
                matrix[current_row][current_col] = "."
                for row in range(n):
                    for col in range(n):
                        if matrix[row][col] == "B":
                            current_row = row
                            current_col = col
                            matrix[current_row][current_col] = "."
                            break
        else:
            is_Game_Finish = True
            break
    if total_food == 10:
        matrix[current_row][current_col] = "S"
        print("You won! You fed the snake.")
        break
    command = input()

if is_Game_Finish:
    print("Game over!")
print(f"Food eaten: {total_food}")
for row in range(n):
    for col in range(n):
        print(matrix[row][col], end="")
    print()
