text = input("Введите текст: ")
width = int(input("Введите ширину колонки: "))

words = text.split()
line = []

for word in words:
    # Проверяем, умещается ли слово в текущую строку
    if sum(len(w) for w in line) + len(line) + len(word) > width:
        # Выравнивание по ширине
        if len(line) == 1:
            print(line[0])
        else:
            total_spaces = width - sum(len(w) for w in line)
            space_between = total_spaces // (len(line) - 1)
            extra = total_spaces % (len(line) - 1)
            for i in range(len(line)-1):
                print(line[i], end=" " * (space_between + (1 if i < extra else 0)))
            print(line[-1])
        line = [word]
    else:
        line.append(word)

# Последняя строка
print(" ".join(line))
