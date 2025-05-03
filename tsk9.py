sentence = input("Введите предложение: ")
words = sentence.split()  

word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1


for word in word_counts:  
    if word_counts[word] == 2:  
        print("Повторяющееся слово:", word)
        break  
