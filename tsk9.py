def find_dubl(sentence):
    words = sentence.split()  
    for i in range(len(words)):
        word = words[i]
        if word in words[i+1:]: 
            return word
            break


sentence = input()
print(find_dubl(sentence))
