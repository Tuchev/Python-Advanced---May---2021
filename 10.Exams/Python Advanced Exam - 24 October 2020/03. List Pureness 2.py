def best_list_pureness(*args):
    num_list = args[0]
    n_times_rotate = args[1]
    best_sum = 0
    best_rotation = 0

    for i in range(n_times_rotate + 1):
        current_sum = 0
        for j in range(len(num_list)):
            current_sum += num_list[j] * j
        stack = []
        if current_sum > best_sum:
            best_sum = current_sum
            best_rotation = i
        stack.append(num_list.pop())
        for el in num_list:
            stack.append(el)
        num_list = stack

    return f"Best pureness {best_sum} after {best_rotation} rotations"


test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
