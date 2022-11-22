# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

num = int(input("Введите число N\n"))
if num > 0:
    print([i for i in range(-num, num + 1)])
# listofnumbers = []                          
# for i in range(-num, num + 1):
#     listofnumbers.append(i)
# print(listofnumbers)                 тоже самое что строчка 3
else:
    print([i for i in range(num, -num + 1)])