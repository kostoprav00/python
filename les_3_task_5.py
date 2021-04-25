# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

massive = random.sample(range(100), 10)
print('Массив:', massive)

min_ = 0
max_ = 0

for i in massive:
    if i < massive[min_]:
        min_ = massive.index(i)
    elif i > massive[max_]:
        max_ = massive.index(i)
print('Минимальный и максимальный элемент: ', massive[min_], 'и',  massive[max_])

if min_ > max_:
    min_, max_ = max_, min_

summ = 0
for i in range(min_+1, max_):
    summ += massive[i]
print('Сумма находящихся между ними элементов:', summ)
