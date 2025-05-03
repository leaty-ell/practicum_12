def is_vowel(c):
    return c.lower() in 'аеёиоуыэюя'

def can_split(word):
    if len(word) <= 1:
        return False
    for i in range(1, len(word)):
        left = word[:i]
        right = word[i:]
        if (is_vowel(left[-1]) and (len(right) == 1 or is_vowel(right[0])):
            return True
    return False

def split_word(word):
    if len(word) <= 1:
        return [word]
    for i in range(1, len(word)):
        left = word[:i]
        right = word[i:]
        if (is_vowel(left[-1])) and (len(right) == 1 or is_vowel(right[0])):
            return [left, right]
    return [word]

def format_text_russian(text, width):
    words = text.split()
    lines = []
    current_line = []
    current_length = 0
    
    for word in words:
        if current_length + len(word) + len(current_line) <= width:
            current_line.append(word)
            current_length += len(word)
        else:
            if len(current_line) == 0:
                if len(word) > width:
                    parts = split_word(word)
                    if len(parts) > 1:
                        part1 = parts[0] + '-'
                        if current_length + len(part1) + len(current_line) <= width:
                            current_line.append(part1)
                            lines.append(current_line)
                            current_line = [parts[1]]
                            current_length = len(parts[1])
                        else:
                            lines.append([part1])
                            current_line = [parts[1]]
                            current_length = len(parts[1])
                    else:
                        lines.append([word[:width-1] + '-'])
                        current_line = [word[width-1:]]
                        current_length = len(word[width-1:])
                else:
                    lines.append([word])
            else:
                lines.append(current_line)
                current_line = [word]
                current_length = len(word)
    if current_line:
        lines.append(current_line)
    
    formatted_lines = []
    for line in lines:
        if len(line) == 1:
            formatted_lines.append(line[0])
            continue
        total_spaces = width - sum(len(word) for word in line)
        space_between = total_spaces // (len(line) - 1)
        extra_spaces = total_spaces % (len(line) - 1)
        
        formatted_line = []
        for i in range(len(line) - 1):
            formatted_line.append(line[i])
            formatted_line.append(' ' * (space_between + (1 if i < extra_spaces else 0)))
        formatted_line.append(line[-1])
        formatted_lines.append(''.join(formatted_line))
    
    return '\n'.join(formatted_lines)

text = input("Введите текст: ")
width = int(input("Введите ширину колонки: "))
print(format_text_russian(text, width))
