# Определить, является ли год, который ввел пользователь, високосным или не високосным.
# https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&page-id=-UTIrcHMV39qAqkq9ub9&title=Untitled%20Diagram.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1K7kdcwn2_RUpaV1TjmCOOgc8GFbwAj_w%26export%3Ddownload

inputYear = int(input('Введите год:'))
if inputYear % 4 == 0:
    if inputYear % 100 == 0 and inputYear % 400 != 0:
        print('Невисокосный год')
    else:
        print('Високосный год')
else:
    print('Невисокосный год')
