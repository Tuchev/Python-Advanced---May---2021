from math import floor

def is_idx_valid(r, c):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False


n = int(input())

matrix = []
for _ in range(n):
    matrix.append([el for el in input().split()])

position = None

for row in range(n):
    for col in range(n):
        if matrix[row][col] == "P":
            position = (row, col)

current_row, current_col = position[0], position[1]
total_points = 0
path = []
is_winner = False

command = input()
while command:

    if command == "up":
        current_row -= 1
    elif command == "down":
        current_row += 1
    elif command == "right":
        current_col += 1
    elif command == "left":
        current_col -= 1
    else:
        command = input()
        continue

    if not is_idx_valid(current_row, current_col):
        break
    elif matrix[current_row][current_col] == "X":
        break
    else:
        total_points += int(matrix[current_row][current_col])
        path.append([current_row, current_col])
        if total_points >= 100:
            is_winner = True
            break
    command = input()

if is_winner:
    print(f"You won! You've collected {total_points} coins.")
else:
    print(f"Game over! You've collected {floor(total_points / 2)} coins.")
print(f"Your path: ")
print("\n".join([str(el) for el in path]))
