import os
import telebot # importamos la libreria de telebot

bot=telebot.TeleBot('1709701852:AAH30YmfhefFNzErdbnlPiH_b_6f9zekGUk')

@bot.message_handler(commands=['hola'])
def hola(mensaje):
    bot.reply_to(mensaje,"Hola como estas")

@bot.message_handler(commands=['nombre'])
def nombrre(mensaje):
    bot.reply_to(mensaje,"Mi nombre es Selvin Guardado")

@bot.message_handler(commands=['edad'])
def edad(mensaje):
    bot.reply_to(mensaje,"Mi edad es 28 años")

@bot.message_handler(commands=['direccion'])
def direccion(mensaje):
    bot.reply_to(mensaje,"Mi direccion es Colonia Rivera Hernandez")

bot.polling()
