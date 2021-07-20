import os

try:
    os.remove("PYTHON.txt")
except FileNotFoundError:
    print("File already deleted")

# if os.path.exists("PYTHON.txt"):
#     os.remove("PYTHON.txt")
# else:
#     print("File already deleted")