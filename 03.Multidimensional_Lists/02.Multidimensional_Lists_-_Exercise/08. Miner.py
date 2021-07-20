from collections import deque


def create_matrix(r):
    mm = []
    for _ in range(r):
        mm.append([x for x in input().split()])
    return mm


def starting_position(m):
    start_pos = ()
    for x in range(len(m)):
        if 's' in m[x]:
            start_pos = (x, matrix[x].index('s'))
    return start_pos


def is_valid(ro, co):
    if 0 <= ro < len(matrix) and 0 <= co < len(matrix):
        return True
    return False


def check_coal(m):
    has = False
    for x in range(len(m)):
        if 'c' in m[x]:
            has = True
            break
    return has


def sum_coal(m):
    sums = 0
    for r in range(len(m)):
        if 'c' in m[r]:
            for c in range(len(m)):
                if m[r][c] == 'c':
                    sums += 1
    return sums


rows = int(input())
moves = deque(input().split())
matrix = create_matrix(rows)
sp = starting_position(matrix)
row, col = sp
coal = 0
finished = False

while True:
    if moves:
        next_move = moves.popleft()
        if next_move == 'up':
            if is_valid(row - 1, col):
                row -= 1
        elif next_move == 'down':
            if is_valid(row + 1, col):
                row += 1
        elif next_move == 'right':
            if is_valid(row, col + 1):
                col += 1
        elif next_move == 'left':
            if is_valid(row, col - 1):
                col -= 1
        if matrix[row][col] == 'e':
            print(f'Game over! ({row}, {col})')
            finished = True
            break
        elif matrix[row][col] == 'c':
            coal += 1
            matrix[row][col] = '*'
            if not check_coal(matrix):
                print(f'You collected all coals! ({row}, {col})')
                finished = True
                break
    else:
        break

if not finished:
    print(f'{sum_coal(matrix)} coals left. ({row}, {col})')
