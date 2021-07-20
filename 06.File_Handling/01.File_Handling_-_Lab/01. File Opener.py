# try:
#     open("text.txt")
# except FileNotFoundError:
#     print("File not found")

from os import path

if path.exists("text.txt"):
    print("File found")
else:
    print("File not found")

file = open("text.txt")
# print(file.readlines())

for line in file:
    print(line, end="")