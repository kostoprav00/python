# По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
# составленного из этих отрезков.
# https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&page-id=-UTIrcHMV39qAqkq9ub9&title=Untitled%20Diagram.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1K7kdcwn2_RUpaV1TjmCOOgc8GFbwAj_w%26export%3Ddownload

a = int(input('Введите длину первого отрезка:'))
b = int(input('Введите длину второго отрезка:'))
c = int(input('Введите длину третьего отрезка:'))

if a + b > c and a + c > b and b + c > a:
    print('Проверка прошла успешно')
    if a == b == c:
        print('Треугольник равносторонный')
    elif a == b or b == c or c == a:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')
else:
    print('Треугольник не существует')
