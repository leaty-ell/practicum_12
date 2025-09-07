text = input()
max_spaces = 0
current = 0

for i in text:
    if i == ' ':
        current += 1
        if current > max_spaces:
            max_spaces = current
    else:
        current = 0
        
print(max_spaces)
