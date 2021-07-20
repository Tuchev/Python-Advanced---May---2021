text = input()

unique_letter = set()
for letter in text:
    unique_letter.add(letter)
all_letters = sorted(unique_letter)
for symbol in all_letters:
    print(f"{symbol}: {text.count(symbol)} time/s")