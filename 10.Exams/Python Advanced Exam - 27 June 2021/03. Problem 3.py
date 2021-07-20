from collections import deque


def math_operations(*nums, **keywords):
    rotation = 1
    numbers = deque(nums)
    while numbers:
        num = numbers.popleft()
        if rotation == 5:
            rotation = 1
            numbers.appendleft(num)
        elif rotation == 1:
            keywords["a"] += num
            rotation += 1
        elif rotation == 2:
            keywords["s"] -= num
            rotation += 1
        elif rotation == 3:
            if num != 0:
                keywords["d"] /= num
            rotation += 1
        elif rotation == 4:
            keywords["m"] *= num
            rotation += 1

    return keywords


print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
print(math_operations(6, a=0, s=0, d=0, m=0))
