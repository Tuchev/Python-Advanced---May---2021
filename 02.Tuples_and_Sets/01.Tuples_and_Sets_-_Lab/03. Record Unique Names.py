n = int(input())
unique_names = set()
for _ in range(n):
    unique_names.add(input())
for person in unique_names:
    print(person)