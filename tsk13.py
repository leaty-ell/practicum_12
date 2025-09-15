k = 1
while True:
    ticket = input("Введите номер билета: ")
    
    if len(ticket) % 2 == 0:
        half = len(ticket) // 2
        sum1 = sum(int(d) for d in ticket[:half])
        sum2 = sum(int(d) for d in ticket[half:])
        
        if sum1 == sum2:
            print(f"Счастливый билет найден! Его порядковый номер: {k}")
            break
    k += 1  
