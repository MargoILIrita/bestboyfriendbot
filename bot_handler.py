from bot import bot 
from messages import * 
from random import randint
from time import sleep
from db import users_db


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, HELLO_MESSAGE)


@bot.message_handler(content_types=["text"])
def answer_sweet_message(message):
    try:
        answer = ANSWERS_LIST[randint(0, len(ANSWERS_LIST))]
        sleep(randint(2, 30)) #for realism
        bot.send_message(message.chat.id, answer)
    except Exception as e:
        print(e)

@bot.message_handler(content_types=["sticker"])
def answer_sticker(message):
    try:
        sticker_id = STICKERS_LIST[randint(0, len(STICKERS_LIST))]
        sleep(randint(2, 30))
        bot.send_sticker(message.chat.id, sticker_id)
    except Exception as e:
        print(e)

if __name__ == '__main__':
     bot.polling(none_stop=True)