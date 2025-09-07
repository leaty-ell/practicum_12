
from hyphen import Hyphenator
h_en = Hyphenator('ru_RU')

text = input("Введите текст: ")
width = int(input("Введите ширину колонки: "))

words = text.split()
line = []

for word in words:
    while len(word) > width:
        parts = h_en.syllables(word)
        if not parts:
            break
        split_index = 0
        total = 0
        for p in parts:
            if total + len(p) > width:
                break
            total += len(p)
            split_index += 1
        print(word[:total] + "-")
        word = word[total:]
    line.append(word)
    if sum(len(w) for w in line) + len(line) - 1 > width:
        print(" ".join(line[:-1]))
        line = [line[-1]]

print(" ".join(line))
