secret = input("Введите загаданное 4-значное число: ")
print("\n" * 25)  
# У игрока 10 попыток
for attempt in range(1, 11):
    guess = input(f"Попытка {attempt}. Введите ваш вариант: ")
    
    bulls = 0
    cows = 0
    
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    
    print(f"Быков: {bulls}, Коров: {cows}")
    
    if bulls == 4:
        print("Победа! Вы угадали число!")
        break
else:
    print(f"Проигрыш! Загаданное число было: {secret}")
