from collections import deque

def best_list_pureness(seq, k):
    best_result = 0
    best_rotation = 0
    seq = deque(seq)
    for i in range(0, k):
        seq.rotate(i)
        result = 0
        for idx in range(len(seq)):

            result += seq[idx] * idx
            if result > best_result:
                best_result = result
                best_rotation = i
    return f"Best pureness {best_result} after {best_rotation} rotations"


test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)


