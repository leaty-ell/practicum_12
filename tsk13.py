ticket = input("Введите номер билета: ")
while True:
    if len(ticket) % 2 == 0:
        half = len(ticket) // 2
        sum1 = sum(int(d) for d in ticket[:half])
        sum2 = sum(int(d) for d in ticket[half:])
        if sum1 == sum2:
            print("Счастливый билет найден!")
            break
    ticket = input("Введите следующий номер билета: ")
