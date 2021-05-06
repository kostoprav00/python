# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# Задача: Определить, какое число в массиве встречается чаще всего.
# Вариант 1
# Вывод: Самый оптимальный вариант в задаче les_6_task_2 с использованием встроенной коллекции - 588 байт
# На втором месте задача les_6_task_3 с использованием хэшируемого маппинга  - 628 байт
# Самый худший случай в задаче les_6_task_1 996 байт, поскольку count(item) перебирает каждый элемент массива
# При тестировании значение n = 10
# Версия и разрядность ОС: "Linux Mint 19.2 Tina" x64
# интерпретатора Python: Python 3.6.8

import sys
from random import randint

n = int(input('Введите количество чисел в массиве: '))
massive = [randint(0, n) for i in range(n)]
massive_unique = set(massive)
most_common_number = 0
count = 0

for item in massive_unique:
    a = massive.count(item)
    if a > count:
        count = a
        most_common_number = item

sum_size_var = 0
sum_size_var += sys.getsizeof(n)
sum_size_var += sys.getsizeof(massive)
sum_size_var += sys.getsizeof(massive_unique)
sum_size_var += sys.getsizeof(most_common_number)
sum_size_var += sys.getsizeof(count)
print('Переменные занимают', sum_size_var)
