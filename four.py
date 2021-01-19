number = int(input('Введите число: '))
a = -1
while number > 10:
    b = number % 10
    number //= 10
    if b > a:
     a = b
print(a)
