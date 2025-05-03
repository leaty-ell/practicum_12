text = input()
max_spaces = 0
current = 0

for char in text:
    if char == ' ':
        current += 1
        if current > max_spaces:
            max_spaces = current
    else:
        current = 0

print("Максимальное количество последовательных пробелов:", max_spaces)
