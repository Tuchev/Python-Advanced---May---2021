n = int(input())

odd_numbers = set()
even_numbers = set()
line = 0

sum_of_name_letter = 0

for _ in range(n):
    name = input()
    line += 1
    for letter in name:
        a = ord(letter)
        sum_of_name_letter += int(a)
    sum_of_name_letter = int(sum_of_name_letter / line)
    if sum_of_name_letter % 2 == 0:
        even_numbers.add(int(sum_of_name_letter))
    else:
        odd_numbers.add(int(sum_of_name_letter))
    sum_of_name_letter = 0

if sum(odd_numbers) > sum(even_numbers):
    result = odd_numbers.difference(even_numbers)
elif sum(odd_numbers) < sum(even_numbers):
    result = odd_numbers.symmetric_difference(even_numbers)
else:
    result = odd_numbers.union(even_numbers)
print(str(result)[1:-1])