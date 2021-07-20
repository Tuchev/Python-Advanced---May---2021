def is_odd(num):
    return num % 2 != 0


def is_even(num):
    return num % 2 == 0


command = input()
all_nums = [int(el) for el in input().split()]


if command == "Odd":
    odd_nums = list(filter(is_odd, all_nums))
    print(sum(odd_nums) * len(all_nums))
else:
    even_nums = list(filter(is_even, all_nums))
    print(sum(even_nums) * len(all_nums))