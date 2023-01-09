# Прикрутить бота к задачам с предыдущего семинара:
# Создать калькулятор для работы с рациональными числами, организовать меню, добавить
# в программу систему логирования (Содержит: дата, имя и id пользователя, ввод, результат).

from telegram import Bot
from telegram.ext import Updater, CommandHandler, ContextTypes, MessageHandler, Filters, ConversationHandler
import logic, logger

A = 0

with open('../token.txt') as token:
    TOKEN = token.readline()

bot = Bot(token=TOKEN)
upd = Updater(token=TOKEN)
dispatcher = upd.dispatcher

def greet(update, context):
    context.bot.send_message(update.effective_chat.id, f'Здравствуйте, {update.effective_user.first_name}!\nВас приветствует Бот-калькулятор!\nВведите "/calc" чтобы начать работу, "/cancel" - чтобы закончить.')

def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Введите арифметическое выражние, используя пробелы.')
    return A

def calc(update, context):
    text = update.message.text
    try:
        result = logic.program(text)
        update.message.reply_text(f'{text} = {round(result, 3)}')
        logger.log_command(update, result)
    except ValueError:
        update.message.reply_text(f'Ошибка, повторите ввод.')
    return A

def cancel(update, context):
    update.message.reply_text(f'Завершение работы...')
    return ConversationHandler.END    

dispatcher.add_handler(CommandHandler('start', greet))
dispatcher.add_handler(ConversationHandler(entry_points=[CommandHandler("calc", start)], 
                                    states={A:[MessageHandler(Filters.text & (~ Filters.command), calc)]}, 
                                    fallbacks=[CommandHandler("cancel", cancel)]))

upd.start_polling()
upd.idle()