text = input()
max_count = 1
current = 1

for i in range(1, len(text)):
    if text[i] == text[i-1]:
        current += 1
        if current > max_count:
            max_count = current
    else:
        current = 1

print("Максимальное количество одинаковых символов подряд:", max_count)
