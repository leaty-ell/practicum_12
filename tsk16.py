def check_brackets(text):
    balance = 0
    for char in text:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
            if balance < 0:
                return False
    return balance == 0

text = input("Введите текст: ")
if check_brackets(text):
    print("Скобки расставлены правильно.")
else:
    print("Скобки расставлены неправильно.")
