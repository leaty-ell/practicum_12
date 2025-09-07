import keyword  # модуль с ключевыми словами

name = input()

if (not keyword.iskeyword(name)      
    and name[0].isalpha()           # проверка, что буква
    and name.replace("_", "").isalnum()):  # Остальные символы буквы/цифры
    print("Допустимое имя")
else:
    print("Недопустимое имя")
