# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import randint

QUANTITY = 10 
user_list = [randint(3,14) for i in range(QUANTITY)]
print(user_list)
result_list = [user_list[i] * user_list[-i - 1] for i in range(QUANTITY // 2)]
# print(result_list) 
# далее необязательная часть
for i in range(QUANTITY // 2):
    print('{} * {} = {}'.format(user_list[i], user_list[-i - 1], result_list[i]))