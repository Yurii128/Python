time = int(input('Введите количество секунд: '))
hour = time // 3600
min = (time - hour * 3600) // 60
sec = time % 60
print('{:02};{:02};{:02}'. format(hour, min, sec))