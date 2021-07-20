n = int(input())

x = set()
y = set()
longest_intersection = set()

for _ in range(n):
    data = input().split("-")

    first = data[0].split(",")
    second = data[1].split(",")

    start_num_1 = int(first[0])
    end_num_1 = int(first[1])

    start_num_2 = int(second[0])
    end_num_2 = int(second[1])

    for num in range(start_num_1, end_num_1 +1):
        x.add(num)

    for num in range(start_num_2, end_num_2 + 1):
        y.add(num)

    intersection = x.intersection(y)

    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection
    x.clear()
    y.clear()

list_of_intersections = []

for i in longest_intersection:
    list_of_intersections.append(i)

print(f"Longest intersection is {list_of_intersections} with length {len(longest_intersection)}")