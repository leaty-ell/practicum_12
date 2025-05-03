s1 = input("Введите первую строку: ")
s2 = input("Введите вторую строку: ")
s3 = input("Введите третью строку: ")

unique_chars = set()

all_chars = set(s1 + s2 + s3)

for char in all_chars:
    count = 0
    if char in s1:
        count += 1
    if char in s2:
        count += 1
    if char in s3:
        count += 1
    if count == 1:
        unique_chars.add(char)

print("Символы, встречающиеся только в одной строке:", ', '.join(unique_chars))
