text = input()

def dif_letters(text):
    text = text.lower()      
    letters = set(text)      
    return len(letters)

print(dif_letters(text))
