# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

massive = random.sample(range(100), 10)
print('Массив:', massive)

min1 = 0
min2 = 1

for i in massive:
    if massive[min1] > i:
        min2 = min1
        min1 = massive.index(i)
    elif massive[min2] > i:
        min2 = massive.index(i)

print('%d — первое наимельшее число, %d — второе наименьшее число' % (massive[min1], massive[min2]))