from collections import deque

def list_manipulator(*args):
    numbers = args[0]
    numbers = deque(numbers)
    command = args[1]
    explanation = args[2]
    if len(args) <4:
        if command == "remove" and explanation == "end":
            numbers.pop()
        elif command == "remove" and explanation == "beginning":
            numbers.popleft()
    else:
        numbers_to_operate = [el for el in args[3::]]
        if command == "add" and explanation == "beginning":
            for i in sorted(numbers_to_operate, reverse=True):
                numbers.appendleft(i)
        elif command == "add" and explanation == "end":
            for i in numbers_to_operate:
                numbers.append(i)
        elif command == "remove" and explanation == "beginning":
            for _ in range(args[3]):
                numbers.popleft()
        elif command == "remove" and explanation == "end":
            for _ in range(args[3]):
                numbers.pop()

    return list(numbers)



print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
