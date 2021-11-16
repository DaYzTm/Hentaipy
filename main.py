import telebot
from telebot import types
from time import sleep
import random
import os
import urllib
import importlib
from werkzeug.wrappers import request
importlib.import_module('os.path')



bot = telebot.TeleBot('2042395634:AAFJtpVLUxgNwDoBBxVgMf4zPyony4J-y2E')
bot.remove_webhook()

#Команда /start
@bot.message_handler(commands=['start'])
def start(message):
  bot.send_message(message.chat.id, "Привет, это бета тест бота для хентай группы. Напишите /help что бы узнать как работает этот бот.")


ListOffsticker = os.listdir('C:\Bot\gitclone hentai\Henpybot\Art\Stickerart')

@bot.message_handler(commands=['stickerart'])
def start(message):
  if not ListOffsticker == []:
    stickerName = random.choice(ListOffsticker)
    sticker = open('C:\Bot\gitclone hentai\Henpybot\Art\Stickerart/' + stickerName, 'rb')
    bot.send_message(message.chat.id, 'Вот вам стикер senpai')
    bot.send_sticker(message.from_user.id, sticker)
    ListOffsticker.remove(stickerName)
  else:  
    bot.send_message(message.from_user.id, 'Стикеры закончились.')


ListOfImage = os.listdir('C:\Bot\gitclone hentai\Henpybot\Art\Echi')



@bot.message_handler(commands=['artechi'])
def start(message):
  if not ListOfImage == []:
    photoName = random.choice(ListOfImage)
    photo = open('C:\Bot\gitclone hentai\Henpybot\Art\Echi/' + photoName, 'rb')
    bot.send_message(message.chat.id, 'Вот вам артик senpai')
    bot.send_document(message.from_user.id, photo)
    ListOfImage.remove(photoName)
  else:  
    bot.send_message(message.from_user.id, 'Артики закончились.')

ListOffart = os.listdir('C:\Bot\gitclone hentai\Henpybot\Hentai')

@bot.message_handler(commands=['art'])
def start(message):
  if not ListOffart == []:
    photoartName = random.choice(ListOffart)
    photoart = open('C:\Bot\gitclone hentai\Henpybot\Hentai/' + photoartName, 'rb')
    bot.send_message(message.chat.id, 'Вот вам артик senpai')
    bot.send_document(message.from_user.id, photoart)
    ListOffart.remove(photoartName)
  else:  
    bot.send_message(message.from_user.id, 'Артики закончились.')

#Сохраняем присланый от пользователя файл commands=['downechi']  content_types=['document']

#@bot.message_handler(content_types=['document'])
#def handle_docs_photo(message):
   #try:
    #chat_id = message.chat.id
    #file_info = bot.get_file(message.document.file_id)
    #downloaded_file = bot.download_file(file_info.file_path)
    #src = 'C:/Bot/Art/Echi/' + message.document.file_name;
    #with open(src, 'wb') as new_file:
     #new_file.write(downloaded_file)
    #bot.reply_to(message, "Спасибо senpai за пополнение данных!")
   #except Exception as e:
    #bot.reply_to(message, e)
    
#Узнать то что делаю и то что уже сделано.
@bot.message_handler(commands=['patch'])
def start(message):
    bot.send_message(message.chat.id, "Patch 1.0\n1.Создан бот.\n2.Добавлены команды art, artechi пополненна база данных.\nPatch1.3\n1.Настроен рандом уровень отличный.\n2.Арты больше не повторяются бот сообщает когда они кончаются.\n3.Для разработчика облегченная загрузка файлов.\n4.Добавлена команда stickerart")

@bot.message_handler(commands=['jobs'])
def start(message):
    bot.send_message(message.chat.id, "1.Реализовать кнопки.\n2.Сделать отдельные арты для персонажей.\n3.Реализовать манги.\n4.Реализовать теги пример бдсм, двойное приникновение, лоликон, юри.\n5.Реализовать Анти-спам.")



#Команда /help
@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, "Список команд:\n/art - простой рандомный арт.\n/artpersy - Персонаж на выбор (В разработке)\n/artechi - Этти арты.\n/stickerart - Арт в форме стикера")


#Команда /start
@bot.message_handler(commands=['start'])
def start(message):
  bot.send_message(message.chat.id, "Привет, это бета тест бота для хентай группы. Напишите /help что бы узнать как работает этот бот.")


bot.polling(none_stop=True)

