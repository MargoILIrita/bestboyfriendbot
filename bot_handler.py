import telebot
from bot import bot 
from messages import * 
from random import randint
from time import sleep, now
from db import *

def generate_answer(chat_id, mode=0):
    boy_type = get_boy_type(chat_id)
    list_ = DICT_TYPES[boy_type][mode]
    answer = list_[randint(0, len(list_))]
    if mode == 0:
        bot.send_message(chat_id, answer)
    elif mode == 1:
        bot.send_sticker(chat_id, answer)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    try:
        if is_user_exist(message.chat.id):
            bot.send_message(message.chat.id, HELLO_AGAIN_MESSAGE)
        else:
            add_user(message.chat.id, now())
            bot.send_message(message.chat.id, HELLO_MESSAGE)
            user_markup = telebot.types.ReplyKeyboardMarkup()
            for i in range(len(BOYFRIEND_TYPES)):
                user_markup.row(BOYFRIEND_TYPES[i])
            bot.send_message(message.chat.id, CHOOSE_YOUR_HERO, reply_markup=user_markup)
    except Exception as e:
        print(e)


@bot.message_handler(content_types=["text"])
def answer_text_message(message):
    try:
        sleep(randint(2, 10)) #for realism
        if message.text in CHOOSE_YOUR_HERO.values():
            boy_type = list(CHOOSE_YOUR_HERO.keys())[list(CHOOSE_YOUR_HERO.values()).index(message.text)]
            add_boyfriend_type(message.chat.id, boy_type)
            bot.send_message(message.chat.id, SUCCESS_LOAD[boy_type])
        else:
            generate_answer(message.chat.id)
    except Exception as e:
        print(e)

@bot.message_handler(content_types=["sticker"])
def answer_sticker(message):
    sleep(randint(2, 10)) #for realism
    try:
        generate_answer(message.chat.id, 1)
    except Exception as e:
        print(e)

if __name__ == '__main__':
     bot.polling(none_stop=True)