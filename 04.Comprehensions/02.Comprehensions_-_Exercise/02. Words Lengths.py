names = input().split(", ")
result = [f"{name} -> {len(name)}" for name in names]
print(", ".join(result))