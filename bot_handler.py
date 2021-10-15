from bot import bot 
from messages import * 
import random


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, HELLO_MESSAGE)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)
    try:
        bot.send_message(message.chat.id, random.randint(0, len(ANSWERS_LIST)))
    except Exception as e:
        print(e)

if __name__ == '__main__':
     bot.polling(none_stop=True)