# Проанализировать скорость и сложность одного любого алгоритма из
# разработанных в рамках домашнего задания первых трех уроков.
# Задача: Определить, какое число в массиве встречается чаще всего.
# Вариант 1

import cProfile
import timeit


def most_common(n):
    from random import randint
    massive = [randint(0, n) for i in range(n)]
   # print('Массив:', massive)
    massive_unique = set(massive)
    most_common_number = 0
    count = 0
    for item in massive_unique:
        a = massive.count(item)
        if a > count:
            count = a
            most_common_number = item
    return most_common_number


print(timeit.timeit('most_common(10)', number=1000, globals=globals()))  # 0.01062618987634778
print(timeit.timeit('most_common(100)', number=1000, globals=globals()))  # 0.07685210602357984
print(timeit.timeit('most_common(1000)', number=1000, globals=globals()))  # 0.7851381241343915
print(timeit.timeit('most_common(10000)', number=1000, globals=globals()))  # 8.558316830080003
cProfile.run('most_common(10000)')

# 0.030584333999286173
# 0.3087645049999992
# 14.406143035999776
# 1284.9540479379993
#          62693 function calls in 1.334 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    1.334    1.334 <string>:1(<module>)
#         1    0.004    0.004    1.334    1.334 les_4_task_1.py:10(most_common)
#         1    0.003    0.003    0.027    0.027 les_4_task_1.py:12(<listcomp>)
#     10000    0.010    0.000    0.019    0.000 random.py:200(randrange)
#     10000    0.005    0.000    0.024    0.000 random.py:244(randint)
#     10000    0.007    0.000    0.009    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    1.334    1.334 {built-in method builtins.exec}
#     10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#      6304    1.303    0.000    1.303    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     16384    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}
