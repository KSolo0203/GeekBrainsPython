# Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход делает человек. За один ход можно забрать не более чем 28 конфет.
# Победитель - тот, кто оставил на столе 0 конфет.

# a) Добавьте игру против бота
# b) Дополнительно: Подумайте как наделить бота ""интеллектом"" (Теория игр)

import os
import time
from random import randint

def greet():
    print('Добро пожаловать в игру "Не тот гад, кто съел всё, а тот, кто съел последнее"!')
    input()

def start_turn():
    while 1:
        os.system('cls')
        try:
            user_input = int(input('Кто ходит первым?\n1. Я!\n2. Компьютер.\n3. Определить случайным образом.\n'))
            match user_input:
                case 1 | 2:
                    time.sleep(READING_T)
                    os.system('cls')
                    return user_input
                case 3:
                    return randint(1,2)
                case _:
                    raise ValueError 
        except ValueError:
            print(f'Нажмите цифру') 
            time.sleep(READING_T)

def player_turn(player='Игрок'):
    while 1:
        try:
            user_inp = int(input(f'{player}, cколько конфет со стола возьмете в этот ход? (не меньше одной и не больше {min(MAX_QUANTITY, table)})\n'))
            if 0 < user_inp <= min(MAX_QUANTITY, table):
                time.sleep(READING_T)
                os.system('cls')
                return user_inp
            else:
                raise ValueError
        except ValueError:
            print(f'{player}, введите целое число, большее, чем 0, но не большее, чем {min(MAX_QUANTITY, table)}.')
            time.sleep(READING_T)
            os.system('cls')
            print(f'На столе конфет: {table}')

def candies_word(quantity, padej):
    if padej == 1: # конфетки берет компьютер
        if quantity % 10 == 1 and quantity != 11:
            return 'конфету'
        elif quantity % 10 in [2,3,4] and quantity not in [12,13,14]:
            return 'конфеты'
        else:
            return 'конфет'
    else: # просто конфетки лежат
        if quantity % 10 == 1 and quantity != 11:
            return 'конфета'
        elif quantity % 10 in [2,3,4] and quantity not in [12,13,14]:
            return 'конфеты'
        else:
            return 'конфет'

# # Наипростейший бот, забирающий со стола псевдослучайное количество конфет
# def cpu_turn():
#     print('Ход компьютера...')
#     time.sleep(CPU_T)
#     cpu_has_taken = randint(1, min(MAX_QUANTITY,table))
#     print(f'Компьютер взял {cpu_has_taken} {candies_word(cpu_has_taken, 1)}.')
#     time.sleep(READING_T)
#     return cpu_has_taken

# Непобедимый бот, если ходит первым
def cpu_turn():
    print('Ход компьютера...')
    time.sleep(CPU_T)
    cpu_has_taken = table % (MAX_QUANTITY + 1) if table % (MAX_QUANTITY + 1) != 0 else randint(1, min(MAX_QUANTITY,table))
    print(f'Компьютер взял {cpu_has_taken} {candies_word(cpu_has_taken, 1)}.')
    time.sleep(READING_T)
    return cpu_has_taken
    
def turn(player):
    global table
    print(f'На столе {table} {candies_word(table, 0)}.')
    table -= player_turn() if player else cpu_turn()
    os.system('cls')

def winner(table):
    return table <= 0
    
START_QUANTITY = 45 # проверить, чтобы START_QUANTITY % (MAX_QUANTITY + 1) != 0
MAX_QUANTITY = 10
CPU_T = 2 # задержка на подумать для компьютера 
READING_T = 2 # задержка на прочитать для пользователя 

table = START_QUANTITY

os.system('cls')
greet()

if start_turn() == 1:
    turn(1)

while True:
    turn(0)
    if winner(table):
        print('Победил великий компьютер!')
        break
    turn(1)
    if winner(table):
        print('Вы одержали победу! Помните - избыточное потребление сахара вредит вашим зубам!')
        break