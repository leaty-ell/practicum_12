hint = input("Введите подсказку: ")
word = input("Введите загаданное слово: ").lower()
print("\n" * 25)
masked = "*" * len(word)
attempts = 10

for _ in range(attempts):
    print(hint)
    print(masked)
    choice = input("Буква или слово (0 - буква, 1 - слово)? ")
    if choice == "0":
        letter = input("Введите букву: ").lower()
        new_masked = ""
        for i in range(len(word)):
            if word[i] == letter or masked[i] != "*":
                new_masked += word[i]
            else:
                new_masked += "*"
        masked = new_masked
    else:
        guess = input("Введите слово: ").lower()
        if guess == word:
            print("Победа!")
            break
    if masked == word:
        print("Победа!")
        break
else:
    print("Проигрыш!")
