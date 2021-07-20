n = int(input())

unique_usernames = set()

for _ in range(n):
    name = input()
    unique_usernames.add(name)

for name in unique_usernames:
    print(name)