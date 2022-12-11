#  Создайте программу для игры в "Крестики-нолики".

import os
import time
from random import randint

def collect_players_names():
    return [name.capitalize() for name in input('Играют два человека. Введите имена игроков через пробел.\n').split()]

def interface_grid(field):
    os.system('cls')
    print('-' * 13)
    for i in range(0,int(DEFAULT_GRID ** 0.5)):
        print(f'| {field[3 * i]} | {field[1 + 3 * i]} | {field[2 + 3 * i]} |')
    print('-' * 13)

def start_turn(players):
    while True:
        os.system('cls')
        try:
            user_inp = int(input(f'Кто ходит первым, т.е. крестиками?\n1. {players[0]}\n2. {players[1]}.\n3. Определить случайным образом.\n'))
            time.sleep(READING_T)
            if user_inp == 3:
                user_inp = rand_start()
            if user_inp == 1:
                return players
            elif user_inp == 2:
                players[1], players[0] = players[0], players[1]
                return players
            else:
                raise ValueError 
        except ValueError:
            print(f'Нажмите цифру\n')
            time.sleep(READING_T)

def rand_start():
    return randint(1,2)

def player_turn(player):
    global grid
    mark = 'X' if turn_switch == 0 else 'O'
    while True:
        try:
            user_inp = int(input((f'Ваш ход, {player}. В какую клетку ставим {mark}?\n')))
            if 0 < user_inp <= DEFAULT_GRID and grid[user_inp - 1] not in 'XO':
                time.sleep(READING_T)
                grid[user_inp - 1] = mark
                break
            else:
                raise ValueError
        except ValueError:
            print(f'Введите цифру от 1 до {DEFAULT_GRID}. При этом клетка должна быть свободна!\n')
            time.sleep(READING_T)
            os.system('cls') 
            interface_grid(grid)
            

def winner(field):
    for a,b,c in COMBINATIONS:
        if field[a] == field[b] == field[c]: 
            return True
    return False

DEFAULT_GRID = 9 #  размер поля
COMBINATIONS = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
READING_T = 2 # задержка на прочитать для пользователя

grid = [str(i) for i in range(1, DEFAULT_GRID + 1)]

os.system('cls')
players = start_turn(collect_players_names())
os.system('cls')

turn_counter = 0

while True:
    turn_switch = turn_counter % 2
    interface_grid(grid)
    player_turn(players[turn_switch])
    if winner(grid):
        interface_grid(grid)
        print(f'Поздравляю, {players[turn_switch]}, вы победили!\n')
        exit()
    if turn_counter == 8:
        interface_grid(grid)
        print(f'Победила дружба!\n')
        exit()
    turn_counter += 1