sentence = input()

def reverse_words(sentence):
    words = sentence.split()
    return " ".join(words[::-1])

reversed_sentence = reverse_words(sentence)
print(reversed_sentence)

