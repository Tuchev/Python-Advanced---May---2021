def get_magic_triangle(rows):
    row = [1]
    triangle = [[1]]
    for i in range(rows -1):
        row = [sum(x) for x in zip([0] + row, row + [0])]
        triangle.append(row)
    return triangle


print(get_magic_triangle(5))