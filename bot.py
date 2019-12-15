import telebot
import urllib.request
from telebot import apihelper
import configparser

# socks5 proxy
apihelper.proxy = {'https':'socks5h://10.1.1.2:9050'}

bot = telebot.TeleBot('1002769513:AAEwBuNPD0RczYAkYRa8pgn5suuw1Y2VAIM')

conf=configparser.ConfigParser()
conf.read("school.conf")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')
    elif message.text.lower() == 'свет в комнате':
        response = urllib.request.urlopen('http://10.1.3.12/sec/?pt=7&cmd=get')
        result = response.read()
        print(result)
        bot.send_message(message.chat.id, result)

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)


bot.polling()