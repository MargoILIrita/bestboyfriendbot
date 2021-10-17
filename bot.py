import config
import telebot

token = config.TOKEN
bot = telebot.TeleBot(token)
print(bot.get_me())
