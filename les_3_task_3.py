# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

massive = [random.randint(0, 10) for i in range(10)]
print('Массив:', massive)

min_value = 6
min_index = 0
min_value2 = 6
min_index2 = 0

for index, value in enumerate(massive):
    if value < min_value:
        min_value = value
        min_index = index

for ind, val in enumerate(massive):
    if min_index == ind:
        continue
    if val < min_value2:
        min_value2 = val

print('%d — первое наимельшее число, %d — второе наименьшее число' % (min_value, min_value2))
