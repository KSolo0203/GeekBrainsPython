# Напишите программу, которая принимает на вход цифру, обозначающую день 
# недели, и проверяет, является ли этот день выходным.

symbol = 0
while symbol == 0:
    try:
        symbol = int(input("Введите цифру, обозначающую день недели. Нажмите Ctrl + C чтобы выйти.\n"))
        if symbol in range(1,6):
            print('Это рабочий день.')
            symbol = 0
            continue
        if symbol in range(6,8):
            print('Это выходной день.')
            symbol = 0
            continue
        else:
            symbol = 0
            print('Nota bene: в неделе всего семь дней.')
    except ValueError:
        print('Вводите цифру!')
