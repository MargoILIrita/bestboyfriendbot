import os
import telebot

token = os.environ['DATABASE_URL']
bot = telebot.TeleBot(token)
print(bot.get_me())
