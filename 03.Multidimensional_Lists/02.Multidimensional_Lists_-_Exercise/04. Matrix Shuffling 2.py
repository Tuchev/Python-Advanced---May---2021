rows, cols = [int(el) for el in input().split()]

matrix = []

for row in range(rows):
    matrix.append(input().split())

data = input()
while not data == "END":
    data = data.split()
    if data[0] == "swap" and len(data) == 5:
        command = data[0]
        row_1 = int(data[1])
        col_1 = int(data[2])
        new_row = int(data[3])
        new_col = int(data[4])
        try:
            matrix[row_1][col_1], matrix[new_row][new_col] = matrix[new_row][new_col], matrix[row_1][col_1]
            for row in range(rows):
                for col in range(cols):
                    print(matrix[row][col], end=' ')
                print()
        except IndexError:\
            print("Invalid input!")
    else:
        print("Invalid input!")
    data = input()
