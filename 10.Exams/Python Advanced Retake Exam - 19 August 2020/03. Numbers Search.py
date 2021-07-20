def numbers_searching(*args):
    all_numbers = [int(el) for el in args]
    all_numbers = sorted(all_numbers)
    missing_numbers = []
    duplicate_numbers = [x for x in all_numbers if all_numbers.count(x) > 1]
    duplicate_numbers = set(duplicate_numbers)
    duplicate_numbers = list(duplicate_numbers)
    for el in range(all_numbers[0], all_numbers[-1] + 1):
        if el not in all_numbers:
            missing_numbers.append(el)
    result = []
    result.extend(missing_numbers)
    result.append(sorted(duplicate_numbers))

    return result


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
