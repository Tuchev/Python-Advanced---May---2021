n = int(input())

unique_elements = set()

for _ in range(n):
    elements = input().split()
    for el in elements:
        unique_elements.add(el)

for element in unique_elements:
    print(element)