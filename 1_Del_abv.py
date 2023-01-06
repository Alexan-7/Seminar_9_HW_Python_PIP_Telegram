# Напишите Бота, удаляющего из текста все слова, содержащие "абв". (Ввод от пользователя)

from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

bot = Bot(token='5946892419:AAH0prsFwMOOcBZA1rmc8dfsciKUoybJEP8')
updater = Updater(token='5946892419:AAH0prsFwMOOcBZA1rmc8dfsciKUoybJEP8')
dispatcher = updater.dispatcher

def del_abv_V1(update, context):
    text = update.message.text.split() # делим сообщение по пробелам
    list1 = []                         # вспомогательный список для элементов без "абв"
    for i in text:
        if "абв" not in i:
            list1.append(i)
    context.bot.send_message(update.effective_chat.id, " ".join(list1)) # отправляем сообщение человеку


def del_abv_V2(update, context):
    text = update.message.text.split()
    list1 = []
    for i in text:
        if "абв" not in i:
            list1.append(i)
    context.bot.send_message(update.effective_chat.id, " ".join(list1[1:]))

hand_com = CommandHandler("filter", del_abv_V2)        # вариант с командой
del_handler = MessageHandler(Filters.text, del_abv_V1) # вариант с сообщением
dispatcher.add_handler(del_handler)
dispatcher.add_handler(hand_com)

updater.start_polling()
updater.idle()