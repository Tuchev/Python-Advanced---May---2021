line = input()
phonebook = {}

while not line.isdigit():
    name, phone_number = line.split('-')
    phonebook[name] = phone_number
    line = input()

count = int(line)
for contact in range(count):
    command = input()
    if command in phonebook:
        print(f"{command} -> {phonebook[command]}")
    else:
        print(f"Contact {command} does not exist.")