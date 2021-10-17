import os
import telebot

token = os.environ['TOKEN']
bot = telebot.TeleBot(token)
print(bot.get_me())
