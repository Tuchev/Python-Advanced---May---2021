text = input().split()
filtered_text = [el for el in text if len(el) % 2 == 0]
for el in filtered_text:
    print(el)