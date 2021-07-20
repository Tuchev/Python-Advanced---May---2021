n, m = input().split()

n = int(n)
m = int(m)

num_1 = set()
num_2 = set()

for _ in range(n):
    number = input()
    num_1.add(number)

for _ in range(m):
    number = input()
    num_2.add(number)

c = num_1.intersection(num_2)
for num in c:
    print(num)