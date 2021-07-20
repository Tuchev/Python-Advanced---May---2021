def permutation(text, count):
    if count >= len(text):
        print("".join(text))
        return
    permutation(text, count + 1)
    for i in range(count + 1, len(text)):
        text[count], text[i] = text[i], text[count]
        permutation(text, count + 1)
        text[count], text[i] = text[i], text[count]

text = list(input())
permutation(text, 0)
