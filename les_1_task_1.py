inputValue = 1233#int(input('Введите трехзначное число'))
if inputValue not in range(100, 999):
    print('Это не трехзначное число!')
    exit(1)

hundreds = int((inputValue % 1000 - inputValue % 100) / 100)
decades = int((inputValue % 100 - inputValue % 10) / 10)
units = int(inputValue % 10)
print('Сумма: ' + str(hundreds + units + decades))
print('Произведение: ' + str(hundreds * units * decades))