# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# Задача: Определить, какое число в массиве встречается чаще всего.
# Вариант 1

from random import randint

massive = [randint(0, 6) for i in range(10)]
print('Массив:', massive)

massive_unique = set(massive)

most_common_number = 0
count = 0

for item in massive_unique:
    a = massive.count(item)
    if a > count:
        count = a
        most_common_number = item

print('Самое частое число в массиве: ', most_common_number)



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




