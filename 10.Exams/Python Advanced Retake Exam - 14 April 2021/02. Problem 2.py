player_1, player_2 = input().split(", ")

matrix = []
for row in range(7):
    matrix.append([el for el in input().split()])

move = 0
player_1_points = 501
player_1_moves = 1
player_2_points = 501
player_2_moves = 1
is_win = False

while True:
    row, col = [int(el) for el in input()[1: -1].split(", ")]
    move += 1

    if move % 2 != 0:
        if row not in range(7) or col not in range(7):
            player_1_moves += 1
            continue

        score = matrix[row][col]
        if score.isnumeric():
            player_1_points -= int(score)
        elif score == "D":
            score = (int(matrix[row][0]) + int(matrix[row][-1]) + int(matrix[0][col]) + int(matrix[6][col])) * 2
            player_1_points -= score
        elif score == "T":
            score = (int(matrix[row][0]) + int(matrix[row][-1]) + int(matrix[0][col]) + int(matrix[6][col])) * 3
            player_1_points -= score
        elif score == "B":
            print(f"{player_1} won the game with {player_1_moves} throws!")
            is_win = True
            break
        if player_1_points <= 0:
            is_win = True
            break
        player_1_moves += 1
    else:
        if row not in range(7) or col not in range(7):
            player_2_moves += 1
            continue

        score = matrix[row][col]
        if score.isnumeric():
            player_2_points -= int(score)
        elif score == "D":
            score = (int(matrix[row][0]) + int(matrix[row][-1]) + int(matrix[0][col]) + int(matrix[6][col])) * 2
            player_2_points -= score
        elif score == "T":
            score = (int(matrix[row][0]) + int(matrix[row][-1]) + int(matrix[0][col]) + int(matrix[6][col])) * 3
            player_2_points -= score
        elif score == "B":
            print(f"{player_2} won the game with {player_2_moves} throws!")
            is_win = True
            break
        if player_2_points <= 0:
            is_win = True
            break
        player_2_moves += 1
    if is_win:
        break

if player_1_points <= 0:
    print(f"{player_1} won the game with {player_1_moves} throws!")
elif player_2_points <= 0:
    print(f"{player_2} won the game with {player_2_moves} throws!")
