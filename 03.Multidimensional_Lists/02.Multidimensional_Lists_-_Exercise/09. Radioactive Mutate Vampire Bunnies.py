rows, cols = [int(x) for x in input().split()]


def read_matrix(r):
    matrix = []
    for _ in range(r):
        matrix.append(list(input()))
    return matrix


def find_player(mtr):
    for r in range(len(mtr)):
        for c in range(len(mtr[0])):
            if mtr[r][c] == 'P':
                return [r, c]


def is_move_valid(r, c):
    return 0 <= r < rows and 0 <= c < cols


def player_move(r, c, dir):
    global potential_row, potential_col
    if dir == 'U':
        potential_row = r - 1
        potential_col = c
    elif dir == 'R':
        potential_col = c + 1
        potential_row = r
    elif dir == 'D':
        potential_row = r + 1
        potential_col = c
    elif dir == 'L':
        potential_col = c - 1
        potential_row = r

    if is_move_valid(potential_row, potential_col):
        matrix[r][c] = '.'
        if matrix[potential_row][potential_col] == 'B':
            return 'dead', potential_row, potential_col
        matrix[potential_row][potential_col] = 'P'
        return potential_row, potential_col
    matrix[r][c] = '.'
    return 'won', r, c


def get_bunnies_indexes(mtr):
    bunnies = []
    for i in range(len(mtr)):
        for j in range(len(mtr[0])):
            if mtr[i][j] == 'B':
                bunnies.append([i, j])

    return bunnies


def mutate_bunny(mtr, r, c, is_dead):
    global dead_row, dead_col
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for position in directions:
        potential_row = r + position[0]
        potential_col = c + position[1]
        if is_move_valid(potential_row, potential_col):
            if mtr[potential_row][potential_col] == 'P':
                is_dead = True
                dead_row, dead_col = potential_row, potential_col
            mtr[potential_row][potential_col] = 'B'
    if is_dead:
        return is_dead, dead_row, dead_col


def bunnies_mutate(mtr, is_dead):
    result = None
    bunnies = get_bunnies_indexes(mtr)
    for bunny in bunnies:
        res = mutate_bunny(mtr, bunny[0], bunny[1], is_dead)
        if res:
            result = res
    return result


matrix = read_matrix(rows)
player_position = find_player(matrix)
commands = list(input())
is_dead = False

for direction in commands:
    res = player_move(player_position[0], player_position[1], direction)

    res_1 = bunnies_mutate(matrix, is_dead)
    if res_1:
        is_dead, row, col = res_1

    if res[0] == 'dead':
        for row in matrix:
            print(''.join(row))
        print(f'dead: {res[1]} {res[2]}')
        break
    elif res[0] == 'won':
        for row in matrix:
            print(''.join(row))
        print(f'won: {res[1]} {res[2]}')
        break
    else:
        player_position[0], player_position[1] = res[0], res[1]

    if is_dead:
        for _ in matrix:
            print(''.join(_))
        print(f'dead: {row} {col}')
        break
