# Вариант 3

import sys
from random import randint

n = int(input('Введите количество чисел в массиве: '))
massive = [randint(0, n) for i in range(n)]

common_key = massive[0]
max_occurrence_cnt = 1
hash_map = dict({common_key: 1})

for i in range(1, n - 1):
    key = massive[i]
    current_key_occurrence_cnt = hash_map.get(key, 0) + 1
    hash_map[key] = current_key_occurrence_cnt
    if current_key_occurrence_cnt > max_occurrence_cnt:
        common_key = key
        max_occurrence_cnt = current_key_occurrence_cnt

sum_size_var = 0
sum_size_var += sys.getsizeof(n)
sum_size_var += sys.getsizeof(massive)
sum_size_var += sys.getsizeof(common_key)
sum_size_var += sys.getsizeof(max_occurrence_cnt)
sum_size_var += sys.getsizeof(hash_map)
print('Переменные занимают', sum_size_var)
