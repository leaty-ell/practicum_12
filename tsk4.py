text = input()
char_count = {}

for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

for char in char_count:
    if char_count[char] == 3:
        print("Символ, встречающийся ровно три раза:", char)
        break  
