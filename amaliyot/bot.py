import telebot
from telebot import types
import random
import xlrd

@bor.message_handler(commands=['start'])
def welcome(message):
    stic = open('stic/welcome.webp','rb')
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1=types.KeyboardButton("sss")
    but2 = types.KeyboardButton("eee")
    markup.add(but1,but2)

    bot.reply_to(message, "salom, {0.first_name}\n".format(message.from_user)
                 ,parse_mode='html',reply_markup=markup)
    bot.send_sticker(message.chat.i