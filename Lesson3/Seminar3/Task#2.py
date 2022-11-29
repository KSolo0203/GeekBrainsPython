# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

# list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# list = ["йцу", "фыв", "ячс", "цук", "йцу", "йцу"]
# list = ["йцу", "фыв", "ячс", "цук", "йцукен"]
# list = ["123", "234", 123, "567"]
list = []
               
second_entry = input()
counter = 0
for i in range(len(list)):
    if list[i] == second_entry and counter == 1:
        print(i)
        break
    if list[i] == second_entry and counter == 0:
        counter += 1
else:
    print("-1")

# spisok = ["строка1", "строка2", "строка1", "строка2"]
# find_str = "строка1"
# if spisok.count(find_str) < 2:
#     print("Второго вхождения нет")
# else:
#     spisok.remove(find_str)  #Удаляет первое вхождение
#     print(spisok.index(find_str) + 1)