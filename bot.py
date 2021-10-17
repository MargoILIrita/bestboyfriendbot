import config
import telebot

token = config.TEST_TOKEN
bot = telebot.TeleBot(token)
print(bot.get_me())