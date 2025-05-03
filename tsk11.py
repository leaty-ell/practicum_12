cities = input("Введите названия городов через пробел: ").split()
winner = "Петя"  # По умолчанию победитель Петя

for i in range(1, len(cities)):
    prev_city = cities[i-1].lower()
    current_city = cities[i].lower()
    
    if current_city[0] != prev_city[-1]:
        winner = "Вася" if i % 2 == 0 else "Петя"
        break
else:
    winner = "Вася" if len(cities) % 2 == 0 else "Петя"

print("Победитель:", winner)
