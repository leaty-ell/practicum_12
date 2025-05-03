sentence = input()
words = sentence.split() 
words.sort(key=len)       # Сортируем слова по длине
print("Слова в порядке неубывания длин:", ' '.join(words))
