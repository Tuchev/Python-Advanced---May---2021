from collections import deque

males = deque(input().split(" "))
females = deque(input().split(" "))

matches = 0

while males and females:
    current_male = males.pop()
    current_female = females.popleft()
    current_male = int(current_male)
    current_female = int(current_female)

    if current_male <= 0:
        females.appendleft(str(current_female))

    elif current_female <= 0:
        males.append(str(current_male))

    elif current_male % 25 == 0:
        females.appendleft(str(current_female))
        current_male = males.pop()
        continue

    elif current_female % 25 == 0:
        males.append(str(current_male))
        current_female = females.popleft()
        continue

    elif current_male == current_female:
        matches += 1

    elif current_male != current_female:
        current_male -= 2
        males.append(str(current_male))

print(f"Matches: {matches}")
if males:
    print(f"Males left: {', '.join(reversed(males))}")
else:
    print(f"Males left: none")
if females:
    print(f"Females left: {', '.join(females)}")
else:
    print(f"Females left: none")