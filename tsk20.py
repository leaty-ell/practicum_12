def number_to_words(n):
    units = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    teens = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 
             'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    tens = ['', 'десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 
            'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    hundreds = ['', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 
                'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']
    thousands = ['', 'тысяча', 'тысячи', 'тысяч']
    millions = ['', 'миллион', 'миллиона', 'миллионов']
    
    if n == 0:
        return 'ноль'
    
    def convert_less_than_thousand(num, is_thousand=False):
        if num == 0:
            return ''
        res = []
        hundred = num // 100
        if hundred > 0:
            res.append(hundreds[hundred])
        num %= 100
        if 10 <= num < 20:
            res.append(teens[num - 10])
        else:
            ten = num // 10
            if ten > 0:
                res.append(tens[ten])
            unit = num % 10
            if unit > 0:
                if is_thousand:
                    if unit == 1:
                        res.append('одна')
                    elif unit == 2:
                        res.append('две')
                    else:
                        res.append(units[unit])
                else:
                    res.append(units[unit])
        return ' '.join(res)
    
    parts = []
    million = n // 1000000
    if million > 0:
        parts.append(convert_less_than_thousand(million) + ' ' + get_plural(million, millions))
    n %= 1000000
    
    thousand = n // 1000
    if thousand > 0:
        parts.append(convert_less_than_thousand(thousand, True) + ' ' + get_plural(thousand, thousands))
    n %= 1000
    
    if n > 0:
        parts.append(convert_less_than_thousand(n))
    
    return ' '.join(parts).strip()

def get_plural(n, forms):
    if n % 10 == 1 and n % 100 != 11:
        return forms[1]
    elif 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
        return forms[2]
    else:
        return forms[3]

n = int(input("Введите число (до 900 000 000): "))
print(number_to_words(n))
