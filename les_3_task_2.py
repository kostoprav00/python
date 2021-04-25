# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

import random

massive = random.sample(range(-100, 100), 10)
print('Массив:', massive)

i = 0
ind = -1

for i in massive:
    if i < 0 and ind == -1:
        ind = massive.index(i)
    elif 0 > i > massive[ind]:
        ind = massive.index(i)
    i += 1
if massive[ind] >= 0:
    print('Отрицательных элементов не нашлось')

else:
    print('Максимальный отрицательный элемент:', massive[ind], 'стоит на позиции:', ind)
