import telebot
import time

bot_token = '1062179301:AAE9oSklFeh4JpdK8UmOjdJel1TYrp9tIt0'

bot = telebot.TeleBot(token=bot_token)

def find_at(msg):
    for text in msg:
        if '@' in text:
            return text

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Welcome! Type /help to to learn how to use it')


@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "Type some instagram account with '@' ")        

@bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text)
def at_answer(message):
    texts = message.text.split()
    at_text = find_at(texts)
    
    bot.reply_to(message, 'http://instagram.com/{}'.format(at_text[1:]))
    print(message)


while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)
    
'''
Api com o Lotti 

import telebot
import time
import json
import jsonpickle

bot_token = '1062179301:AAE9oSklFeh4JpdK8UmOjdJel1TYrp9tIt0'

bot = telebot.TeleBot(token=bot_token)

def find_at(msg):
    for text in msg:
        if '@' in text:
            return text

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Welcome! Type /help to to learn how to use it')


@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "Type some instagram account with '@' ")        

@bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text)
def at_answer(message):
    texts = message.text.split()
    at_text = find_at(texts)

    #make the message objc in string
    data = jsonpickle.encode(message)
    print(dict(data))
    
    # write the json file for the bot 
    with open('log.json', 'w') as hdl_file:
        json.dump(data, hdl_file)
    #    hdl_file.close()
    
    bot.reply_to(message, 'http://instagram.com/{}'.format(at_text[1:]))
    #rint(message)


while True:
    try:
        print('running bot...')
        bot.polling()
    except Exception:
        time.sleep(15)
    
'''


'''
Outra API teste

from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import telebot

updater = Updater(token='1062179301:AAE9oSklFeh4JpdK8UmOjdJel1TYrp9tIt0', use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def find_at_msg(msg):
    for text in msg:
        if '@' in text:
            return text

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text= "Type some instagram account with '@' ")

help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)
'''
