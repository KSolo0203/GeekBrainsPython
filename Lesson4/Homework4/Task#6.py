# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.(Вывод тех элементов,
# которые были без повторов).

user_input = input('Вводите числа через пробел, затем нажмите ENTER.\n')
user_num_list = [int(num) for num in user_input.split()]

result_list = [element for element in user_num_list if user_num_list.count(element) < 2]
print(result_list)