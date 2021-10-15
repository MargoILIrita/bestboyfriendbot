from bot import bot 
from messages import * 
import random


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, HELLO_MESSAGE)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    try:
        answer = ANSWERS_LIST[random.randint(0, len(ANSWERS_LIST))]
        bot.send_message(message.chat.id, answer)
    except Exception as e:
        print(e)

if __name__ == '__main__':
     bot.polling(none_stop=True)