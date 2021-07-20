n = int(input())

matrix = []
for _ in range(n):
    matrix.append(input().split())

raw_coordinates = input().split()
bombs_coordinates = []
for i in range(len(raw_coordinates)):
    current_coord = tuple(map(int, raw_coordinates[i].split(',')))
    bombs_coordinates.append(current_coord)

for el in bombs_coordinates:
    row, col = el
    bomb_value = matrix[row][col]
    bomb_value = int(bomb_value)
    if bomb_value > 0:
        cells_to_reduce = [(row, col),
                           (row - 1, col - 1),
                           (row - 1, col),
                           (row - 1, col + 1),
                           (row, col + 1),
                           (row + 1, col + 1),
                           (row + 1, col),
                           (row + 1, col - 1),
                           (row, col - 1)]
        for cell in cells_to_reduce:
            cell_row, cell_col = cell
            if 0 <= cell_row < n and 0 <= cell_col < n:
                current_value = int(matrix[cell_row][cell_col])
                if current_value > 0:
                    current_value -= bomb_value
                    matrix[cell_row][cell_col] = str(current_value)

alive_cells_positions = []
for row in range(n):
    for col in range(n):
        if int(matrix[row][col]) > 0:
            alive_cells_positions.append((row, col))

alive_cells_sum = 0
for cell in alive_cells_positions:
    cell_row, cell_col = cell
    alive_cells_sum += int(matrix[cell_row][cell_col])

print(f"Alive cells: {len(alive_cells_positions)}")
print(f"Sum: {alive_cells_sum}")
for row in range(len(matrix)):
    print(*matrix[row], sep=' ')
