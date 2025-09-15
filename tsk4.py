text= input()
def three_times(text):
    for ch in text:
        k = 0
        for c in text:
            if c == ch:
                count += 1
        if count == 3:
            return ch
            break

print(three_times(text))
