# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
# https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&page-id=-UTIrcHMV39qAqkq9ub9&title=Untitled%20Diagram.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1K7kdcwn2_RUpaV1TjmCOOgc8GFbwAj_w%26export%3Ddownload

inputValue = int(input('Введите трехзначное число'))
if inputValue not in range(100, 999):
    print('Это не трехзначное число!')
    exit(1)

hundreds = int((inputValue % 1000 - inputValue % 100) / 100)
decades = int((inputValue % 100 - inputValue % 10) / 10)
units = int(inputValue % 10)
print('Сумма: ' + str(hundreds + units + decades))
print('Произведение: ' + str(hundreds * units * decades))
