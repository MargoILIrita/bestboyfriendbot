import telebot
from bot import bot 
from messages import * 
from random import randint
from time import sleep
from datetime import date
from db import *

def generate_answer(chat_id, mode=0):
    boy_type = get_boy_type(chat_id)
    print('boy type got')
    list_ = DICT_TYPES[boy_type][mode]
    print('list get')
    answer = list_[randint(0, len(list_))]
    print('answer', answer)
    if mode == 0:
        bot.send_message(chat_id, answer)
    elif mode == 1:
        print('in mode')
        bot.send_sticker(chat_id, answer)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    try:
        if is_user_exist(message.chat.id):
            bot.send_message(message.chat.id, HELLO_AGAIN_MESSAGE)
        else:
            add_user(message.chat.id, date.today())
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
        if message.text in BOYFRIEND_TYPES.values():
            hide_markup = telebot.types.ReplyKeyboardRemove()
            boy_type = list(BOYFRIEND_TYPES.keys())[list(BOYFRIEND_TYPES.values()).index(message.text)]
            add_boyfriend_type(message.chat.id, boy_type)
            bot.send_message(message.chat.id, SUCCESS_LOAD[boy_type], reply_markup=hide_markup)
        else:
            sleep(randint(2, 10)) #for realism
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