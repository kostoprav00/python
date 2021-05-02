# Вариант 2
import cProfile
import timeit
from collections import Counter


def __most_common__(n):
    from random import randint
    massive = [randint(0, n) for i in range(n)]
    occurence_count = Counter(massive)
    return occurence_count.most_common(1)[0][0]


print(timeit.timeit('__most_common__(10)', number=1000, globals=globals()))
print(timeit.timeit('__most_common__(100)', number=1000, globals=globals()))
print(timeit.timeit('__most_common__(1000)', number=1000, globals=globals()))
print(timeit.timeit('__most_common__(10000)', number=1000, globals=globals()))
cProfile.run('__most_common__(10000)')

# 0.033759685000404716
# 0.17398883499845397
# 1.6951854799990542
# 18.20053947999986
#          56369 function calls in 0.025 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.025    0.025 <string>:1(<module>)
#         1    0.000    0.000    0.001    0.001 __init__.py:540(__init__)
#         1    0.000    0.000    0.000    0.000 __init__.py:559(most_common)
#         1    0.000    0.000    0.001    0.001 __init__.py:608(update)
#         1    0.000    0.000    0.000    0.000 abc.py:96(__instancecheck__)
#         1    0.000    0.000    0.000    0.000 heapq.py:521(nlargest)
#         1    0.000    0.000    0.025    0.025 les_4_task_2.py:7(__most_common__)
#         1    0.003    0.003    0.024    0.024 les_4_task_2.py:9(<listcomp>)
#     10000    0.008    0.000    0.017    0.000 random.py:200(randrange)
#     10000    0.004    0.000    0.021    0.000 random.py:244(randint)
#     10000    0.006    0.000    0.008    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
#         1    0.001    0.001    0.001    0.001 {built-in method _collections._count_elements}
#         1    0.000    0.000    0.025    0.025 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.iter}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#     10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     16353    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
#         1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}