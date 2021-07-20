nums = [int(el) for el in input().split()]


def is_positive(num):
    return num >= 0


def is_negative(num):
    return num < 0


positive_nums = list(filter(is_positive, nums))
negative_nums = list(filter(is_negative, nums))
print(sum(negative_nums))
print(sum(positive_nums))

if sum(positive_nums) > abs(sum(negative_nums)):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")