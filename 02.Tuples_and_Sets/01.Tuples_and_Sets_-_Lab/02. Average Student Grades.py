def calculate_avg(grades):
    return sum(grades) / len(grades)


number_of_students = int(input())
students = {}

for _ in range(number_of_students):
    name, grade = input().split()
    if name not in students:
        students[name] = []
    students[name].append(float(grade))

for name, grade_st in students.items():
    grades_string = " ".join(map(lambda grade: f"{grade:.2f}", grade_st))
    print(f"{name} -> {grades_string} (avg: {calculate_avg([float(x) for x in grade_st]):.2f})")