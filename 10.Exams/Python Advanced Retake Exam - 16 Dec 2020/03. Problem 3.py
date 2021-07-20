def get_magic_triangle(n):
    global Pascal_triangle
    temp = []

    # if n == 0:
    #     return []
    #
    # if n == 1:
    #     return [[1]]

    if n >= 2:
        Pascal_triangle = [[1]]

        for i in range(1, n):
            # print(i)
            for j in range(0, len(Pascal_triangle[i - 1])):
                # print(j)

                if j == 0:
                    temp.append(Pascal_triangle[i - 1][0])
                    # print(temp)

                else:
                    temp.append(Pascal_triangle[i - 1][j - 1] + Pascal_triangle[i - 1][j])
                    # print(temp)
            temp.append(1)
            Pascal_triangle.append(temp)
            temp = []

    return Pascal_triangle

print(get_magic_triangle(5))