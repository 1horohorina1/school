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
        url = 'http://'+conf.get("light","host")+'/'+conf.get("light","password")+'/?pt='+conf.get("light","light1")+'&cmd=get'
        print(url)
        response = urllib.request.urlopen(url)
        result = response.read()
        print(result)
        bot.send_message(message.chat.id, result)
    elif message.text.lower() == 'температура в помещении':
        url = 'http://'+conf.get("temperature","host")+'/'+conf.get("temperature","password")+'/?pt='+conf.get("temperature","port")+'&cmd=list'
        print(url)
        response = urllib.request.urlopen(url)
        result = response.read()
        print(result)
        for pair in result.decode().split(';'):
            print (pair)
        bot.send_message(message.chat.id, result)

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)


bot.polling()