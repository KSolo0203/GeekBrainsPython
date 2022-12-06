# Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход делает человек. За один ход можно забрать не более чем 28 конфет.
# Победитель - тот, кто оставил на столе 0 конфет.

import os
import time
from random import randint

def collect_players_names():
    return [name for name in input('Играют два человека. Введите имена игроков через пробел.\n').split()]

def start_turn(players):
    select = 0
    while select == 0:
        os.system('cls')
        print(f'Кто ходит первым?\n1. {players[0]}\n2. {players[1]}.\n3. Определить случайным образом.')
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

def player_turn(player):
    quantity = 0
    while quantity == 0:
        print(f'{player}, cколько конфет со стола возьмете в этот ход? (не меньше одной и не больше {MAX_QUANTITY})')
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
            print(f'{player}, введите целое число, большее, чем 0, но не большее, чем {MAX_QUANTITY}.')
            time.sleep(READING_T)
            os.system('cls')
            global table
            print(f'На столе конфет: {table}')

def cpu_turn():
    print('Ход компьютера...')
    time.sleep(CPU_T)
    return randint(1,MAX_QUANTITY)

def turn(player):
    global table
    print(f'На столе конфет: {table}')
    table -= player_turn(player)
    os.system('cls')

def winner(table):
    return table <= 0
    
START_QUANTITY = 21
MAX_QUANTITY = 7
CPU_T = 2 # задержка на подумать для компьютера 
READING_T = 1 # задержка на прочитать для пользователя 

table = START_QUANTITY
players = collect_players_names()

os.system('cls')
if start_turn(players) == 1:
    turn(players[0])

while True:
    turn(players[1])
    if winner(table):
        print(f'Вы одержали победу, {players[1]}! Помните - избыточное потребелние сахара вредит вашим зубам!')
        break
    
    turn(players[0])
    if winner(table):
        print(f'Вы одержали победу, {players[0]}! Помните - избыточное потребелние сахара вредит вашим зубам!')
        break
