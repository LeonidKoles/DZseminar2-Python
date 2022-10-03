# Задание 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на 
# экран их сумму, округлённую до трёх знаков после точки.

# Пример: Для n = 6 -> 14.072

print('Задайте размерность списка')
n = int(input())
ar = []

for i in range(1, n + 1):
    i = pow(1 + 1 / i, i)
    ar.append(i)
print(ar)
summ = 0

for i in range(n):
    summ += ar[i]
print(round(summ, 3))