# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
# https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&page-id=-UTIrcHMV39qAqkq9ub9&title=Untitled%20Diagram.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1K7kdcwn2_RUpaV1TjmCOOgc8GFbwAj_w%26export%3Ddownload

a = int(input('Введите первое число:'))
b = int(input('Введите второе число:'))
c = int(input('Введите третье число:'))

if a > b:
    if b > c:
        print(b)
    elif a > c:
        print(c)
    else:
        print(a)
else:
    if a > c:
        print(a)
    elif b > c:
        print(c)
    else:
        print(b)
