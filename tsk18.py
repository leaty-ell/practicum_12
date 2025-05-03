def justify(text, width):
    words = text.split()
    lines = []
    current_line = []
    current_length = 0
    
    for word in words:
        if current_length + len(word) + len(current_line) <= width:
            current_line.append(word)
            current_length += len(word)
        else:
            lines.append(current_line)
            current_line = [word]
            current_length = len(word)
    if current_line:
        lines.append(current_line)
    
    for i in range(len(lines)):
        line = lines[i]
        if len(line) == 1:
            print(line[0])
            continue
        total_spaces = width - sum(len(word) for word in line)
        gaps = len(line) - 1
        spaces_per_gap = total_spaces // gaps
        extra = total_spaces % gaps
        
        for j in range(gaps):
            line[j] += ' ' * (spaces_per_gap + (1 if j < extra else 0))
        print(''.join(line))

text = input("Введите текст: ")
width = int(input("Введите ширину колонки: "))
print(format_text(text, width))
