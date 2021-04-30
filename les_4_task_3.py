# Вариант 3
# Вывод: быстрее всех работает программа с кортежем,
# средняя производительность - с использованием коллекции,
# худшая - мой первый код с массивом
import cProfile
import timeit


def most_common(n):
    from random import randint
    massive = [randint(0, n) for i in range(n)]

    def common(a_list: list) -> tuple:
        max_tuple = (0, a_list[0])
        for element in a_list:
            count = a_list.count(element)
            if count > max_tuple[0]:
                max_tuple = (count, element)
        return max_tuple


# counts = most_common(massive)
# print('Чаще всех повторяется: %d, число повторений: %d' % (counts[1], counts[0]))

print(timeit.timeit('most_common(10)', number=1000, globals=globals()))  # 0.010236029047518969
print(timeit.timeit('most_common(100)', number=1000, globals=globals()))  # 0.07246048515662551
print(timeit.timeit('most_common(1000)', number=1000, globals=globals()))  # 0.7593235580716282
print(timeit.timeit('most_common(10000)', number=1000, globals=globals()))  # 8.12065843702294
cProfile.run('most_common(10000)')

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.016    0.016 <string>:1(<module>)
#         1    0.000    0.000    0.016    0.016 les_4_task_3.py:6(most_common)
#         1    0.002    0.002    0.016    0.016 les_4_task_3.py:8(<listcomp>)
#     10000    0.004    0.000    0.006    0.000 random.py:238(_randbelow_with_getrandbits)
#     10000    0.005    0.000    0.011    0.000 random.py:291(randrange)
#     10000    0.003    0.000    0.014    0.000 random.py:335(randint)
#         1    0.000    0.000    0.016    0.016 {built-in method builtins.exec}
#     10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     16283    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
