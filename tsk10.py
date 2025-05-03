sentence = input()
words = sentence.split()
first_word = words[0]
result_words = []

for word in words[1:]:
    if word != first_word:
        # Проверяем, есть ли повторяющиеся буквы
        unique_letters = set(word)
        if len(unique_letters) == len(word):
            result_words.append(word)

print("Подходящие слова:", ', '.join(result_words))
