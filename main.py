import configparser
from random import randrange
import telebot as tb 
import time
import configparser
import os
cfg = configparser.ConfigParser()
cfg.read("settings.ini")

try:
    token = cfg["bot"]["token"]
except KeyError:
    token = "321"

bot = tb.TeleBot(str(token))
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'test')

@bot.message_handler(content_types=["text"])
def ans(message):
    try:  
        pass
        
    except Exception as e:
        bot.send_message(message.chat.id, e)

bot.polling(none_stop=True, interval=0) 

