numbers = [int(el) for el in input().split(", ")]

positive = [el for el in numbers if el >= 0]
negative = [el for el in numbers if el < 0]
even = [el for el in numbers if el % 2 == 0]
odd = [el for el in numbers if el % 2 != 0]

print("Positive:", ", ".join([str(el) for el in positive]))
print("Negative:", ", ".join([str(el) for el in negative]))
print("Even:", ", ".join([str(el) for el in even]))
print("Odd:", ", ".join([str(el) for el in odd]))