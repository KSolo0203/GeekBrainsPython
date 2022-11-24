# Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в
# списке, который вы сами заполняете.

def MultiplyElements(array_factors,indices):
    result = 1
    for x in indices:
        result *= array_factors[x]
    return result

dicunt = int(input('Введите число N.\n'))
diapazon = [n for n in range(-dicunt, dicunt + 1)]
print(diapazon)
dicunt = map(int,input('Элементы под какими индексами умножить? Введите числа через пробел.\n').split())
print(MultiplyElements(diapazon,dicunt))