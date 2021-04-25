# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

massive = random.sample(range(100), 10)
print('Массив:', massive)

min_index = 0
max_index = 0

min_value = massive[0]
max_value = massive[0]
for index, value in enumerate(massive):
    if value > max_value:
        max_value = value
        max_index = index
    elif value < min_value:
        min_value = value
        min_index = index
print('Минимальный и максимальный элемент: ', min_value, 'и', max_value)

if min_index > max_index:
    min_index, max_index = max_index, min_index

summ = 0
for i in range(min_index + 1, max_index):
    summ += massive[i]
print('Сумма находящихся между ними элементов:', summ)
