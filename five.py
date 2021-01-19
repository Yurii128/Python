revenue = int(input('Выручка'))
costs = int(input('Издержки'))
result = revenue - costs
profitability = result / revenue
if result >= 1:
    print('Отлично! Мы в плюсе!')
    print('Заработали', result, 'денег')
    print('Рентабельность', f"{result / revenue:.2f}")
if result <= -1:
    print('Дело дрянь! Мы в минусе!', f"{result:.2f}", 'денег')
if result == 0:
    print("Будем считать что мы волонтеры")
if result >= 1:
    personnel = int(input('Сколько человек в штате?'))
    print(f"{result / personnel:.2f}", 'прибыли от одного сотрудника')
    
