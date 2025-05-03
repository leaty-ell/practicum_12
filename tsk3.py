text = input("Введите текст: ").lower()
unique_letters = set()

for char in text:
    if char.isalpha():
        unique_letters.add(char)

print("Количество различных букв:", len(unique_letters))
