# lines = [_ for _ in input().split("|")]
#
# matrix = ([list(map(int, lines[row].split())) for row in range(len(lines) - 1, -1, -1)])
# flatten_matrix = [val for sublist in matrix for val in sublist]
# print(" ".join([str(_) for _ in flatten_matrix]))

input_string = [item.split() for item in input().split("|")[::-1]]
print(*[element for item in input_string for element in item])