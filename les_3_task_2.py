# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

import random

massive = random.sample(range(-100, 100), 10)
print('Массив:', massive)

max_negative_value = -100
index_of_value = -1

for index, value in enumerate(massive, 1):
    if 0 > value > max_negative_value:
        max_negative_value = value
        index_of_value = index

if index_of_value == -1:
    print('Отрицательных элементов не нашлось')
else:
    print('Максимальный отрицательный элемент:', max_negative_value, 'стоит на позиции:', index_of_value)
