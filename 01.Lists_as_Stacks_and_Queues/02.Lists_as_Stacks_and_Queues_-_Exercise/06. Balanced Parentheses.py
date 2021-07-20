from collections import deque

parentheses = deque(list(input()))
balanced = []

while parentheses:
    balanced.append(parentheses.popleft())
    if len(balanced) > 1:
        if balanced[-2:] != ['(', ')'] and balanced[-2:] != ['[', ']'] and balanced[-2:] != ['{', '}']:
            continue
        balanced.pop()
        balanced.pop()

if balanced:
    print("NO")
else:
    print("YES")