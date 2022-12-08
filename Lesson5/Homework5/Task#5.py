#  Создайте программу для игры в "Крестики-нолики".

import numpy as np
import os
import time
from random import randint

def collect_players_names():
    return [name.capitalize() for name in input('Играют два человека. Введите имена игроков через пробел.\n').split()]

def Turn():
    pass

def start_turn(players):
    select = 0
    while select == 0:
        os.system('cls')
        print(f'Кто ходит первым, т.е. крестиками?\n1. {players[0]}\n2. {players[1]}.\n3. Определить случайным образом.')
        try:
            user_inp = input()
            if user_inp in '12':
                select = int(user_inp)
                time.sleep(READING_T)
                os.system('cls')
                return select
            elif user_inp == '3':
                select = rand_start()
                return select
            else:
                raise ValueError 
        except ValueError:
            print(f'Нажмите цифру')
            time.sleep(READING_T)

def rand_start():
    return randint(1,2)

def player_turn():
    quantity = 0
    while quantity == 0:
        print(f'Сколько конфет со стола возьмете в этот ход? (не меньше одной и не больше {MAX_QUANTITY})')
        try:
            user_inp = int(input())
            if 0 < user_inp <= MAX_QUANTITY:
                quantity = user_inp
                time.sleep(READING_T)
                os.system('cls')
                return quantity
            else:
                raise ValueError
        except ValueError:
            print(f'Введите целое число, большее, чем 0, но не большее, чем {MAX_QUANTITY}.')
            time.sleep(READING_T)
            os.system('cls')
            global field
            print(f'На столе конфет: {field}')

# Наипростейший бот, забирающий со стола псевдослучайное количество конфет
# def cpu_turn():
#     print('Ход компьютера...')
#     time.sleep(CPU_T)
#     return randint(1,MAX_QUANTITY)

# Бот с интеллектом
# def cpu_turn():
#     print('Ход компьютера...')
#     time.sleep(CPU_T)
#     for i in range(1, MAX_QUANTITY):
#         if table <= MAX_QUANTITY:
#             return table
#         elif not table / MAX_QUANTITY % 2:
#             return MAX_QUANTITY - 1
#         elif table / MAX_QUANTITY % 2:
#             return MAX_QUANTITY
#         elif (table - i) % (table // (MAX_QUANTITY + 1)) != 0 and \
#              (table // (MAX_QUANTITY)) % 2 != 0:
#             return i
#         else:
#             return randint(1,MAX_QUANTITY)
    
def turn(player):
    global field
    print(f'{field}')
    player_turn(player)
    os.system('cls')

def winner(field):
    for i in range(len(field[0])):
        if all(field[i]) == 'X':
            return True
        # elif np.all([field[0,0],field[1,1],field[2,2]] == 'X'):
        #     return True
    return False

START_FIELD = (3,3) #  размер поля
READING_T = 2 # задержка на прочитать для пользователя
CPU_T = 2 # задержка на подумать для компьютера 

field = [['...' for i in range(START_FIELD[0])] for k in range(START_FIELD[1])]

print(field)
print(winner(field))
field[1][1] = 'X'
print(field)
print(winner(field))


# players = collect_players_names()

# os.system('cls')
# if start_turn(players) == 1:
#     turn(players[0])

# while True:
#     for player in players:
#         turn(player)
#         if winner(field):
#             print(f'Поздравляю, {player}б вы победили!')
#             exit()