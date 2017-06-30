from telegram.ext import Updater, CommandHandler
from time import strftime


up = Updater('381143222:AAHLQXTyoSOx7YCpHI6WKgqkVr-9qoegvrA')

def Horas(bot, update):
    msg = 'Olá {user_name} agora são: '
    msg += strftime('%H:%M:%S')

    bot.send_message(chat_id=update.message.chat_id,
                     text=msg.format(
                         user_name=update.message.from_user.first_name))
                         
def Duvida(bot, update):
    msg = 'Me explica como funciona isso passo a passo'
    bot.sendPhoto(chat_id=update.message.chat_id,
                  photo=open('img/duck.png', 'rb'))
    bot.send_message(chat_id=update.message.chat_id,
        	        text=msg.format())

def Comeca(bot, update):
    bot.sendPhoto(chat_id=update.message.chat_id,
                  photo=open('img/duck.png', 'rb'))

up.dispatcher.add_handler(CommandHandler('duvidas', Duvida))                  
up.dispatcher.add_handler(CommandHandler('horas', Horas))
up.dispatcher.add_handler(CommandHandler('start', Comeca))
up.dispatcher.add_handler(CommandHandler('help', Duvida))
up.dispatcher.add_handler(CommandHandler('ajuda', Duvida))
up.start_polling()