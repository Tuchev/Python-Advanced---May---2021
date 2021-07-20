def is_even(num):
    return num % 2 == 0

print(list(filter(is_even, [int(el) for el in input().split()])))