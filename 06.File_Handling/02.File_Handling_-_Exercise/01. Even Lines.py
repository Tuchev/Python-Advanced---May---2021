# import re
#
#
# def replace_symbols(line):
#     return re.sub(r"[\?,\!\.-]", '@', line)
#
#
# save_row_el = []
# with open('text.txt', 'r') as file:
#     lines = file.readlines()
#     for row in range(len(lines)):
#         if row % 2 == 0:
#             replaced = replace_symbols(lines[row]).split()
#             save_row_el.append(" ".join(replaced[::-1]))
#
# with open('output.txt', 'w') as f:
#     f.writelines('\n'.join(save_row_el))


import re

file = open("text.txt")

for idx, line in enumerate(file.readlines()):
    if idx % 2 != 0:
        continue

    line = re.sub(r"[-,\.!?]", "@", line)
    line = " ".join(reversed(line.split()))

    print(line.strip())
file.close()