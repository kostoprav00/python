#  В программе генерируется случайное целое число от 0 до 100.
#  Пользователь должен его отгадать не более чем за 10 попыток.
#  После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число,
#  чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.
# https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Lesson2.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1CmR3AtEvtXxLKTpqLGRT-3RSQKPQAYKr%26export%3Ddownload

import random


secret = round(random.randrange(0, 100))
i = 1
print("Отгадайте число в 10 попыток")
while i <= 10:
    attempt = int(input('Вводите: '))
    if attempt > secret:
        print('Нужно меньше')
    elif attempt < secret:
        print('Нужно больше')
    else:
        print('Вы угадали')
        break
    i += 1
else:
    print('Неудача. Было загадано число:', secret)