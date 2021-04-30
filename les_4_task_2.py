# Вариант 2
import cProfile
import timeit


def most_common(n):
    from collections import Counter
    from random import randint
    massive = [randint(0, n) for i in range(n)]

    # print('Массив:', massive)

    def most_frequent(massive):
        occurence_count = Counter(massive)
        return occurence_count.most_common(1)[0][0]


# print('Самое частое число в массиве: ', most_frequent(massive))

print(timeit.timeit('most_common(10)', number=1000, globals=globals()))  # 0.012099198065698147
print(timeit.timeit('most_common(100)', number=1000, globals=globals()))  # 0.07788456113263965
print(timeit.timeit('most_common(1000)', number=1000, globals=globals()))  # 0.7620219350792468
print(timeit.timeit('most_common(10000)', number=1000, globals=globals()))  # 8.166030570166185
cProfile.run('most_common(10000)')

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1033(_handle_fromlist)
#         1    0.000    0.000    0.016    0.016 <string>:1(<module>)
#         1    0.000    0.000    0.016    0.016 les_4_task_2.py:6(most_common)
#         1    0.002    0.002    0.016    0.016 les_4_task_2.py:9(<listcomp>)
#     10000    0.005    0.000    0.006    0.000 random.py:238(_randbelow_with_getrandbits)
#     10000    0.005    0.000    0.011    0.000 random.py:291(randrange)
#     10000    0.003    0.000    0.014    0.000 random.py:335(randint)
#         1    0.000    0.000    0.016    0.016 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
#     10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     16332    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
