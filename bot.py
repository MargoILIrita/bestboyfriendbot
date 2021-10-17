import os
import telebot
import config

token = os.environ['TOKEN']
bot = telebot.TeleBot(token)
print(bot.get_me())
