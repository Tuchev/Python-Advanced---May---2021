n = int(input())

numbers = []
for _ in range(1, n + 1):
    data = input().split()
    if int(data[0]) == 1:
        numbers.append(int(data[1]))
    elif int(data[0]) == 2:
        if len(numbers) > 0:
            numbers.pop()
    elif int(data[0]) == 3:
        if len(numbers) > 0:
            print(max(numbers))
    elif int(data[0]) == 4:
        if len(numbers) > 0:
            print(min(numbers))

reverse_numbers = []

for _ in range(len(numbers)):
    reverse_numbers.append(str(numbers.pop()))
print(", ".join(reverse_numbers))