# Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться,
# а должна запрашивать новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0'
# в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа
# должна сообщать ему об ошибке и снова запрашивать знак операции. Также сообщать пользователю о невозможности
# деления на ноль, если он ввел 0 в качестве делителя.
# https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Lesson2.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1CmR3AtEvtXxLKTpqLGRT-3RSQKPQAYKr%26export%3Ddownload


def do_math():
    if sign == '+':
        return input_value1 + input_value2
    elif sign == '-':
        return input_value1 - input_value2
    elif sign == '*':
        return input_value1 * input_value2
    elif sign == '/':
        return input_value1 / input_value2
    else:
        return 'Знак некорректен'


while True:
    input_value1 = float(input('Введите первое число:'))
    input_value2 = float(input('Введите второе число:'))
    sign = input('Введите знак операции:')
    if sign == '0':
        break
    if input_value2 == 0:
        print('Деление на ноль невозможно')
        continue
    print(do_math())
