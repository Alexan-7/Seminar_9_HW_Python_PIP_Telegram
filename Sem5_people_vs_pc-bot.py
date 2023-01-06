'''
1) Создайте программу для игры с конфетами человек против бота.
Условие задачи: На столе лежит 120 конфет. Играют два игрока делая ход друг после друга.
Первый ход делает человек. За один ход можно забрать не более чем 28 конфет.
Победитель - тот, кто оставил на столе 0 конфет.
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

2021 21 ---> 2000 бот4 -> 1996 .... бот --->29 --> 27 >> 2конф

a) Добавьте игру против бота

# Доп b) Подумайте как наделить бота ""интеллектом"" (Теория игр)
'''

from random import randint as ri

total_sweet = 120
take_sweet = 0
player_sweet = 0
bot_sweet = 0

def who_is_first():
    random_number = ri(1, 2)
    if random_number == 1:
        player_turn()
    else: 
        bot_turn()

def start_game():
    print('На столе лежит 120 конфет. За один ход можно забрать не более чем 28 конфет.\nПобедитель - тот, кто съел все конфеты.')
    who_is_first()

def player_turn():
    global total_sweet  # чтобы функция пользовалась глобальной переменной
    global take_sweet
    global player_sweet

    print(f'On the table {total_sweet} candies. Your turn')
    take_sweet = int(input('How many sweets you want take?\n'))
    while take_sweet > 28 or take_sweet < 0 or take_sweet > total_sweet: # 3-е: не больше, чем осталось
        take_sweet = int(input(F'You can not eat {take_sweet} sweets. Try again from 1 to 28 sweets: '))
    total_sweet -= take_sweet
    player_sweet += take_sweet
    if total_sweet > 0:
        bot_turn()
    else:
        print(f'We do not have any more candy in the game! You are winning player!')

def bot_turn():
    global total_sweet
    global take_sweet
    global bot_sweet
    '''
    Умный бот всегда выигрывает: бот берет остаток от деления на 29,
    если остаток от деления не равен нулю. Иначе берет Quantum satis 
    '''
    take_sweet = total_sweet % 29 if total_sweet % 29 != 0 else ri(1, 28)
    # take_sweet = ri(1, 28) # строка для глупого бота (вместо предыдущей)
    total_sweet -= take_sweet
    bot_sweet += take_sweet
    print(f'the bot took {take_sweet} candies. On the table {total_sweet} candies.')
    if total_sweet > 0:
        player_turn()
    else:
        print(f'We do not have any more candy in the game! Smart-bot is winning player!')

start_game()