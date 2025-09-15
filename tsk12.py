import keyword #модуль с ключевыми словами

name = input().strip()  # убираем пробелы по краям

if (name  # строка не пустая
    and not keyword.iskeyword(name)  
    and (name[0].isalpha() or name[0] == '_') 
    and name.replace('_', '').isalnum()):  
    print("Допустимое имя")
else:
    print("Недопустимое имя")
