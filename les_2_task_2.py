# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.
# https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Lesson2.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1CmR3AtEvtXxLKTpqLGRT-3RSQKPQAYKr%26export%3Ddownload

input_value = int(input('Введите целое число:'))
reverse = 0
while input_value > 0:
    reverse = reverse * 10
    reverse = reverse + input_value % 10
    input_value = input_value // 10
print(reverse)
