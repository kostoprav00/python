# Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
from collections import *


def check_and_get_number_as_16digit_deque(number: str) -> deque:
    raw_deque = deque(number.upper())
    for digit in raw_deque:
        if not ('0' <= digit < 'G') or digit in ';<=>?@':
            print(number + ' не 16-ричное число')
            exit(0)
    return raw_deque


def get_sum(digit1: str, digit2: str, remainder: int) -> (str, int):
    num1: int = int(hex_digit_dict.get(digit1, digit1))
    num2: int = int(hex_digit_dict.get(digit2, digit2))
    sum_digits = num1 + num2 + remainder
    if sum_digits > 15:
        diff = sum_digits - 16
        remainder = 1
        return dec_digit_dict.get(diff, str(diff)), remainder
    remainder = 0
    return str(dec_digit_dict.get(sum_digits, str(sum_digits))), remainder


def get_digit(deque_16digit: deque) -> str:
    if len(deque_16digit) == 0:
        return '0'
    return deque_16digit.pop()


def sum_16digits(hex_digit_1: deque, hex_digit_2: deque) -> list:
    max_len = max(len(hex_digit_1), len(hex_digit_2))
    remainder = 0
    sum_result = list()
    for i in range(0, max_len):
        result = get_sum(get_digit(hex_digit_1), get_digit(hex_digit_2), remainder)
        sum_result.append(result[0])
        remainder = result[1]
    if remainder == 1:
        sum_result.append('1')
    sum_result.reverse()
    return sum_result


hex_digit_dict = dict({'A': '10', 'B': '11', 'C': '12', 'D': '13', 'E': '14', 'F': '15'})
dec_digit_dict = dict({10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'})
deque_16digit_1 = check_and_get_number_as_16digit_deque(input('Введите первое число: '))
deque_16digit_2 = check_and_get_number_as_16digit_deque(input('Введите второе число: '))
print(deque_16digit_1)
print(deque_16digit_2)
print(sum_16digits(deque_16digit_1, deque_16digit_2))
