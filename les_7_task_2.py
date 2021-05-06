# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

# Алгоритм с Википедии:
# Для решения задачи сортировки эти три этапа выглядят так:
#     1.Сортируемый массив разбивается на две части примерно одинакового размера;
#     2.Каждая из получившихся частей сортируется отдельно, например — тем же самым алгоритмом;
#     3.Два упорядоченных массива половинного размера соединяются в один.
# 1.1. — 2.1. Рекурсивное разбиение задачи на меньшие происходит до тех пор,
# пока размер массива не достигнет единицы (любой массив длины 1 можно считать упорядоченным).
# 3.1. Соединение двух упорядоченных массивов в один.
# Основную идею слияния двух отсортированных массивов можно объяснить на следующем примере.
# Пусть мы имеем два уже отсортированных по возрастанию подмассива. Тогда:
# 3.2. Слияние двух подмассивов в третий результирующий массив.
# На каждом шаге мы берём меньший из двух первых элементов подмассивов и записываем его в результирующий массив.
# Счётчики номеров элементов результирующего массива и подмассива, из которого был взят элемент, увеличиваем на 1.
# 3.4. «Прицепление» остатка.
# Когда один из подмассивов закончился, мы добавляем все оставшиеся элементы второго подмассива
# в результирующий массив.

from random import uniform

n = int(input('Введите количество чисел в массиве: '))
generated_array = [uniform(0, 50) for i in range(0, n)]
print(generated_array)


def merge_sort(array):  # функция выполняет сортировку слиянием
    if len(array) == 1:
        return array
    middle = len(array) // 2
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])
    return merge_two_lists(left, right)


def merge_two_lists(a, b):  # функция объединяет два списка
    result = []  # кладём сюда уже отсортированные списки
    i = j = 0  # указатели
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    if i < len(a):
        result += a[i:]
    if j < len(b):
        result += b[j:]
    return result


print(merge_sort(generated_array))
# print(sorted(generated_array))
