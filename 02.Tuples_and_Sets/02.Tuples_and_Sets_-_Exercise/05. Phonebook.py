data = input()
phonebook = set()

while True:
    if data in phonebook:
        phonebook.update(data)
    phonebook.add(data)
    data = input()
    if data.isdigit():
        break

all_contacts = []
for tel in phonebook:
    all_contacts.append(tel)
phonebook_dict = {}
for el in all_contacts:
    name, number = el.split("-")
    phonebook_dict[name] = number

for _ in range(int(data)):
    name = input()
    if name not in phonebook_dict:
        print(f"Contact {name} does not exist.")
    else:
        print(f"{name} -> {phonebook_dict[name]}")