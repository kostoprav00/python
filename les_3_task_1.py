# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

massive = random.sample(range(100), 5)
print('Было:', massive)

_min = massive[0]
_max = massive[0]
for i in massive:
    if i > _max:
        _max = i
    elif i < _min:
        _min = i
min_index = massive.index(_min)
max_index = massive.index(_max)

massive[min_index], massive[max_index] = massive[max_index], massive[min_index]
print('Стало: ')
print(massive)

