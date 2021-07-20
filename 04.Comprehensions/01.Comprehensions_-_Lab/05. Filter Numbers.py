start_num = int(input())
end_num = int(input())

nums_from_2_to_10 = [num for num in range(2, 10 + 1)]

all_numbers = [num for num in range(start_num, end_num + 1)]

filtered_nums = [num for num in all_numbers if any ([num % x == 0 for x in nums_from_2_to_10])]
print(filtered_nums)