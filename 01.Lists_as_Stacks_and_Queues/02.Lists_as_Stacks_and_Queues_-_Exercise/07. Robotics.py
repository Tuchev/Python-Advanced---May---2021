from collections import deque


def time(hh, mm, ss):
    ss += 1
    if ss >= 60:
        ss = 0
        mm += 1
    if mm >= 60:
        mm = 0
        hh += 1
    if hh >= 24:
        hh = 0
    return (hh, mm, ss)


data = input().split(";")
robots = {sub.split("-")[0]: int(sub.split("-")[1]) for sub in data}
avaliable_robots = {k: 0 for k in robots}
tasks = deque()
hh, mm, ss = map(int, input().split(":"))
command = input()
while command != "End":
    tasks.append(command)
    command = input()
timed = time(hh, mm, ss)

while tasks:
    avaliable = [k for k, v in avaliable_robots.items() if v <= 0]
    if avaliable:
        print(f"{avaliable[0]} - {tasks.popleft()} [{timed[0]:0>2d}:{timed[1]:0>2d}:{timed[2]:0>2d}]")
        avaliable_robots[avaliable[0]] = robots[avaliable[0]]
        timed = time(timed[0], timed[1], timed[2])
        avaliable_robots = {k: v - 1 for k, v in avaliable_robots.items()}
    else:
        while not avaliable:
            tasks.append(tasks.popleft())
            avaliable_robots = {k: v - 1 for k, v in avaliable_robots.items()}
            timed = time(timed[0], timed[1], timed[2])
            avaliable = [k for k, v in avaliable_robots.items() if v <= 0]
