from bot import bot 
from  messages import ANSWERS_LIST, HELLO_MESSAGE
import random as rand


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, HELLO_MESSAGE)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    answer = ANSWERS_LIST[rand.randint(len(ANSWERS_LIST))]
    bot.send_message(message.chat.id, answer)


if __name__ == '__main__':
     bot.polling(none_stop=True)
