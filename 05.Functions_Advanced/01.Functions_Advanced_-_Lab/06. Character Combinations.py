from itertools import permutations

result = list(permutations(input()))
for el in result:
    print(*el, sep="")
