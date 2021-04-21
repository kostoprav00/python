# Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. Выполнить над числом 5 побитовый сдвиг
# вправо и влево на два знака.
# https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&page-id=-UTIrcHMV39qAqkq9ub9&title=Untitled%20Diagram.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1K7kdcwn2_RUpaV1TjmCOOgc8GFbwAj_w%26export%3Ddownload

a = 5
b = 6
print("Побитовое И чисел 5 и 6 :" + str(5 & 6))
print("Побитовое ИЛИ чисел 5 и 6 :" + str(5 | 6))
print("Побитовое искючающее ИЛИ чисел 5 и 6 :" + str(5 ^ 6))
print("Cдвиг влево числа 5 на 2 знака :" + str(5 << 2))
print("Cдвиг вправл числа 5 на 2 знака :" + str(5 >> 2))
