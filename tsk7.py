sentence = input()

def shortst_length(sentence):
    words = sentence.split()
    return min(len(word) for word in words)
  
print(shortst_length(sentence))
