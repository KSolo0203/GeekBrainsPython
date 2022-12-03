# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее
# число. В качестве символа-разделителя используйте пробел.

user_input = input('Вводите числа через пробел, затем нажмите ENTER.\n')
user_num_list = [int(num) for num in user_input.split()]
print(max(user_num_list),' ', min(user_num_list))