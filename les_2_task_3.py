# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
# https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Lesson2.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1CmR3AtEvtXxLKTpqLGRT-3RSQKPQAYKr%26export%3Ddownload

def counter(digit):
    number = int(input('Введите целое число: '))
    count = 0
    while number > 0:
        cut_number = number % 10
        number = number // 10
        if digit == cut_number:
            count += 1
    return count


def recursive_counter(count_number):
    if count_number == 0:
        return 0
    return counter(input_digit) + recursive_counter(count_number - 1)


count_numbers = int(input('Введите количество чисел: '))
input_digit = int(input('Введите цифру для поиска: '))
if 0 <= input_digit < 10:
    print('Цифра "' + str(input_digit) + '" во всех введенных числах встречается: '
          + str(recursive_counter(count_numbers)) + ' раз.')
else:
    print('Некорретный ввод цифры')
