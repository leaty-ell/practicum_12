sentence = input()
words = sentence.split() 
words.sort(key=len)       
print(' '.join(words))
