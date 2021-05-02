# Вариант 3
# Вывод: быстрее всех работает программа с каунтером
# худшая - мой первый код с массивом (операция massive.count(item) неоптимальна). Текущая задача на втором месте,
# т.к.немного проигрывает Counter-у из второй задачи

import cProfile
import timeit
from random import randint


def most_common(n: int):
    massive = [randint(0, n) for i in range(n)]
    common_key = massive[0]
    max_occurrence_cnt = 1
    hash_map = dict({common_key: 1})
    for i in range(1, n-1):
        key = massive[i]
        current_key_occurrence_cnt = hash_map.get(key, 0) + 1
        hash_map[key] = current_key_occurrence_cnt
        if current_key_occurrence_cnt > max_occurrence_cnt:
            common_key = key
            max_occurrence_cnt = current_key_occurrence_cnt
    return common_key


print(timeit.timeit('most_common(10)', number=1000, globals=globals()))  # 0.010236029047518969
print(timeit.timeit('most_common(100)', number=1000, globals=globals()))  # 0.07246048515662551
print(timeit.timeit('most_common(1000)', number=1000, globals=globals()))  # 0.7593235580716282
print(timeit.timeit('most_common(10000)', number=1000, globals=globals()))  # 8.12065843702294
cProfile.run('most_common(10000)')

# 0.020967884000128834
# 0.18965445999856456
# 1.9952667990000919
# 21.43944801500038
#          66367 function calls in 0.030 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.030    0.030 <string>:1(<module>)
#         1    0.004    0.004    0.030    0.030 les_4_task_3.py:10(most_common)
#         1    0.003    0.003    0.024    0.024 les_4_task_3.py:11(<listcomp>)
#     10000    0.009    0.000    0.017    0.000 random.py:200(randrange)
#     10000    0.004    0.000    0.021    0.000 random.py:244(randint)
#     10000    0.006    0.000    0.008    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.030    0.030 {built-in method builtins.exec}
#     10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      9998    0.001    0.000    0.001    0.000 {method 'get' of 'dict' objects}
#     16364    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
