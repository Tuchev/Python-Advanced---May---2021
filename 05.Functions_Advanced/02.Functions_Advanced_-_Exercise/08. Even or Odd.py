def is_even(num):
    return num % 2 ==0


def is_odd(num):
    return num % 2 != 0


def even_odd(*args):
    if args[-1] == "even":
        return list(filter(is_even, args[0: -1]))
    elif args[-1] == "odd":
        return list(filter(is_odd, args[0: -1]))



print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))