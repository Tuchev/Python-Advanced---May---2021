def shooting(player, direction, matrix):
    x, y = direction
    current_direction_x, current_direction_y = player
    target_hit = []
    while True:
        current_direction_x += x
        current_direction_y += y
        if current_direction_x in range(5) and current_direction_y in range(5):
            if matrix[current_direction_x][current_direction_y] == 'x':
                matrix[current_direction_x][current_direction_y] = '.'
                target_hit = [current_direction_x, current_direction_y]
                break
        else:
            break
    return target_hit, matrix


def find_player(matrix):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == 'A':
                return [row, col]


def check_for_targets(matrix):
    targets = []
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == 'x':
                targets.append([row, col])
    return targets


def move(player, command, matrix):
    direction = command[1]
    steps = int(command[2])
    if direction == 'up' or direction == 'down':
        if direction == 'up':
            if player[0] - steps in range(5):
                if matrix[player[0] - steps][player[1]] == '.':
                    matrix[player[0]][player[1]] = '.'
                    matrix[player[0] - steps][player[1]] = 'A'
                    player = [player[0] - steps, player[1]]
        elif direction == 'down':
            if player[0] + steps in range(5):
                if matrix[player[0] + steps][player[1]] == '.':
                    matrix[player[0]][player[1]] = '.'
                    matrix[player[0] + steps][player[1]] = 'A'
                    player = [player[0] + steps, player[1]]
    elif direction == 'left' or direction == 'right':
        if direction == 'left':
            if player[1] - steps in range(5):
                if matrix[player[0]][player[1] - steps] == '.':
                    matrix[player[0]][player[1]] = '.'
                    matrix[player[0]][player[1] - steps] = 'A'
                    player = [player[0], player[1] - steps]
        elif direction == 'right':
            if player[1] + steps in range(5):
                if matrix[player[0]][player[1] + steps] == '.':
                    matrix[player[0]][player[1]] = '.'
                    matrix[player[0]][player[1] + steps] = 'A'
                    player = [player[0], player[1] + steps]

    return player, matrix


def shoot(player, command, matrix):
    direction = command[1]
    hit_target = []
    if direction == 'up' or direction == 'down':
        if direction == 'up':
            target, matrix = shooting(player, [-1, 0], matrix)
            hit_target.append(target)
        elif direction == 'down':
            target, matrix = shooting(player, [1, 0], matrix)
            hit_target.append(target)
    elif direction == 'left' or direction == 'right':
        if direction == 'left':
            target, matrix = shooting(player, [0, -1], matrix)
            hit_target.append(target)
        elif direction == 'right':
            target, matrix = shooting(player, [0, 1], matrix)
            hit_target.append(target)
    return player, matrix, hit_target


matrix = [[x for x in input().split()] for _ in range(5)]
player = find_player(matrix)
num = int(input())
hit_targets = []
for _ in range(num):
    targets = check_for_targets(matrix)
    if not targets:
        break
    command = input().split(' ')
    if command[0] == 'move':
        player, matrix = move(player, command, matrix)
    elif command[0] == 'shoot':
        player, matrix, targetss = shoot(player, command, matrix)
        for i in targetss:
            if len(i) > 0:
                hit_targets.append(i)
if check_for_targets(matrix):
    print(f"Training not completed! {len(check_for_targets(matrix))} targets left.")
else:
    print(f"Training completed! All {len(hit_targets)} targets hit.")
for i in hit_targets:
    print(i)
