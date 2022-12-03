# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму
# элементов списка, стоящих на нечётной позиции.

QUANTITY = 5 # уменьшить для простоты
user_list = [int(input('Введите число.\n')) for i in range(QUANTITY)] # Если чисел много, то консоль уплывает и список получается ненаглядным
print(user_list) # поэтому напишем список
# result_graphic = []
# for i in range(len(user_list)):
#     if i % 2 != 0:
#         result_graphic.append('^'.center(len(str(user_list[i])) - 2))
#     else:
#         result_graphic.append(' ' * (len(str(user_list[i])) - 2))
# print(result_graphic) # и пометим элементы, имеющие нечётный индекс
result_list = sum([user_list[i] for i in range(len(user_list)) if i % 2 != 0]) # просуммируем их
print(result_list)