# Задание 1 Напишите программу, которая принимает на вход вещественное число и 
# показывает сумму его цифр.

# Пример:

# 6782 -> 23
# 0,56 -> 11


print('Введите число ')
n = input()
summ = 0


for i in str(n):
    if i != '.':
        summ += int(i)

print(f'Сумма чисел равна: {summ}')