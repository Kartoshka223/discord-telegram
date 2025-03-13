import datetime
import random
import telebot
import randomcatimage
import requests
from PIL import Image
import os
import dog

TOKENTG = 'yourtoken'
bot = telebot.TeleBot(TOKENTG)
@bot.message_handler(commands = ['pol'])
def pol(message):
        msg = bot.send_message(message.chat.id,'отправь код сообщения, которое хочешь получить')
        bot.register_next_step_handler(msg,send_message)
def send_message(message):
        trt = message.text
        print(trt)
        with open("file.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                        if trt in line:
                                bot.send_message(message.chat.id,line)  

@bot.message_handler(commands = ['otv'])
def otv(message):
        msg = bot.send_message(message.chat.id,'отправь сообщение, которое хочешь передать в дс💨')
        bot.register_next_step_handler(msg,otv_v_file)
def otv_v_file(message):
        code = random.randint(10043,99979)
        date = datetime.datetime.now()
        format_date = date.strftime("%Y-%m-%d %H:%M:%S")
        msg = ''.join(message.text)
        bot.send_message(message.chat.id,f'Сообщение "{msg}" сохранено.')
        format_message = f'\nсообщение: "{msg}"' + f'код: {code}' + f' время отправки: {format_date}'
        with open("file.txt", "a") as file:
                file.write(format_message)

@bot.message_handler(commands = ['cat'])
def cat(message):
        cat = randomcatimage.getCat()
        papka = "papka_s_kotikami"
        if not os.path.isdir(papka):
                os.mkdir(papka)
        print(cat)
        img = random.randint(1000,9999)
        bot.send_photo(message.chat.id, photo=cat)

@bot.message_handler(commands = ['dog'])
def sobachka(message):

        papka = "papka_s_sobakami"
        if not os.path.isdir(papka):
                os.mkdir(papka)
        img = random.randint(1000,9999)
        sobaka = dog.getDog(directory= papka, filename=f'dog_{img}')
        bot.send_photo(message.chat.id, photo = open(f'{papka}/dog_{img}.jpg',"rb"))
bot.infinity_polling()
