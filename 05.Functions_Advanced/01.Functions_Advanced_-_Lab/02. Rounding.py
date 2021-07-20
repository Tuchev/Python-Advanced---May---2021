def make_rounded(seq):
    return [round(float(num)) for num in seq]


nums = [float(el) for el in input().split()]
print(make_rounded(nums))

