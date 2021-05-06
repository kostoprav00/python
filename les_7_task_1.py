# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.

from random import randint

n = int(input('Введите количество чисел в массиве: '))
generated_array = [randint(-100, 100) for i in range(0, n)]
print(generated_array)


def bubble(array):
    for run in range(n - 1):
        for i in range(n - 1 - run):  # -run убираем сравнение с уже найденными пузырьками
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
    return array


print(bubble(generated_array))
# print(sorted(generated_array))
