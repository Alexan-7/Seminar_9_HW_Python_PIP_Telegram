# Создайте Бота для игры с конфетами человек против бота. (Дополнительно)

from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from random import randint as ri

TOKEN = '5896263225:AAFZRyKlavW2uf2RaofxHht_uR47w_6-4bY'
bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN)  # переменная для обновлений чата
dispatcher = updater.dispatcher # мост программы

total_sweet = 120

def start_game(update, context):                       # u - чат,  с - ответы
    context.bot.send_message(update.effective_chat.id, # кому отвечать
    'На столе лежит 120 конфет. За один ход можно забрать не более чем 28 конфет.\nПобедитель - тот, кто съел последние конфеты. В общем, обжора, а не победитель:)')

def restart_game(update, context):
    global total_sweet
    total_sweet = 120
    context.bot.send_message(update.effective_chat.id,
    'На столе опять лежит 120 конфет. За один ход можно забрать не более чем 28 конфет.\nПобедитель - тот, кто съел все конфеты.')

def take_candies(update, context):
    global total_sweet
    take_sweet = int(update.message.text)
    
    while take_sweet > 28 or take_sweet < 0 or take_sweet > total_sweet: # 3-е: не больше, чем осталось
        context.bot.send_message(update.effective_chat.id, F'You can not eat {take_sweet} sweets. Try again from 1 to 28 sweets.')
        return
    
    # у человека нет шансов, поэтому закомментировал
    # if total_sweet - take_sweet == 0:
    #     context.bot.send_message(update.effective_chat.id, "Конфеты закончились, ты выиграл :-)")
    #     return

    # if total_sweet < take_sweet:
    #     context.bot.send_message(update.effective_chat.id, 'Вообще закончились конфеты :-O')
    #     return

    total_sweet -= take_sweet
    context.bot.send_message(update.effective_chat.id, f'On the table {total_sweet} candies.')

    '''
    Умный бот всегда выигрывает: бот берет остаток от деления на 29,
    если остаток от деления не равен нулю. Иначе берет Quantum satis 
    '''
    take_sweet = total_sweet % 29 if total_sweet % 29 != 0 else ri(1, 28)

    if total_sweet <= 28:
        total_sweet = 0
        context.bot.send_message(update.effective_chat.id, 'Бот забрал оставшиеся чупа-чупсы и победил!')

        context.bot.sendmessage(update.effective_chat.id, "Введите /restart для перезапуска игры")
        return

    context.bot.send_message(update.effective_chat.id, f'the bot took {take_sweet} candies. On the table {total_sweet - take_sweet} candies.')

start_handler = CommandHandler('start', start_game)
restart_handler = CommandHandler('restart', restart_game)
message_handler = MessageHandler(Filters.text, take_candies)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(restart_handler)
dispatcher.add_handler(message_handler)

updater.start_polling()
updater.idle()