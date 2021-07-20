from collections import deque

green_light = int(input())
windows = int(input())

cars = deque()
cars_counter = 0
is_crash = False

command = input()

while not command == "END":
    if command == "green":
        if cars:
            current = cars.popleft()
            seconds_left = green_light - len(current)
            while seconds_left > 0:
                cars_counter += 1
                if cars:
                    current = cars.popleft()
                    seconds_left -= len(current)
                else:
                    break
            if seconds_left == 0:
                cars_counter += 1
            if windows >= abs(seconds_left):
                if seconds_left < 0:
                    cars_counter += 1
            else:
                idx = windows + seconds_left
                print("A crash happened!")
                print(f"{current} was hit at {current[idx]}.")
                is_crash = True
                break
    else:
        cars.append(command)
    command = input()

if not is_crash:
    print("Everyone is safe.")
    print(f"{cars_counter} total cars passed the crossroads.")