# This Python file uses the following encoding: utf-8
# (env) $ pip freeze > requirements.txt
# python -m venv Venv  - имя папки
import telebot
from telebot import types
from config import decouple


TOKEN = decouple.config('KEY')
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


# @bot.message_handler(content_types=['text'])
# def get_message_text(message):
#     if message.text == 'Hello':
#         bot.send_message(message.chat.id, 'и тебе ПРИВЕТ!', parse_mode='html')
#     elif message.text == 'id':
#         bot.send_message(message.chat.id, f'Твой id: {message.from_user.id}', parse_mode='html')
#     elif message.text == 'photo':
#         photo = open('airplane_22318.png', 'rb')
#         bot.send_photo(message.chat.id, photo)
    # else:
    #     bot.send_message(message.chat.id, 'Я тебя не понимаю!', parse_mode='html')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'ВАУ, крутое ФОТО!')


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Посетить веб сайт', url='http://itproger.com'))
    bot.send_message(message.chat.id, 'Перейдите на сайт!', reply_markup=markup)


@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)  # Выглядят красиво кнопки
    my_website = types.KeyboardButton('Веб сайт')
    my_start = types.KeyboardButton('Start')
    markup.add(my_website, my_start)
    bot.send_message(message.chat.id, 'Список кнопок!', reply_markup=markup)


bot.polling(none_stop=True)
# 2e12e12e
