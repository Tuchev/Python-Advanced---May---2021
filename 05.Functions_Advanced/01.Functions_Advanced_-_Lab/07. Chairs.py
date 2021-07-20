from itertools import combinations

result = list(combinations(input().split(", "), int(input())))
for el in result:
    print(*el, sep=", ")