cities = input("Введите названия городов через пробел: ").split()


winner = "Петя" # По умолчанию (Петя) победит

for i in range(1, len(cities)):
    previous_city = cities[i - 1].lower() 
    current_city = cities[i].lower()       


    if current_city[0] != previous_city[-1]:
        # Если правило нарушено, выигрывает другой игрок
        # Петя ходит первым (нечётные ходы), Вася ходит вторым (чётные ходы)
        if i % 2 == 0:
            winner = "Вася"
        else:
            winner = "Петя"
        break
else:
    # Если правила соблюдаются, определяем победителя по количеству ходов
    if len(cities) % 2 == 0:
        winner = "Вася"
    else:
        winner = "Петя"

print(winner)
