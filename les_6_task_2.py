# Вариант 2

from random import randint
from collections import Counter
import sys

def __most_common__(n):
    massive = [randint(0, n) for i in range(n)]
    print(massive)
    print(sys.getrefcount(massive))
    print(sys.getsizeof(massive))
    occurence_count = Counter(massive)
    print(sys.getrefcount(occurence_count))
    print(sys.getsizeof(occurence_count))
    return occurence_count.most_common(1)[0][0]


counter = int(input('Введите размерность массива: '))
print(__most_common__(counter))

