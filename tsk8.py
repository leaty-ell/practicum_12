sentence = input()
words = sentence.split() 
words.sort(key=len)       # параметр key указывает ф-цию по знач. которой будет выполняться сравнение)

print(' '.join(words))
