all_tasks = [int(el) for el in input().split(", ")]
idx_of_the_needed_task = int(input())

new_list_of_tasks = sorted(all_tasks)

clock_cycles = 0


for task in new_list_of_tasks:
    current_idx = all_tasks.index(task)
    if current_idx != idx_of_the_needed_task:
        clock_cycles += int(task)
        all_tasks[current_idx] = 9999999999999999
    elif current_idx == idx_of_the_needed_task:
        clock_cycles += int(task)
        break
print(clock_cycles)