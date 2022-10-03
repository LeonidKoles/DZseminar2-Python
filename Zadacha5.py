# Задание 5 Реализуйте алгоритм перемешивания списка.
n = int(input('Введите размер списка '))
import random

ar = []

for i in range(n):
    ar.append(random.randint(-5 , 5))
print(f'Исходный список {ar}')

for i in range(len(ar) - 1, 0, -1):
    j = random.randint(0, i + 1)
    ar[i], ar[j] = ar[j], ar[i]
print(f'Перемешанный список {ar}')
