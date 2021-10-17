from datetime import datetime

import telebot
from bot import bot 
from messages import * 
from random import randint
from time import sleep
from datetime import datetime
from db import *

print(datetime.now(tz=None).timestamp())


def generate_answer(chat_id, mode=0):
    boy_type = get_boy_type(chat_id)
    list_ = DICT_TYPES[boy_type][mode]
    answer = list_[randint(0, len(list_))]
    if mode == 0:
        print(chat_id, answer)
    elif mode == 1:
        print(chat_id, answer)
