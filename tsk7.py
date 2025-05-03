sentence = input()
words = sentence.split()  
shortest_length = min(map(len, words)) 
print("Длина самого короткого слова:", shortest_length)
