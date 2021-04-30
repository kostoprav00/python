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

#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.017    0.017 <string>:1(<module>)
#         1    0.000    0.000    0.017    0.017 les_4_task_1.py:10(most_common)
#         1    0.002    0.002    0.016    0.016 les_4_task_1.py:12(<listcomp>)
#     10000    0.004    0.000    0.006    0.000 random.py:238(_randbelow_with_getrandbits)
#     10000    0.005    0.000    0.011    0.000 random.py:291(randrange)
#     10000    0.003    0.000    0.014    0.000 random.py:335(randint)
#         1    0.000    0.000    0.017    0.017 {built-in method builtins.exec}
#     10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     16589    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
