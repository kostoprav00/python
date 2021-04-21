# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
# https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Lesson2.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1CmR3AtEvtXxLKTpqLGRT-3RSQKPQAYKr%26export%3Ddownload

input_value = int(input('Введите целое число: '))
init = input_value
count_even: int = 0
count_odd: int = 0
while input_value > 0:
    if input_value % 2 == 0:
       count_even += 1
    else:
       count_odd += 1
    input_value = input_value // 10

print('У числа ' + str(init) + ' количество чётных цифр: ' + str(count_even) + ' и количество нечётных цифр: '
      + str(count_odd))
