nums = [int(el) for el in input().split()]
filtered_nums = []
for num in nums:
    if num % 2 == 0:
        filtered_nums.append(num)
print(filtered_nums)

