# Вариант 2

import sys
from random import randint
from collections import Counter

n = int(input('Введите количество чисел в массиве: '))
massive = [randint(0, n) for i in range(n)]
occurrence_cnt = Counter(massive)
occurrence_cnt.most_common(1)[0][0]



sum_size_var = 0
sum_size_var += sys.getsizeof(n)
sum_size_var += sys.getsizeof(massive)
sum_size_var += sys.getsizeof(occurrence_cnt)
print('Переменные занимают', sum_size_var)
