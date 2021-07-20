from collections import deque

bomb_effects = deque(input().split(", "))
bomb_casing = deque(input().split(", "))

DATURA_BOMBS = 40
CHERRY_BOMBS = 60
SMOKE_DEKOY_BOMBS = 120

datura_bombs = 0
cherry_bombs = 0
smoke_dekoy_bombs = 0

is_Completed = False

while bomb_effects and bomb_casing:
    current_bomb_effects = int(bomb_effects.popleft())
    current_bomb_casing = int(bomb_casing.pop())

    if current_bomb_effects + current_bomb_casing == DATURA_BOMBS:
        datura_bombs += 1
    elif current_bomb_effects + current_bomb_casing == CHERRY_BOMBS:
        cherry_bombs += 1
    elif current_bomb_effects + current_bomb_casing == SMOKE_DEKOY_BOMBS:
        smoke_dekoy_bombs += 1
    else:
        current_bomb_casing -= 5
        bomb_effects.appendleft(str(current_bomb_effects))
        bomb_casing.append(str(current_bomb_casing))
    if datura_bombs >= 3 and cherry_bombs >= 3 and smoke_dekoy_bombs >= 3:
        is_Completed = True
        break
if is_Completed:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if bomb_effects:
    print(f"Bomb Effects: {', '.join([str(el) for el in bomb_effects])}")
else:
    print("Bomb Effects: empty")
if bomb_casing:
    print(f"Bomb Casings: {', '.join([str(el) for el in bomb_casing])}")
else:
    print("Bomb Casings: empty")
print(f"Cherry Bombs: {cherry_bombs}")
print(f"Datura Bombs: {datura_bombs}")
print(f"Smoke Decoy Bombs: {smoke_dekoy_bombs}")

