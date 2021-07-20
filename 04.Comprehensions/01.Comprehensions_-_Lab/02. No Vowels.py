word = input().lower()

print("".join([char for char in word if char not in "aeoui"]))