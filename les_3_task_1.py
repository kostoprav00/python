# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

massive = random.sample(range(100), 5)
print('Было:', massive)

min_value = massive[0]
max_value = massive[0]
max_index = 0
min_index = 0
for index, value in enumerate(massive):
    if value > max_value:
        max_value = value
        max_index = index
    elif value < min_value:
        min_value = value
        min_index = index

massive[min_index], massive[max_index] = massive[max_index], massive[min_index]
print('Стало: ')
print(massive)
