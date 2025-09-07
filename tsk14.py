hint = input("Введите подсказку: ")
word = input("Введите загаданное слово: ")

print("\n" * 25)

hidden_word = []
for letter in word:
    hidden_word.append("*")

attempts = 10
print(hint)


while attempts > 0:
    print("".join(hidden_word))

    choice = input("Буква или слово (0 - буква, 1 - слово)? ")

    if choice == "0":
        letter = input("Введите букву: ")
        for i in range(len(word)):
            if word[i] == letter:
                hidden_word[i] = letter
    else:
        guess = input("Введите слово: ")
        if guess == word:
            print("Победа!")
            break
        else:
            print("Неправильно!")
            attempts -= 1
            print("Осталось попыток:", attempts)


    if "".join(hidden_word) == word:
        print("Победа!")
        break
else:
    print("Проигрыш!")
