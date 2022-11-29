# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму
# элементов списка, стоящих на нечётной позиции.

QUANTITY = 10 # уменьшить для простоты
user_list = [int(input('Введите число.\n')) for i in range(QUANTITY)] # Если чисел много, то консоль уплывает и список получается ненаглядным
print(userlist) # поэтому напишем список
result_graphic = []
for i in range(len(userlist)):
    if i % 2 != 0:
        result_graphic.append('^'.center(len(str(userlist[i])) - 2))
    else:
        result_graphic.append(' ' * (len(str(userlist[i])) - 2))
print(result_graphic) # и пометим элементы, имеющие нечётный индекс
result_list = sum([userlist[i] for i in range(len(userlist)) if i % 2 != 0]) # просуммируем их
print(result_list)