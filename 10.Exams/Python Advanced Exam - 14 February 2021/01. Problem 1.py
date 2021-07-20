from collections import deque

firework_effects = deque(input().split(", "))
explosive_power = deque(input().split(", "))

palm_firework = 0
willow_firework = 0
crossette_firework = 0

while firework_effects and explosive_power:
    if palm_firework >= 3 and willow_firework >= 3 and crossette_firework >= 3:
        break
    current_firework_effect = firework_effects.popleft()
    current_explosive_power = explosive_power.pop()
    current_firework_effect = int(current_firework_effect)
    current_explosive_power = int(current_explosive_power)
    if current_firework_effect <= 0:
        explosive_power.append(str(current_explosive_power))
        continue
    elif current_explosive_power <= 0:
        firework_effects.appendleft(str(current_firework_effect))
        continue
    else:
        result = current_firework_effect + current_explosive_power
        if result % 3 == 0 and result % 5 == 0:
            crossette_firework += 1
        elif result % 3 == 0 and result % 5 != 0:
            palm_firework += 1
        elif result % 3 != 0 and result % 5 == 0:
            willow_firework += 1

        else:
            current_firework_effect -= 1
            if current_firework_effect > 0:
                firework_effects.append(str(current_firework_effect))
            explosive_power.append(str(current_explosive_power))

if palm_firework >= 3 and willow_firework >= 3 and crossette_firework >= 3:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if firework_effects:
        print(f"Firework Effects left: {', '.join(firework_effects)}")
if explosive_power:
        print(f"Explosive Power left: {', '.join(explosive_power)}")
print(f"Palm Fireworks: {palm_firework}")
print(f"Willow Fireworks: {willow_firework}")
print(f"Crossette Fireworks: {crossette_firework}")