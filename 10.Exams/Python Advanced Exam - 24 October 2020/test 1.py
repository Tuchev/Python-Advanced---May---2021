numbers = [int(n) for n in input().split(", ")]
index = int(input())

cycle_count = 0
needed_task = numbers[index]

for el in numbers:
    if el <= needed_task:
        cycle_count += el

print(cycle_count)